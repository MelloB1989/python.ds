import pandas as pd
import numpy as np

s1 = np.array([1,2])
s2 = np.array([3,4])
s3 = np.array([5,6])

s11 = pd.Series(s1, index=['S1', 'S2'])
s22 = pd.Series(s2, index=['S1', 'F2'])
s33 = pd.Series(s3, index=['G1', 'G2'])

df = pd.DataFrame({'A': s11, 'B': s22, 'C': s33})
df.columns = ['Column1', 'Column2', 'Column3']
print(df)
print("Printing Head:")
print(df.head(2))
print("Printing tail")
print(df.tail(2))
print(df.describe())
print("Sorted data:")
print(df.sort_values(by='Column3'))
print(df[df['Column1'] == 2.0])
print(df.groupby('Column2').mean())
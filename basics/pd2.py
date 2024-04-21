import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [2, 3], 'C': [5, 6]})
merged_df = pd.merge(df1, df2, on='A')  # Merges df1 and df2 on column 'A'
print(df1)
print(df2)
print(merged_df)
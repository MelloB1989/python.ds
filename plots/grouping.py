import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,5), columns=['a','b','c','d','e'], index=['Joe', 'John', 'Mia', 'Lia', 'Lisa'])

mapping = {
    'a': 'red',
    'b': 'red',
    'c': 'blue',
    'd': 'blue',
    'e': 'red'
}

grouped = df.T.groupby(mapping).count()
#print(grouped)

#Grouping by function
keys = ['one','one','one','two','two']
g2 = df.groupby([len, keys]).max()
print(g2)
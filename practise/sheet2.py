import numpy as np
import pandas as pd

index = ['a','b','c','d','e','f','g','h','i','j']
djson = {
    'attempts': [1,3,2,3,2,3,1,1,2,1],
    "name": ['Anadffvc','Dimadsf','Kathdfs','James','Emily','Mach','Matt','Laura','Kevin','Jonas'],
    "qualify": ['yes','no','yes','no','no','yes','yes','no','no','yes'],
    "score": [12.5,9.0,16.5,np.nan,9.0,20.0,14.5,np.nan,8.0,19.0]
}

df = pd.DataFrame(djson)

#Replace NaN with 0
df = df.fillna(0)

#Extract first five characters of name col
#names = df['name'].values
names = df['name'].str.extract(r'(^.{5})')

print(names)

print(df)
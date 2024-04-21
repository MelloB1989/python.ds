import pandas as pd
import pickle

data={'team':['SA','pakisthan','NZ','uganda','bangladesh'],
      'matches':[23,23,21,20,24],'won':[15,14,13,13,11],
      'lost':[8,6,8,5,13]}
df=pd.DataFrame(data)

df.to_pickle('data.pickle')
p = pickle.dumps(df)

print(p)
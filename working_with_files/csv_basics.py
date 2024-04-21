import pandas as pd
data=pd.DataFrame({'Matches':[23,23,21,20,24],'Won':[15,14,13,13,11],'Lost':[8,6,8,5,13],'Tied':[0,0,0,0,0]},index=['South Africa','Pakisthan','New Zeland','Uganda','Bangladesh'])

#print(data)

data.to_csv('data.csv')
data.to_html('data.html')
data.to_xml('data.xml')
data.to_json('data.json')

d = pd.read_csv('data.csv', header=None, index_col=2)
print(d)

d = pd.read_json('data.json')
print(d)
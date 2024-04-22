import pandas as pd
from lxml import objectify
import os
import sqlite3

index = ['Agfa ePhoto 1280', 'Canon EOS 10D', 'Epson', 'Fujifilm', 'HP', 'Kodak', 'Nikon', 'Olympus']
release_date = pd.Series([1997,2003,1997,2004,2005,2004,2004,2005], index=index)
max_res = pd.Series([1024,3072,640,4256,2592,0,2288,2592], index=index)
low_res = pd.Series([640,2048,320,3024,2048,0,1600,2288], index=index)
effec_pixels = pd.Series([0,6,0,6,5,2,3,5], index=index)
zoom_wide = pd.Series([38,0,43,0,36,37,35,38], index=index)

df = pd.DataFrame({
    'Release_Date': release_date,
    'Max_resolution': max_res,
    'Low_resolution': low_res,
    'Effective_pixels': effec_pixels,
    'Zoom_wide': zoom_wide
})

#df.columns = ['Release Date', "max res", "low res", "effe", "zoom"] #Change col names

#Print the DF
print(df)

#Convert to XML
#df.to_xml('sheet1.xml')

#Read from XML
# parsed = objectify.parse(open('sheet1.xml'))

# root = parsed.getroot()

# indexs = []

# for i in root.getchildren():
#     for j in i.getchildren():
#         if j.tag == 'Release_Date': #Get any col
#             indexs.append(j.text)
#             print(j.text)

#print(indexs)

#Convert to feather
#df.to_feather('sheet1')
#os.system('cat sheet1')

conn = sqlite3.connect('sheet1.db')
#q = "create table emp( id number(10), name char(100) )"
#q = "INSERT INTO emp(id, name) VALUES (1,'aparna')"
q = 'select * from emp'
#q = 'update emp set name = "Aparna" where name = "aparna"'
r = conn.execute(q)
print(r.fetchall()) # To get
conn.commit()
import sqlite3

db = sqlite3.connect('data.db')
"""
try:
    cur = db.cursor()
    q = 'create table emp(id number(5) primary key, name char(100) not null, dept char(50))'
    cur.execute(q)
    print("Done")
except:
    print("Fked")
"""

q = "insert into emp(id,name,dept) values (?,?,?)"
id = int(input("ID: "))
name = input("Name: ")
dept = input("Dept: ")
try:
    cur = db.cursor()
    r = cur.execute(q, (id, name, dept))
    db.commit()
    print(r)
except:
    print('fked')
import sqlite3

db = sqlite3.connect('data.db')

q = "SELECT * FROM emp where id > 1"

cur = db.cursor()
cur.execute(q)

print(cur.fetchall())
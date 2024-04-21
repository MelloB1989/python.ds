import pandas as pd

s = pd.Series(['Tokyo', 'Lisbon', 'Paris'])
s.index = ['C1', 'C2', 'C3']

print(s.str.match(pat='(T$)'))

s = pd.Series(['This is a string', 'https://noobsverse.com'])

print(s.str.split())
print(s.str.split(':'))
print(s.str.split(r'is|a'))
print(s.str.split(r'.'))
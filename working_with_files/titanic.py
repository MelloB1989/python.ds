import pandas as pd

data = pd.read_csv('titanic.csv')

print(data)

#Replacing Na values with mean
age_mean = data['age'].mean()

data['age'] = data['age'].fillna(age_mean)
survived = data[data['survived'] == 1]
survived = survived.sort_values(by='age')
print(survived)
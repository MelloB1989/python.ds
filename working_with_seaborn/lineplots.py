import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('flights')

# Line plot for each year
sns.lineplot(data=df, x="month", y="passengers", hue="month")
plt.title('Monthly Passengers Over Years')
plt.show()
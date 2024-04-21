import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset('tips')

# Bar plot showing average tip by day
sns.barplot(data=tips, x='day', y='tip', ci=None)
plt.title('Average Tip by Day')
plt.show()

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
ax.set_xticks([1, 2, 3, 4, 5])
#ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'])
plt.show()

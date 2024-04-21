import matplotlib.pyplot as plt

fig, ax = plt.subplots(2)  # Creates a figure and two subplots vertically
ax[0].plot([1, 2, 3], [1, 4, 9])
ax[1].plot([1, 2, 3], [1, 2, 3])
plt.show()

plt.plot([1, 2, 3], [4, 5, 6], color='red', marker='o', linestyle='--')
plt.show()

"""
Figures: A figure in Matplotlib acts as a container for all plot elements. It can contain one or more axes objects.
Subplots: Subplots are axes that allow multiple plots to be shown in the same figure. They are organized in a grid. You can create subplots using plt.subplots() or plt.subplot().
"""
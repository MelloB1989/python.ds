import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum(), label='left boob')
ax.plot(np.random.randn(1000).cumsum(), 'g--', label='right boob')

ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='medium')
ax.set_xlabel('BOOBS')
ax.legend(loc='best')
circ = plt.Circle((5.7,5.2), 90.15, color='r', alpha=0.3)
ax.add_patch(circ)
plt.show()
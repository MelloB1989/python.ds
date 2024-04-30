import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure()

# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)

# plt.plot(np.random.randn(50).cumsum(), 'k--')
# ax1.hist(np.random.randn(100), bins=50, color='r', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))

fig, axes = plt.subplots(3,3, sharex=True, sharey=True)

for i in range(3):
    for j in range(3):
        axes[i,j].scatter(np.arange(30), np.arange(30) + 5 * np.random.randn(30))

plt.show()
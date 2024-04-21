import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_axes([1,2,3,4])
ax=fig.add_axes([9,8,7,6])

x = np.arange(20,4,8)
plt.subplot(2,4,2)
plt.plot(x, np.sin(x))
plt.show()
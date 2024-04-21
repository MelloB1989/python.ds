import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([6,9,1])
ypoints = np.array([9,4,5])

#plt.plot(xpoints, ypoints, 'p-.r')
plt.title('Test')
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(xpoints, ypoints, marker='h',ms=50, mec='r', mfc='k')
plt.axis([0, 10, 0, 10])

plt.show()
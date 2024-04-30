import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(np.random.randn(10, 4).cumsum(0), columns=['A', 'B', 'C', 'D'], index=np.arange(0,100,10))

#print(np.random.randn(10, 4).cumsum(0))
print(np.random.normal(10,2,size=100))

df.plot()
#plt.show()
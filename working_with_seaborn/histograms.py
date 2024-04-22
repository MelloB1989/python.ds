import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset('penguins')

# Histogram with a kernel density estimate (KDE)
sns.histplot(penguins, x='flipper_length_mm', kde=True)
plt.title('Flipper Length Distribution')
plt.show()
"""
How KDE Works:
KDE works by placing a continuous kernel (like a Gaussian) at each data point. The kernel is typically a symmetrical function centered at each data point, and it spreads out the influence of that data point over a range determined by a bandwidth parameter. The overall density function is then the sum of these individual kernels. The bandwidth parameter controls how smooth the resulting density estimate is: a larger bandwidth leads to a smoother, less detailed estimate, while a smaller bandwidth captures more detail but can lead to a noisier estimate.

Purpose and Uses of KDE:
KDE is used to:

Visualize Data: It provides a smooth, continuous estimation of data distribution, which can be more informative and appealing than a histogram.
Estimate the Density Function: This can be useful for outlier detection, data analysis, or as an input for further statistical methods.
Compare Distributions: KDE can help compare the underlying distributions of different datasets on a common set of axes.
"""
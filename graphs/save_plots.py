import matplotlib.pyplot as plt

# Create some data
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]

# Plot the data
plt.plot(x, y)
plt.title('Example Plot')

# Save the figure
plt.savefig('plot.png')  # Saves the plot as a PNG file
plt.savefig('plot_high_res.png', dpi=300)  # High-resolution output
plt.savefig('plot.svg', format='svg')  # Vector format for scalability without loss of quality
plt.savefig('plot.jpg')  # High-quality JPEG
plt.savefig('plot_transparent.png', transparent=True)  # Transparent background
plt.close()  # Closes the plot window to free up resources
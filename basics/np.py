import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# crate 2d array of (3,3) shape
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# reshape the array to (9,1)
arr = arr.reshape(1, 9)
print(arr)

arr = np.array([3, 7, 1, 9, 9, 3, 2, 1, 4])

# Get the maximum value from the array
print(arr.max())

# Get the minimum value from the array
print(arr.min())

#Get values greater than 4
print(arr[arr > 4])
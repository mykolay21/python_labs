import numpy as np

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

###################################
arr = np.array([1, 2, 3, 4, 5])

# Element-wise operations
print(arr + 5)  # Adds 5 to each element
print(arr * 2)  # Multiplies each element by 2
#######################################
arr = np.array([1, 2, 3, 4, 5])

print(np.mean(arr))   # Mean
print(np.sum(arr))    # Sum
print(np.std(arr))    # Standard deviation
#############################################
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.dot(A, B))  # Matrix multiplication
print(np.linalg.inv(A))  # Inverse of matrix A

################################################
rand_arr = np.random.rand(3, 3)  # 3x3 matrix with random numbers
print(rand_arr)

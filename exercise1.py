import numpy as np

# Create matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix addition
addition_result = matrix1 + matrix2
print("Matrix Addition:\n", addition_result)

# Scalar multiplication
scalar_result = 3 * matrix1
print("\nScalar Multiplication:\n", scalar_result)

# Dot product
dot_product_result = np.dot(matrix1, matrix2)
print("\nDot Product:\n", dot_product_result)

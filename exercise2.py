import numpy as np
import matplotlib.pyplot as plt

# Define vectors
vector1 = np.array([1, 2])
vector2 = np.array([3, 1])

# Plot the vectors
origin = [0], [0]  # origin point
plt.quiver(*origin, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
plt.quiver(*origin, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 2')

# Modify vector values and re-plot (Optional)
vector1 = np.array([2, 3])
plt.quiver(*origin, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='g', label='Modified Vector 1')

# Set plot limits and labels
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.title("Vector Visualization")
plt.show()
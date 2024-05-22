import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the point cloud data from the CSV file
data = np.loadtxt('PC_sm.csv', delimiter=',')

# Perform Singular Value Decomposition (SVD) on the centered data
U, S, Vt = np.linalg.svd(data - np.mean(data, axis=0))

# The columns of Vt are the principal directions
principal_directions = Vt.T

# Plotting the point cloud and the principal axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='blue', marker='o', alpha=0.5, s=1)

# Plot the principal axes
center = np.mean(data, axis=0)
for i in range(3):
    # Each axis is a line from the mean to the direction defined by the singular vector,
    # scaled by the singular value
    ax.quiver(center[0], center[1], center[2],
              principal_directions[0, i], principal_directions[1, i], principal_directions[2, i],
              length=S[i], normalize=True, color=['r', 'g', 'b'][i])

# Setting labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('Point Cloud with Principal Axes (xyz)')
plt.show()

# The unit axes are:
unit_axis_1 = principal_directions[:, 0]  # Red axis
unit_axis_2 = principal_directions[:, 1]  # Green axis
unit_axis_3 = principal_directions[:, 2]  # Blue axis

# Now, let's print these unit axes:
print("Unit Axis 1 (Red):", unit_axis_1)
print("Unit Axis 2 (Green):", unit_axis_2)
print("Unit Axis 3 (Blue):", unit_axis_3)

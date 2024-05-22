import numpy as np
import matplotlib.pyplot as plt
import csv

# Generate x_values ranging from 1 to 5621
x_values = np.linspace(1, 5621, 5621)

# Read y_values from CSV file
y_values_file = 'Samsung.csv'
with open(y_values_file, 'r') as file:
    reader = csv.reader(file)
    # Skip first row
    next(reader)
    # Read only the fifth column from the second row (assuming it contains the y-values)
    y_values = [float(row[4]) for row in reader]

# Plot the original data points
plt.plot(x_values, y_values, '-', label='Data Points')

# Add labels and title
plt.xlabel('Evenly spaced points in days')
plt.ylabel('Closed Prices')
plt.title('Original Data Points')
plt.legend()
plt.grid(True)

# Show plot
plt.show()

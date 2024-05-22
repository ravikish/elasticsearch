import numpy as np
import matplotlib.pyplot as plt
import csv


def lagrange_interpolation(x_values, y_values, degree):
    """
    Perform Lagrange interpolation using NumPy's polyfit function.

    Parameters:
        x_values (array-like): The x-coordinates of the data points.
        y_values (array-like): The y-coordinates of the data points.
        degree (int): The degree of the polynomial to be used for interpolation.

    Returns:
        np.poly1d: The interpolating polynomial.
    """
    # Perform polynomial interpolation using polyfit
    coeffs = np.polyfit(x_values, y_values, degree)
    interpolating_polynomial = np.poly1d(coeffs)
    return interpolating_polynomial


# Generate x_values ranging from 1 to 250
x_values = np.linspace(1, 5621, 5621)

# Read y_values from CSV file
y_values_file = 'Samsung.csv'
with open(y_values_file, 'r') as file:
    reader = csv.reader(file)
    # Skip first row
    next(reader)
    # Read only the first column from the second row
    y_values = [float(row[4]) for row in reader]

degree = 5

# Perform Lagrange interpolation
interpolating_polynomial = lagrange_interpolation(x_values, y_values, degree)

# Generate points for plotting the interpolating polynomial
x_plot = np.linspace(min(x_values), max(x_values), 100)
y_plot = interpolating_polynomial(x_plot)

# Plot the original data points
plt.plot(x_values, y_values, 'bo', label='Data Points')

# Plot the interpolating polynomial
plt.plot(x_plot, y_plot, 'r-', label='Interpolating Polynomial')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation')
plt.legend()
plt.grid(True)

# Show plot
plt.show()

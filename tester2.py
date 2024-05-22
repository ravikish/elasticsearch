import numpy as np
import matplotlib.pyplot as plt
import csv


def newton_interpolation(x_values, y_values, degree):
    """
    Perform Newton's divided differences interpolation.

    Parameters:
        x_values (array-like): The x-coordinates of the data points.
        y_values (array-like): The y-coordinates of the data points.
        degree (int): The degree of the polynomial to be used for interpolation.

    Returns:
        np.poly1d: The interpolating polynomial.
    """
    n = len(x_values)
    F = np.zeros((n, n))
    for i in range(n):
        F[i, 0] = y_values[i]

    for j in range(1, n):
        for i in range(j, n):
            F[i, j] = (F[i, j - 1] - F[i - 1, j - 1]) / (x_values[i] - x_values[i - j])

    coefficients = F[0, :degree + 1]
    powers = np.arange(degree + 1)

    return np.poly1d(coefficients[::-1], True)(powers[::-1])


# Generate x_values ranging from 1 to 252
x_values = np.linspace(1, 5621, 5621)

# Read y_values from CSV file
y_values_file = 'Samsung.csv'
with open(y_values_file, 'r') as file:
    reader = csv.reader(file)
    # Skip first row
    next(reader)
    # Read only the first column from the second row
    y_values = [float(row[4]) for row in reader]

degree_5 = 3
#degree_50 = 50

# Perform Newton's divided differences interpolation for degree 5
interpolating_polynomial_deg5 = newton_interpolation(x_values, y_values, degree_5)

# Perform Newton's divided differences interpolation for degree 50
#interpolating_polynomial_deg50 = newton_interpolation(x_values, y_values, degree_50)

# Print the equations
print("Interpolating polynomial for degree 5:")
print(interpolating_polynomial_deg5)

print("\nInterpolating polynomial for degree 50:")
#print(interpolating_polynomial_deg50)

# Generate points for plotting the interpolating polynomial for degree 5
x_plot = np.linspace(min(x_values), max(x_values), 100)
y_plot_deg5 = np.polyval(interpolating_polynomial_deg5, x_plot)

# Generate points for plotting the interpolating polynomial for degree 50
#y_plot_deg50 = np.polyval(interpolating_polynomial_deg50, x_plot)

# Plot the original data points
plt.plot(x_values, y_values, 'bo', label='Data Points')

# Plot the interpolating polynomials
plt.plot(x_plot, y_plot_deg5, 'r-', label='Interpolating Polynomial (Degree 5)')
#plt.plot(x_plot, y_plot_deg50, 'g-', label='Interpolating Polynomial (Degree 50)')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Newton\'s Divided Differences Interpolation')
plt.legend()
plt.grid(True)

# Show plot
plt.show()

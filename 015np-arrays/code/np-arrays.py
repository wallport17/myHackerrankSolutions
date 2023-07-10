import numpy as np

# Original data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Fit a linear regression line
coefficients = np.polyfit(x, y, 1)
slope = coefficients[0]
intercept = coefficients[1]

# Calculate predicted values using the linear function
predicted = slope * x + intercept

# Calculate percent error
percent_error = (abs(y - predicted) / y) * 100

print(percent_error)
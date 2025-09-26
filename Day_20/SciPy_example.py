import numpy as np
from scipy.optimize import minimize

# Define a function to minimize
def f(x):
    return x**2 + 3*x + 5  # Quadratic function

# Minimize the function starting at x=0
result = minimize(f, x0=0)

print("Minimum value of function:", result.fun)
print("Optimal x value:", result.x)
###############################
from scipy.integrate import quad

# Define a function to integrate
def f(x):
    return x**2  # Integrating x^2

# Compute definite integral from 0 to 2
integral, error = quad(f, 0, 2)

print("Integral result:", integral)
print("Estimated error:", error)
########################################
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Given data points
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 3, 5, 7])

# Create interpolation function
f_interp = interp1d(x, y, kind='cubic')

# Generate new x values for smooth curve
x_new = np.linspace(0, 4, 50)
y_new = f_interp(x_new)

# Plot results
plt.scatter(x, y, color='red', label="Original Data")
plt.plot(x_new, y_new, label="Cubic Interpolation")
plt.legend()
plt.show()
##############################################################
from scipy.linalg import solve

# Define a system of equations:
#  2x + y = 1
#  3x + 4y = 7

A = np.array([[2, 1], [3, 4]])  # Coefficients matrix
b = np.array([1, 7])  # Right-hand side

solution = solve(A, b)
print("Solution for x and y:", solution)
#################################################################
from scipy.stats import norm

# Generate random numbers from a normal distribution
samples = norm.rvs(loc=0, scale=1, size=10)
print("Random normal samples:", samples)

# Compute probability density function (PDF) at x=0
print("PDF at x=0:", norm.pdf(0, loc=0, scale=1))

# Compute cumulative distribution function (CDF) at x=0
print("CDF at x=0:", norm.cdf(0, loc=0, scale=1))
####################################################################

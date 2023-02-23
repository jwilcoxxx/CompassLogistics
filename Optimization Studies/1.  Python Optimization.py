import scipy
from scipy.optimize import minimize
import numpy as np

def objective(x):
    return x[0]**2 + x[1]**2

def constraint1(x):
    return x[0] + x[1] - 1

def constraint2(x):
    return 1 - x[0] - x[1]

# Initial guess
x0 = np.array([0, 0])

# Constraints
# Sample Change to test GitHub SetUp
# Another change in comments
cons = ({'type': 'eq', 'fun': constraint1} ,
        {'type': 'ineq', 'fun': constraint2})

# Optimize
sol = minimize(objective, x0, constraints=cons)

# Results
print(sol.x)

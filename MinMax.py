import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import seaborn as sns
from Functions import f_1, f_2

plt.rcParams['text.usetex'] = False

# Define the range for X
A = 10  # Range of x, can be adjusted

# List to store Pareto-optimal results for min-max method
pareto_optimal = []

# Define the ideal values for f1 and f2 based on the individual minimization of the convex functions
z1_star = 0
z2_star = 0

# Generate a list of weight values in the range from 0 to 1 with 101 points
w_values = np.linspace(0, 1, 101)

# Step 1: Minimize the objective function using the min-max method
for w in w_values:
    # Define the objective for min-max method
    def objective(vars):
        return vars[1]  # Minimize D

    # Define the constraints
    def constraints(vars):
        x = vars[0]
        D = vars[1]
        # Calculate differences from ideal values
        diff_f1 = f_1(x) - z1_star
        diff_f2 = f_2(x) - z2_star
        
        return [
            D - w * diff_f1,   # Ensure D >= w * diff_f1
            D - (1 - w) * diff_f2  # Ensure D >= (1 - w) * diff_f2
        ]

    # Set up the constraints in the required format
    constraints_dict = [{'type': 'ineq', 'fun': constraints}]
    bounds = [(-A, A), (None, None)]  # Limits for x and D
    x0 = [0.0, 0.0]  # Initial guess

    # Minimize the objective function with constraints
    opt = minimize(objective, x0, bounds=bounds, constraints=constraints_dict)
    
    # Check if the optimization was successful
    if opt.success:
        # Store the result in a dictionary with the values of f_1(x) and f_2(x)
        result = {
            "x": opt.x[0],
            "f_1(x)": f_1(opt.x[0]),
            "f_2(x)": f_2(opt.x[0])
        }
        # Add the Pareto-optimal solution to the list
        pareto_optimal.append([result['x'], result['f_1(x)'], result['f_2(x)']])
    else:
        print(f"Optimization failed for w={w}: {opt.message}")

# Convert the list to a NumPy array for plotting
pareto_optimal = np.array(pareto_optimal)

# Plot the Pareto front (f_1 vs f_2)
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
plt.scatter(pareto_optimal[:, 1], pareto_optimal[:, 2], c='purple', s=30, alpha=0.7, label='Pareto Optimal Solutions')

plt.xlabel('$f_1(x)$', fontsize=16) 
plt.ylabel('$f_2(x)$', fontsize=16)  
plt.title('Pareto Front for the Schaffer Problem', fontsize=16) 
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.grid()
plt.legend(fontsize=16)
plt.tight_layout()
plt.savefig("MinMax.png")
plt.show()

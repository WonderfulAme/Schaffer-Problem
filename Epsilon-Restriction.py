import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from Functions import f_1, f_2
import seaborn as sns
plt.rcParams['text.usetex'] = False


# Define the range for X and the weights
A = 10  # Range of x, can be adjusted

# List to store Pareto-optimal results for f_1 minimization
pareto_optimal_f1 = []

# Generate a list of epsilon values in the range from 0 to 10 with 101 points
epsilon_values = np.linspace(0, 10, 101)

# Step 1: Minimize f_1(x) with a constraint on f_2(x)
for epsilon in epsilon_values:
    # Restriction on f_2(x) with epsilon constraint
    constraints = [{'type': 'ineq', 'fun': lambda x: epsilon - f_2(x)}]
    bounds = [(-A, A)]  # Bounds for x
    x0 = [0.0]  # Initial guess
    
    # Minimize the objective function f_1(x) subject to the constraint on f_2(x)
    opt = minimize(f_1, x0, bounds=bounds, constraints=constraints)
    
    # Store the result in a dictionary with the values of f_1(x) and f_2(x)
    result = {
        "x": opt.x[0],
        "f_1(x)": f_1(opt.x[0]),
        "f_2(x)": f_2(opt.x[0])
    }
    # Add the Pareto-optimal solution to the list for f_1 minimization
    pareto_optimal_f1.append([result['x'], result['f_1(x)'], result['f_2(x)']])

# Convert the list to a NumPy array for plotting f_1 minimization
pareto_optimal_f1 = np.array(pareto_optimal_f1)


# Step 2: Minimize f_2(x) with a constraint on f_1(x)
pareto_optimal_f2 = []

for epsilon in epsilon_values:
    # Restriction on f_1(x) with epsilon constraint
    constraints = [{'type': 'ineq', 'fun': lambda x: epsilon - f_1(x)}]
    bounds = [(-A, A)]  # Bounds for x
    x0 = [0.0]  # Initial guess
    
    # Minimize the objective function f_2(x) subject to the constraint on f_1(x)
    opt = minimize(f_2, x0, bounds=bounds, constraints=constraints)
    
    # Store the result in a dictionary with the values of f_1(x) and f_2(x)
    result = {
        "x": opt.x[0],
        "f_1(x)": f_1(opt.x[0]),
        "f_2(x)": f_2(opt.x[0])
    }
    # Add the Pareto-optimal solution to the list for f_2 minimization
    pareto_optimal_f2.append([result['x'], result['f_1(x)'], result['f_2(x)']])

# Convert the list to a NumPy array for plotting f_2 minimization
pareto_optimal_f2 = np.array(pareto_optimal_f2)

# Plot both Pareto fronts (f_1 vs f_2)
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Plot Pareto front for f_1 minimization
plt.scatter(pareto_optimal_f1[:, 1], pareto_optimal_f1[:, 2], c='purple', s=30, alpha=0.7, 
            label=r'Pareto Optimal Solutions Taking $f_1$ as Objective')

# Plot Pareto front for f_2 minimization
plt.scatter(pareto_optimal_f2[:, 1], pareto_optimal_f2[:, 2], c='orange', s=30, alpha=0.7, 
            label=r'Pareto Optimal Solutions Taking $f_2$ as Objective')


plt.xlabel('$f_1(x)$', fontsize=16) 
plt.ylabel('$f_2(x)$', fontsize=16)  
plt.title('Pareto Front for Schaffer Problem', fontsize=16) 
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.grid()
plt.legend(fontsize=16)
plt.tight_layout()
plt.savefig("Epsilon-Restriction.png")
plt.show()

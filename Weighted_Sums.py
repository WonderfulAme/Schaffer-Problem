import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from Functions import f_1, f_2

# Define the range for X and the weights
A = 10  # Range of x, can be adjusted

# List to store Pareto-optimal results
pareto_optimal = []

# Generate a list of weights in the range from 0 to 1 with 101 points
weights = np.linspace(0, 1, 101)

# For each weight in the list
for w in weights:
    # Minimize a weighted combination of f_1(x) and f_2(x)
    opt = minimize(lambda x: w * f_1(x) + (1 - w) * f_2(x), 0.0, bounds=[(-A, A)], method='SLSQP')
    
    # Store the result in a dictionary with the values of f_1(x) and f_2(x)
    result = {
        "x": opt.x[0],
        "f_1(x)": f_1(opt.x[0]),
        "f_2(x)": f_2(opt.x[0])
    }
    # Add the Pareto-optimal solution to the list
    pareto_optimal.append([result['x'], result['f_1(x)'], result['f_2(x)']])

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
plt.savefig("Weighted_Sums.png")
plt.show()

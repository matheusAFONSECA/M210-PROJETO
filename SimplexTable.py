import pulp

# Create a maximization problem
problem = pulp.LpProblem("Simplex Optimization", pulp.LpMaximize)

# Define the decision variables
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)

# Define the objective function
problem += 3*x + 5*y

# Define the constraints
problem += 2*x + y <= 10
problem += x + 3*y <= 12

# Solve the problem
problem.solve()

# Print the optimal solution
print("Optimal Solution:")
print("x =", pulp.value(x))
print("y =", pulp.value(y))
print("Objective =", pulp.value(problem.objective))
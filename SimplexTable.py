import pulp

# Create a maximization problem
problem = pulp.LpProblem("Simplex Optimization", pulp.LpMaximize)

# Define the decision variables
e = pulp.LpVariable("e", lowBound=0)
m = pulp.LpVariable("m", lowBound=0)
a = pulp.LpVariable("a", lowBound=0)
p = pulp.LpVariable("p", lowBound=0)

# Define the objective function
problem += 80*e + 70*m + 100*a + 16*p

# Define as restrições com nomes
problem += e + m + a + 4*p <= 250, "Restrição 1"
problem += m + a + 2*p <= 600, "Restrição 2"
problem += 3*e + 2*m + 4*a <= 500, "Restrição 3"

# Solve the problem
problem.solve()

# Print the optimal solution
print("Solução ótima:")
print("e =", pulp.value(e))
print("m =", pulp.value(m))
print("a =", pulp.value(a))
print("s =", pulp.value(p))
print("Z* =", pulp.value(problem.objective))

# Imprime os preços sombra de cada restrição
print("\nPreços sombra (multiplicadores de Lagrange) para cada restrição:")
for name, constraint in problem.constraints.items():
    print(f"{name}: {constraint.pi}")
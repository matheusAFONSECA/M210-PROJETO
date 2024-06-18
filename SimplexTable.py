import pulp

def simplex_optimization(objective_coeffs, constraints, bounds):
    """    
    Parâmetros:
    - objective_coeffs: lista de coeficientes da função objetivo.
    - constraints: lista de tuplas contendo os coeficientes das restrições e os limites superiores.
    - bounds: lista de limites inferiores das variáveis de decisão.
    
    Retorna:
    - solução ótima para as variáveis de decisão.
    - valor ótimo da função objetivo.
    - preços sombra para cada restrição.
    - sobras de cada restrição.
    """
    # Cria um problema de maximização
    problem = pulp.LpProblem("Simplex Optimization", pulp.LpMaximize)

    # Define as variáveis de decisão com os limites inferiores fornecidos
    variables = [pulp.LpVariable(f"x{i}", lowBound=bounds[i]) for i in range(len(objective_coeffs))]

    # Define a função objetivo
    problem += pulp.lpSum([objective_coeffs[i] * variables[i] for i in range(len(objective_coeffs))])

    # Adiciona as restrições
    for i, (coeffs, limit) in enumerate(constraints):
        problem += (pulp.lpSum([coeffs[j] * variables[j] for j in range(len(coeffs))]) <= limit, f"Restrição {i + 1}")

    # Resolve o problema
    problem.solve(pulp.PULP_CBC_CMD(msg=True))

    # Obtém os resultados
    solution = {f"x{i}": pulp.value(variables[i]) for i in range(len(variables))}
    optimal_value = pulp.value(problem.objective)
    shadow_prices = {name: constraint.pi for name, constraint in problem.constraints.items()}
    slacks = {name: constraint.slack for name, constraint in problem.constraints.items()}

    return solution, optimal_value, shadow_prices, slacks

# Exemplo de uso da função
objective_coeffs = [80, 70, 100, 16]
constraints = [
    ([1, 1, 1, 4], 250),
    ([0, 1, 1, 2], 600),
    ([3, 2, 4, 0], 500)
]
bounds = [0, 0, 0, 0]

solution, optimal_value, shadow_prices, slacks = simplex_optimization(objective_coeffs, constraints, bounds)

print("Solução ótima:")
for var, value in solution.items():
    print(f"{var} = {value}")
print("Z* =", optimal_value)

print("\nPreços sombra (multiplicadores de Lagrange) para cada restrição:")
for name, price in shadow_prices.items():
    print(f"{name}: {price}")

print("\nSobras de cada restrição:")
for name, slack in slacks.items():
    print(f"{name}: {slack} >= 0")

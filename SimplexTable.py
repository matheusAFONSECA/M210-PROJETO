import pulp
import pandas as pd

def simplex_optimization(df_objective, df_constraints, df_bounds):
    """    
    Parâmetros:
    - df_objective: DataFrame com os coeficientes da função objetivo.
    - df_constraints: DataFrame com os coeficientes das restrições e limites superiores.
    - df_bounds: DataFrame com os limites inferiores das variáveis de decisão.
    
    Retorna:
    - solução ótima para as variáveis de decisão.
    - valor ótimo da função objetivo.
    - preços sombra para cada restrição.
    - sobras de cada restrição.
    """
    # Cria um problema de maximização
    problem = pulp.LpProblem("Simplex Optimization", pulp.LpMaximize)

    # Extrai os coeficientes da função objetivo e define as variáveis de decisão
    objective_coeffs = df_objective.iloc[0].values
    bounds = df_bounds.iloc[0].values
    variables = [pulp.LpVariable(f"x{i}", lowBound=bounds[i]) for i in range(len(objective_coeffs))]

    # Define a função objetivo
    problem += pulp.lpSum([objective_coeffs[i] * variables[i] for i in range(len(objective_coeffs))])

    # Adiciona as restrições
    for i in range(len(df_constraints)):
        coeffs = df_constraints.iloc[i, :-1].values
        limit = df_constraints.iloc[i, -1]
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
data_objective = {"e": [80], "m": [70], "a": [100], "p": [16]}
data_constraints = {
    "e": [1, 0, 3],
    "m": [1, 1, 2],
    "a": [1, 1, 4],
    "p": [4, 2, 0],
    "limit": [250, 600, 500]
}
data_bounds = {"e": [0], "m": [0], "a": [0], "p": [0]}

df_objective = pd.DataFrame(data_objective)
df_constraints = pd.DataFrame(data_constraints)
df_bounds = pd.DataFrame(data_bounds)

solution, optimal_value, shadow_prices, slacks = simplex_optimization(df_objective, df_constraints, df_bounds)

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

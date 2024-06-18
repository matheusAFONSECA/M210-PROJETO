import pandas as pd
import pulp

def simplex_optimization(df_objective, df_constraints, df_bounds, optimization_type='maximize'):
    """
    Realiza a otimização usando o método simplex.
    
    Parâmetros:
    - df_objective: DataFrame com os coeficientes da função objetivo.
    - df_constraints: DataFrame com os coeficientes das restrições e limites superiores.
    - df_bounds: DataFrame com os limites inferiores das variáveis de decisão.
    - optimization_type: Tipo de otimização ('maximize' ou 'minimize').
    
    Retorna:
    - solução ótima para as variáveis de decisão.
    - valor ótimo da função objetivo.
    - preços sombra para cada restrição.
    - sobras de cada restrição.
    """
    # Define o tipo de problema (maximização ou minimização)
    if optimization_type == 'maximize':
        problem = pulp.LpProblem("Simplex Optimization", pulp.LpMaximize)
    elif optimization_type == 'minimize':
        problem = pulp.LpProblem("Simplex Optimization", pulp.LpMinimize)
    else:
        raise ValueError("optimization_type deve ser 'maximize' ou 'minimize'")
    
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

# Define os dados do problema
data_objective = {"x1": [2], "x2": [3]}
data_constraints = {
    "x1": [-1, -3],
    "x2": [-2, -1],
    "limit": [-4, -3]
}
data_bounds = {"x1": [0], "x2": [0]}

df_objective = pd.DataFrame(data_objective)
df_constraints = pd.DataFrame(data_constraints)
df_bounds = pd.DataFrame(data_bounds)

solution, optimal_value, shadow_prices, slacks = simplex_optimization(df_objective, df_constraints, df_bounds, optimization_type='minimize')

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

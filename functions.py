import pulp
from time import sleep
import streamlit as st
import pandas as pd
from scipy.optimize import linprog

# Função que cria a tabela simplex dada a quantidade de variáveis e restrições
def create_simplex_table(num_vars, num_constraints):
    st.subheader("Tabela Simplex")
    
    # Criação de uma tabela vazia
    simplex_table = pd.DataFrame(columns=[f"x{i+1}" for i in range(num_vars)] + [f"s{i+1}" for i in range (num_constraints)] + ["LD"],
                                 index=[f"Restrição {j+1}" for j in range(num_constraints)] + ["Função Objetivo"])
    
    # Preenchimento da tabela com zeros (ou valores iniciais)
    simplex_table[:] = 0

    return simplex_table

# Função que resolve o tableau simplex
def solve_tableau(simplex_table):
    optimized_tableau = linprog(c=simplex_table.loc["Função Objetivo", :].values[:-1],
                                A_ub=simplex_table.loc[:"Restrição 1", :].values[:, :-1],
                                b_ub=simplex_table.loc[:"LD", :].values[:, -1],
                                method="simplex")
    
    st.write("Solução do problema:")
    st.write(optimized_tableau)


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
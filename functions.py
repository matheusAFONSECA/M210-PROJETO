# Bibliotecas
import pulp
import streamlit as st
import pandas as pd

# Função que cria a tabela simplex dada a quantidade de variáveis, restrições e tipo de otimização
def create_simplex_table(num_vars, num_constraints, optimization_type):
    st.subheader("Tabela Simplex")
    
    # Criação de uma tabela vazia
    simplex_table = pd.DataFrame(columns=[f"x{i+1}" for i in range(num_vars)] + ["cond"] + ["LD"],
                                 index=["Função Objetivo"] + [f"Restrição {j+1}" for j in range(num_constraints)])
    
    # Preenche os valores padrão da tabela
    if optimization_type == "Maximizar":
        simplex_table["cond"] = ["-"] + ["<="] * num_constraints
    elif optimization_type == "Minimizar":
        simplex_table["cond"] = ["-"] + [">="] * num_constraints
    simplex_table["LD"] = 0
    simplex_table.iloc[:, :-2] = 0  # Preenche as variáveis de decisão com 0

    return simplex_table

# Função que resolve o problema de programação linear com o método Simplex
def simplex_optimization(simplex_tableau, optimization_type):
    # Remover a coluna 'cond' da tabela
    df_optimization = simplex_tableau.drop(columns=["cond"])

    # Extrair a função objetivo
    df_objective = df_optimization.loc["Função Objetivo", df_optimization.columns[:-1]]
    
    # Extrair as restrições e o lado direito (LD)
    df_constraints = df_optimization.loc[df_optimization.index != "Função Objetivo", df_optimization.columns[:-1]]
    df_rhs = df_optimization.loc[df_optimization.index != "Função Objetivo", "LD"]
    
    # Define os limites das variáveis de decisão (não-negatividade)
    variable_bounds = {col: (0, None) for col in df_objective.index}
    
    # Define o tipo de problema (maximização ou minimização)
    if optimization_type == 'Maximizar':
        problem = pulp.LpProblem("Simplex Optimization", pulp.LpMaximize)
    elif optimization_type == 'Minimizar':
        problem = pulp.LpProblem("Simplex Optimization", pulp.LpMinimize)
    else:
        raise ValueError("optimization_type deve ser 'maximize' ou 'minimize'")
    
    # Define as variáveis de decisão
    variables = {name: pulp.LpVariable(name, lowBound=variable_bounds[name][0], upBound=variable_bounds[name][1])
                 for name in df_objective.index}
    
    # Define a função objetivo
    problem += pulp.lpSum(df_objective[name] * variables[name] for name in df_objective.index), "Objective"
    
    # Define as restrições
    for i in range(len(df_constraints)):
        constraint_name = df_constraints.index[i]
        coeffs = df_constraints.iloc[i]
        limit = df_rhs.iloc[i]
        problem += (pulp.lpSum(coeffs[j] * variables[j] for j in df_constraints.columns) <= limit, constraint_name)
    
    # Resolve o problema
    problem.solve(pulp.PULP_CBC_CMD(msg=True))
    
    # Extrai a solução, valor ótimo, preços sombra e folgas
    solution = {var: pulp.value(variables[var]) for var in variables}
    if optimization_type == 'Maximizar':
        optimal_value = pulp.value(problem.objective)
    else:    
        optimal_value = -pulp.value(problem.objective)
    shadow_prices = {name: constraint.pi for name, constraint in problem.constraints.items()}
    slacks = {name: constraint.slack for name, constraint in problem.constraints.items()}
    
    return solution, optimal_value, shadow_prices, slacks
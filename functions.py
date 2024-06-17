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

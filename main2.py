import streamlit as st
import pandas as pd
from functions import *
from scipy.optimize import linprog

cols = 2
rows = 2
# Função principal
def main():
    st.title("SolveX - Solucionador de Programação Linear com Método Simplex")

    # Entrada do número de variáveis (colunas) e restrições (linhas)
    num_vars = st.number_input("Número de Variáveis (Colunas)", min_value=1, max_value=4, step=1)
    num_constraints = st.number_input("Número de Restrições (Linhas)", min_value=1, max_value=4, step=1)
    table_created = False

    # Criação da tabela Simplex com base nas entradas do usuário
    if st.button("Criar Tabela Simplex"):

        st.session_state['initial_simplex'] = create_simplex_table(num_vars, num_constraints)
    
    # Verifica se a tabela foi criada e exibe a data editor
    if 'initial_simplex' in st.session_state:
        st.write("Edite a tabela abaixo:")
        st.session_state['updated_simplex'] = st.data_editor(st.session_state['initial_simplex'])

        table_created = True

    # Solução do problema de programação linear
    if table_created:
        if st.button("Resolver Tableau"):
            solve_tableau(st.session_state['updated_simplex'])

# Executar a aplicação Streamlit
if __name__ == '__main__':
    main()

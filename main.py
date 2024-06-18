import streamlit as st
import pandas as pd
from functions import create_simplex_table, simplex_optimization
from scipy.optimize import linprog

# Função principal
def main():
    st.image("logo.jpg", width=400)
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
            solution, optimal_value, shadow_prices, slacks = simplex_optimization(st.session_state['updated_simplex'])
            
            st.subheader("Solução do Problema")
            
            st.subheader("Valor Ótimo da Função Objetivo (Z):")
            st.write(optimal_value)
            
            st.subheader("Valores Ótimos das Variáveis de Decisão")
            solution_df = pd.DataFrame(list(solution.items()), columns=['Variável', 'Valor'])
            st.table(solution_df)

            st.subheader("Preços Sombra das Restrições")
            shadow_prices_df = pd.DataFrame(list(shadow_prices.items()), columns=['Restrição', 'Preço Sombra'])
            st.table(shadow_prices_df)


# Executar a aplicação Streamlit
if __name__ == '__main__':
    main()

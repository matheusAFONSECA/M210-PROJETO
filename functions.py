from time import sleep
import streamlit as st
import pandas as pd

# Função que cria a tabela simplex dada a quantidade de variáveis e restrições
def create_simplex_table(num_vars, num_constraints):
    st.subheader("Tabela Simplex")
    
    # Criação de uma tabela vazia
    simplex_table = pd.DataFrame(columns=[f"x{i+1}" for i in range(num_vars)] + ["LD"],
                                 index=[f"Restrição {j+1}" for j in range(num_constraints)] + ["Função Objetivo"])
    
    # Preenchimento da tabela com zeros (ou valores iniciais)
    simplex_table[:] = 0

    # Create a dynamic data editor
    edit_df = st.data_editor(simplex_table, height=400)

# Check if there are changes in the editor
    if edit_df is not None:
    # Get the updated 'x' column from the editor
        x_values = edit_df['x']

    # Calculate the corresponding 'y' values
        y_values = x_values ** 2

    # Update the 'y' column in the original DataFrame
        simplex_table['y'] = y_values

    if st.button("Resolver Simplex"):
        st.write("Simplex Resolvido")
        st.write(simplex_table)
        st.write("Solução: ")
        st.write("x1 = 1, x2 = 2, x3 = 3, LD = 4")
        st.write("Valor da Função Objetivo: 10")
        st.write("Solução Ótima Encontrada!")
        sleep(5)
   
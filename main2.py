import streamlit as st
import pandas as pd
from functions import *

cols = 2
rows = 2
# Função principal
def main():
    st.title("SolveX - Solucionador de Programação Linear com Método Simplex")

    # Entrada do número de variáveis (colunas) e restrições (linhas)
    num_vars = st.number_input("Número de Variáveis (Colunas)", min_value=1, max_value=4, step=1)
    num_constraints = st.number_input("Número de Restrições (Linhas)", min_value=1, max_value=4, step=1)

    # Criação da tabela Simplex com base nas entradas do usuário
    if st.button("Criar Tabela Simplex"):
        create_simplex_table(num_vars, num_constraints)


# Executar a aplicação Streamlit
if __name__ == '__main__':
    main()

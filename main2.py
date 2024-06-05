import streamlit as st
import pandas as pd


# Função principal
def main():
    st.title("Simulação de Entrada de uma Tabela Simplex")

    # Entrada do número de variáveis (colunas) e restrições (linhas)
    num_vars = st.number_input("Número de Variáveis (Colunas)", min_value=1, value=3, step=1)
    num_constraints = st.number_input("Número de Restrições (Linhas)", min_value=1, value=3, step=1)

    # Criação da tabela Simplex com base nas entradas do usuário
    if st.button("Criar Tabela Simplex"):
        create_simplex_table(num_vars, num_constraints)


# Função que cria a tabela simplex dada a quantidade de variáveis e restrições
def create_simplex_table(num_vars, num_constraints):
    st.subheader("Tabela Simplex")
    
    # Criação de uma tabela vazia
    simplex_table = pd.DataFrame(columns=[f"Var_{i+1}" for i in range(num_vars)] + ["RHS"],
                                 index=[f"Restrição_{j+1}" for j in range(num_constraints)] + ["Função Objetivo"])
    
    # Entrada dos coeficientes para a tabela Simplex
    for row in simplex_table.index:
        for col in simplex_table.columns:
            simplex_table.at[row, col] = st.text_input(f"{row} - {col}", value=0, key=f"{row}_{col}")

    # Exibição da tabela Simplex preenchida
    st.write("Tabela Simplex Preenchida:")
    st.write(simplex_table)

# Executar a aplicação Streamlit
if __name__ == '__main__':
    main()


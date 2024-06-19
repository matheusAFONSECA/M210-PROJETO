# Simplex Calculator
Este projeto é uma calculadora Simplex desenvolvida em Python, utilizando o framework Streamlit para a interface gráfica e a biblioteca Pulp para resolver problemas de programação linear.

# Sumário
- [Visão geral](#visão-geral)
- [Instalação](#instalação)
   - [Criar ambiente virtual](#criar-ambiente-virtual)
   - [Instalar dependências](#instalar-dependências)
- [Execução do projeto](#execução-do-projeto)
- [Tecnologias utilizadas](#tecnologias-utilizadas)

# Visão geral
A Calculadora Simplex é um aplicativo que permite resolver problemas de programação linear utilizando o método Simplex. A interface gráfica foi construída com Streamlit, proporcionando uma experiência de usuário intuitiva e fácil de usar. A resolução dos problemas é feita com a ajuda da biblioteca Pulp, que facilita a modelagem e a solução de problemas de otimização linear.

# Requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

# Instalação
## Criar ambiente virtual
1. Navegue até o diretório do projeto.
2. Crie um ambiente virtual com o comando:
```
$ python -m venv venv
```
3. Ative o ambiente virtual:
   - No Windows:
     ```
      $ venv\Scripts\activate
     ```
   - No macOS e Linux:
     ```
      $ source venv/bin/activate
     ```
## Instalar Dependências
Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt` com o comando:
```
$ pip install -r requirements.txt
```

# Execução do projeto
Para iniciar a aplicação, execute o seguinte comando na raiz do projeto:
```
$ streamlit run main.py
```
Este comando iniciará o servidor Streamlit e abrirá a aplicação no seu navegador padrão.

# Tecnologias Utilizadas
- __Python__: Linguagem de programação principal utilizada para desenvolver o projeto.
- **Streamlit**: Framework usado para construir a interface gráfica da calculadora.
- **Pulp**: Biblioteca utilizada para modelagem e solução de problemas de otimização linear.

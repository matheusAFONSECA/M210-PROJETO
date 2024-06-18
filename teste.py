from scipy.optimize import linprog

# Coeficientes da função objetivo
c = [-80, -70, -100, -16]  # Os valores são negativos porque linprog faz minimização por padrão

# Matriz A das restrições de desigualdade Ax <= b
A = [[1, 1, 1, 4],
     [0, 1, 1, 2],
     [3, 2, 4, 0]]

# Vetor b das restrições de desigualdade Ax <= b
b = [250, 600, 500]

# Limites para cada variável
x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)

# Resolvendo o problema de otimização
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds, x3_bounds], method='simplex', options={"disp": True})

print(result.success)

# Condições de viabilidade
if result.success:
    print(f"Solução ótima encontrada: {result.fun * -1}")  # Multiplica por -1 para corrigir para problema de maximização
    print("Valores das variáveis:")
    for i, var in enumerate(result.x):
        print(f"Variável {i+1}: {var}")
else:
    print("A otimização não encontrou uma solução ótima.")
    print(f"Motivo: {result.message}")

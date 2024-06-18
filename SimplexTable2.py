import numpy as np
from scipy.optimize import linprog

# Coeficientes da função objetivo (negativos para maximização)
c = [-80, -70, -100, -16]

# Coeficientes das restrições (Ax <= b)
A = [
    [1, 1, 1, 4],
    [0, 1, 1, 2],
    [3, 2, 4, 0]
]

# Termos independentes das restrições
b = [250, 600, 500]

# Solve the linear programming problem
res = linprog(c, A_ub=A, b_ub=b)

# Print the optimal simplex table
print("Optimal Simplex Table:")
print("x1\tx2\tx3\tb")
for i in range(len(A)):
    print(f"{res.x[i]}\t", end="")
print(f"{res.fun}")

# Display the simplex table
print("\nSimplex Table:")
print("x1\t x2\t x3\t b")
for i in range(len(A)):
    for j in range(len(A[i])):
        print(f"{A[i][j]}\t", end="")
    print(f"{b[i]}")

print(res.fun)
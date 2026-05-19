import random

def determinante_matriz_3x3(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    return (
        a * (e * i - f * h)
        - b * (d * i - f * g)
        + c * (d * h - e * g)
    )

matriz = [[random.randint(0, 100) for _ in range(3)] for _ in range(3)]

print("Matriz 3x3 de números aleatórios:")
for linha in matriz:
    print(linha)

soma_diagonal_principal = sum(matriz[i][i] for i in range(3))
soma_diagonal_secundaria = sum(matriz[i][2 - i] for i in range(3))
determinante = determinante_matriz_3x3(matriz)
print(f"Soma da diagonal principal: {soma_diagonal_principal}")
print(f"Soma da diagonal secundária: {soma_diagonal_secundaria}")
print(f"Determinante da matriz: {determinante}")


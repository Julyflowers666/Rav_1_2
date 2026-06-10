matriz = [[10, 32, 45],
        [23, 54, 67],
        [78, 89, 90]]

valor_maior = matriz[0][0]
for i in range(3):
    for j in range(3):
        if matriz[i][j] > valor_maior:
            valor_maior = matriz[i][j]
print(f"O maior valor da matriz é: {valor_maior}")
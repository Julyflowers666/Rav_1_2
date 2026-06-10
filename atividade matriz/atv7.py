matriz = [[3, 6, 9],
        [12, 15, 18],
        [21, 24, 27]]

diagonal_principal = []
for i in range(3): 
    diagonal_principal.append(matriz[i][i])

soma = 0

for i in range(3):
    soma += diagonal_principal[i]
print(f"A soma dos elementos da diagonal principal é: {soma}")
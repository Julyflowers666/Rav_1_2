matriz = [[3, 6, 9],
        [12, 15, 18],
        [21, 24, 27]]
diagonal_principal = []

for i in range(3): 
    diagonal_principal.append(matriz[i][i])
print(f"Os elementos da diagonal principal são: {diagonal_principal}")
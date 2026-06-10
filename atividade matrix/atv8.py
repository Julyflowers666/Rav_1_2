matriz = [[2, 4, 6, 8],
        [10, 12, 14, 16],
        [18, 20, 22, 24],
        [26, 28, 30, 32]]

num_pares = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            num_pares += 1

print(f"O número de números pares na matriz é: {num_pares}")
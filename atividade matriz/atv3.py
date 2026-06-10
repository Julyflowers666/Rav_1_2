matriz = []

for linha in range (3):
    nova = []
    for colunas in range(3):
        valor = float(input("digite valor: "))
        nova.append(valor)
    matriz.append(nova)

print(matriz)
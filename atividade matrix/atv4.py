matriz = []

for linha in range (6):
    nova = []
    valor = float(input("digite valor: "))
    nova.append(valor)
    matriz.append(nova)

for i in range (len(matriz) -1, -1, -1):
    print (matriz[i])
notas = []

for i in range(3):
    linha = []
    for j in range(4):
        valor = float(input(f"Digite a nota do aluno {i+1} {j+1}: "))
        linha.append(valor)
    notas.append(linha)
    
for i in range(3):
    soma = 0

    for j in range(4):
        soma = soma + notas[i][j]

    media = soma / 4
    print(notas[i])
    print(f"Média da linha {i}: {media}")
    
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
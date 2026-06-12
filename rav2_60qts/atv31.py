def filtrar_pares(lista):
    pares = []

    for num in lista:
        if num % 2 == 0:
            pares.append(num)

    return pares

print(filtrar_pares([1, 2, 3, 4, 5, 6]))
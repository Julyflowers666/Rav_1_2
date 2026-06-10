def eh_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

print(eh_palindromo("A base do teto desaba"))
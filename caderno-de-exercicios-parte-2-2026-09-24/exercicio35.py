frase = input("Digite uma frase: ")

palavras = frase.split()
total_palavras = len(palavras)

total_letras_a = 0
for letra in frase:
    if letra == "a" or letra == "A":
        total_letras_a += 1

print(f"Quantidade de palavras: {total_palavras}")
print(f"Quantidade de letras 'A': {total_letras_a}")

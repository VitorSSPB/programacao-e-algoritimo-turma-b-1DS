vetor = []

for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    vetor.append(numero)

print("Números pares:")
for numero in vetor:
    if numero % 2 == 0:
        print(numero)

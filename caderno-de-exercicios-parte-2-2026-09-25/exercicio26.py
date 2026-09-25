vetor = []

for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    vetor.append(numero)

for indice, valor in enumerate(vetor):
    print(f"Posição {indice}: {valor}")

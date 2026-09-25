vetor = []

for i in range(5):
    valor = int(input(f"Digite o valor {i + 1}: "))
    vetor.append(valor)

print("Ordem digitada:")
for i in range(len(vetor)):
    print(vetor[i])

print("Ordem inversa:")
for i in range(len(vetor) - 1, -1, -1):
    print(vetor[i])

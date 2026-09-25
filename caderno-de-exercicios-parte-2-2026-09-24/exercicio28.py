principal = []

for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    principal.append(numero)

pares = []
impares = []

for numero in principal:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista principal:", principal)
print("Lista de pares:", pares)
print("Lista de ímpares:", impares)

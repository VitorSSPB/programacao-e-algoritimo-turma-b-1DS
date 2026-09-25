lista = []

for i in range(8):
    numero = int(input(f"Digite o número {i + 1}: "))
    lista.append(numero)

busca = int(input("Digite o número de busca: "))

encontrado = False
for indice, valor in enumerate(lista):
    if valor == busca:
        print(f"Número encontrado na posição {indice}")
        encontrado = True
        break

if not encontrado:
    print("Número não encontrado na lista")

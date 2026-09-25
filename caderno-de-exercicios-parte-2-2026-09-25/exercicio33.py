saque = int(input("Digite o valor do saque: "))

cedulas = [100, 50, 20, 10, 5, 2, 1]

restante = saque

for cedula in cedulas:
    quantidade = restante // cedula
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R${cedula}")
        restante = restante % cedula

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = int(input("Escolha a operação: "))
if operacao == 1:
    print(f"Resultado: {n1 + n2}")
elif operacao == 2:
    print(f"Resultado: {n1 - n2}")
elif operacao == 3:
    print(f"Resultado: {n1 * n2}")
elif operacao == 4:
    if n2 == 0:
        print("Não é possível dividir por zero")
    else:
        print(f"Resultado: {n1 / n2}")
else:
    print("Operação inválida")

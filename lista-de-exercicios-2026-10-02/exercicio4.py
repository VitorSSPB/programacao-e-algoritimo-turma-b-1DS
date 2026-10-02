# Programa que lê dois números e exibe qual deles é o maior, ou informa se são iguais.

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
if a > b:
    print(f"O maior número é {a}")
elif b > a:
    print(f"O maior número é {b}")
else:
    print("Os números são iguais")
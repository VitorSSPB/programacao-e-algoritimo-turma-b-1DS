numero = int(input("Digite um número: "))
primo = numero > 1
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break
if primo:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")

a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("EQUILÁTERO")
    elif a == b or a == c or b == c:
        print("ISÓSCELES")
    else:
        print("ESCALENO")
else:
    print("Esses segmentos não formam um triângulo")

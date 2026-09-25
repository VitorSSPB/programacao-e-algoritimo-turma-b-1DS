poltronas = [False] * 10

while True:
    numero = int(input("Digite o número da poltrona (0 a 9, negativo para encerrar): "))
    if numero < 0:
        break
    if poltronas[numero]:
        print("Ocupada")
    else:
        poltronas[numero] = True
        print("Reservada")

    print("Mapa de assentos:")
    for i in range(10):
        status = "Ocupada" if poltronas[i] else "Livre"
        print(f"Poltrona {i}: {status}")

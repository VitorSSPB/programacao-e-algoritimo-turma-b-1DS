import random

segredo = random.randint(1, 10)
tentativas = 0
palpite = 0
print("Estou pensando em um número entre 1 e 10.")
while palpite != segredo:
    palpite = int(input("Qual é o seu palpite? "))
    tentativas += 1
    if palpite < segredo:
        print("Maior")
    elif palpite > segredo:
        print("Menor")
print(f"Acertou! Foram {tentativas} tentativa(s).")

import random

campo = [0] * 10

minas = random.sample(range(10), 3)
for posicao in minas:
    campo[posicao] = 1

perdeu = False

for passo in range(5):
    indice = int(input(f"Passo {passo + 1} - Escolha uma posição (0 a 9): "))
    if campo[indice] == 1:
        print("Você pisou em uma mina! Fim de jogo.")
        perdeu = True
        break
    else:
        print("Posição segura")

if not perdeu:
    print("Você sobreviveu aos 5 passos! Você ganhou!")

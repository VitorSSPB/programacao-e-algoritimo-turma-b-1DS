candidatos = {1: "João", 2: "Maria", 3: "José"}
contadores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

while True:
    voto = int(input("Digite o voto (1-João, 2-Maria, 3-José, 4-Nulo, 5-Branco, 0-Encerrar): "))
    if voto == 0:
        break
    if voto in contadores:
        contadores[voto] += 1

print("Resultado final:")
print(f"João: {contadores[1]}")
print(f"Maria: {contadores[2]}")
print(f"José: {contadores[3]}")
print(f"Nulos: {contadores[4]}")
print(f"Brancos: {contadores[5]}")

votos_candidatos = {k: contadores[k] for k in (1, 2, 3)}
vencedor = max(votos_candidatos, key=votos_candidatos.get)
print(f"Vencedor: {candidatos[vencedor]}")

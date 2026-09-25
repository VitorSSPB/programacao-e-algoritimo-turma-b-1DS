nomes = []
notas = []

for i in range(3):
    nome = input(f"Nome do aluno {i + 1}: ")
    nota = float(input(f"Nota do aluno {i + 1}: "))
    nomes.append(nome)
    notas.append(nota)

for i in range(3):
    situacao = "Aprovado" if notas[i] >= 7 else "Reprovado"
    print(f"{nomes[i]} - Nota: {notas[i]} - {situacao}")

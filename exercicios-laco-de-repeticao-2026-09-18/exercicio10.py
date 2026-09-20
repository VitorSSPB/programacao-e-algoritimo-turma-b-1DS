quantidade = int(input("Quantos alunos existem? "))
notas = []
for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)
media = sum(notas) / len(notas)
print(f"Média da turma: {media:.2f}")

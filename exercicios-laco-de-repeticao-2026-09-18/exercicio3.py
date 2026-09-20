while True:
    nota = float(input("Digite uma nota de 0 a 10: "))
    if 0 <= nota <= 10:
        break
    print("Nota inválida! Tente novamente.")
print(f"Nota registrada: {nota}")

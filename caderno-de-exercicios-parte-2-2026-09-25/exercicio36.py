nomes = []
idades = []

while True:
    print("1 - Cadastrar")
    print("2 - Listar maiores de 18 anos")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        nomes.append(nome)
        idades.append(idade)
    elif opcao == 2:
        for i in range(len(nomes)):
            if idades[i] >= 18:
                print(f"{nomes[i]} - {idades[i]} anos")
    elif opcao == 3:
        break
    else:
        print("Opção inválida")

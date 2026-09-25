produtos = []
quantidades = []

while True:
    print("1 - Adicionar Produto")
    print("2 - Dar Baixa")
    print("3 - Ver Estoque")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome do produto: ")
        qtde = int(input("Quantidade: "))
        produtos.append(nome)
        quantidades.append(qtde)
    elif opcao == 2:
        nome = input("Nome do produto: ")
        if nome in produtos:
            indice = produtos.index(nome)
            qtde = int(input("Quantidade a dar baixa: "))
            if qtde <= quantidades[indice]:
                quantidades[indice] -= qtde
                print("Baixa realizada com sucesso")
            else:
                print("Estoque insuficiente")
        else:
            print("Produto não encontrado")
    elif opcao == 3:
        for i in range(len(produtos)):
            print(f"{produtos[i]} - {quantidades[i]} unidades")
    elif opcao == 4:
        break
    else:
        print("Opção inválida")

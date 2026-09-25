nome = ""
conta = ""
saldo = 0
conta_criada = False

while True:
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato/Ver Saldo")
    print("5 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome: ")
        conta = input("Número da conta: ")
        saldo = 0
        conta_criada = True
        print("Conta criada com sucesso")
    elif opcao == 2:
        if conta_criada:
            valor = float(input("Valor do depósito: "))
            saldo += valor
            print("Depósito realizado com sucesso")
        else:
            print("Nenhuma conta criada")
    elif opcao == 3:
        if conta_criada:
            valor = float(input("Valor do saque: "))
            if valor <= saldo:
                saldo -= valor
                print("Saque realizado com sucesso")
            else:
                print("Saldo insuficiente")
        else:
            print("Nenhuma conta criada")
    elif opcao == 4:
        if conta_criada:
            print(f"Nome: {nome}")
            print(f"Conta: {conta}")
            print(f"Saldo: R${saldo:.2f}")
        else:
            print("Nenhuma conta criada")
    elif opcao == 5:
        break
    else:
        print("Opção inválida")

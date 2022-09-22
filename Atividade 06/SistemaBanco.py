import os


def clear():
    os.system('clear')


def criar_conta(numeroConta, titularConta, saldoConta=0):
    nova_conta = {
        "numeroConta": numeroConta,
        "titularConta": titularConta,
        "saldoConta": saldoConta
    }
    print("Conta criado com sucesso!")
    return nova_conta


def busca_conta(numeroConta):
    for i in contas:
        if i["numeroConta"] == numeroConta:
            print("Conta encontrada com sucesso!")
            return i
    return None


def remover_conta(conta):
    contas.remove(conta)
    print("Conta excluida com sucesso!")


def transferir_saldoConta(contaEmUso, contaAlvo, valor):
    if valor <= contaEmUso["saldoConta"] and valor > 0:
        for i in contas:
            if i == contaAlvo:
                contaAlvo["saldoConta"] += valor
            if i == contaEmUso:
                contaEmUso["saldoConta"] -= valor
            print("Transferencia Completa")
    else :
        print("Voce não tem saldo suficiente na conta")




contas = []


def menu():
    sair = 0

    while sair != 3:
        print("-----Menu-----")
        print("1 - Cadastrar nova conta")
        print("2 - Encontrar uma conta")
        print("3 - Sair")
        print("--------------")
        opcao = int(input("Opcao: "))

        clear()

        if opcao == 1:

            numeroConta = int(input("Número da conta: "))
            titularConta = input("Nome do titularConta: ")
            saldoConta = float(input("saldoConta: "))

            clear()
            contas.append(criar_conta(
                numeroConta, titularConta, saldoConta))

        elif opcao == 2:

            numeroConta = int(input("Digite o numeroConta da conta: "))
            contaEmUso = busca_conta(numeroConta)

            if contaEmUso:
                menuControle(contaEmUso)
            else:
                print("Conta inexistente!")

        elif opcao == 3:

            sair = 3

        else:

            print("Opcao inválida")


def menuControle(contaEmUso):
    sair = 0

    while sair != 5:
        print("-----Opções da Conta-----")
        print("1 - Remover conta")
        print("2 - Realizar transferência")
        print("3 - Exibir saldoConta")
        print("4 - Depositar valor")
        print("5 - Voltar")
        print("-------------------------")
        opcao = int(input("Opcao: "))
        clear()

        if opcao == 1:

            remover_conta(contaEmUso)
            menu()
            sair = 5

        elif opcao == 2:

            conta_desejada = int(
                input("Você deseja transferir para qual cont : "))
            contaAlvo = busca_conta(conta_desejada)

            if contaAlvo:

                print("Destinatário encontrado !")
                valor = float(input("Deseja transferir quantos R$ "))

                if contaAlvo == contaEmUso:
                    print(
                        "Você está tentando fazer uma transição pra si mesmo")
                else:
                    transferir_saldoConta(contaEmUso, contaAlvo, valor)

            else:
                print("Conta inválida")

        elif opcao == 3:

            print("Seu saldo é : ", contaEmUso['saldoConta'])

        elif opcao == 4:
            contaEmUso['saldoConta'] = contaEmUso['saldoConta'] + \
                int(input("Digite o valor do deposito : "))
            print("4")

        elif opcao == 5:

            sair = 5
            clear()
            menu()

        else:
            print("Opção inválida")


menu()

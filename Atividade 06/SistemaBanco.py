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
    for i in lista_contas:
        if i["numeroConta"] == numeroConta:
            print("Conta encontrada com sucesso!")
            return i
    return None


def remover_conta(conta):
    lista_contas.remove(conta)
    print("Conta excluida com sucesso!")


def transferir_saldoConta(contaEmUso, conta_recebedora, valor):
    if contaEmUso["saldoConta"] <= valor:
        conta_recebedora["saldoConta"] += valor
        contaEmUso["saldoConta"] -= valor
    else:
        print(f"Você não possui esse valor {valor}")

lista_contas = []

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
            lista_contas.append(criar_conta(
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
                input("Você deseja transferir para qualquer número de conta: "))
            conta_recebedora = busca_conta(conta_desejada)

            if conta_recebedora:

                print("Destinatário encontrado !")
                valor = float(input("Deseja transferir quantos R$ "))

                if conta_recebedora == contaEmUso:
                    print(
                        "Você está tentando fazer uma transição pra si mesmo")
                else:
                    transferir_saldoConta(contaEmUso, conta_recebedora, valor)

            else:
                print("Conta inválida")

        elif opcao == 3:

            print(contaEmUso.get())

        elif opcao == 4:

            print("4")

        elif opcao == 5:

            sair = 5
            clear()
            menu()

        else:
            print("Opção inválida")


menu()

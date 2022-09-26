# Prova POO Nailson Onesio de Almeida

# 1. O sistema deverá ter um menu com as seguintes opções do sistema
# 1. Cadastro de Funcionários
# 2. Pesquisar funcionário
# 3. Cadastrar novo telefone
# 4. Editar dados do Funcionário
# 5. Deletar funcionário
# 0.Sair

# 2. Cada funcionário deverá ser um dicionário com os seguintes atributos (chaves): NOME, CPF, CARGO, SALARIO, TELEFONES.Onde a chave telefones deve receber uma lista de telefones. Os funcionários (dicionários) deverao ser armazenados em uma lista de Funcionários

# 3. O sistema deve ter uma função para encontra (pesquisar) um funcionário pelo seu cpf e exibir na tela seus dados
# 4. O sistema deve ter uma função para encontrar um funcionário e adicionar um novo telefone
# 5. O sistema deve ter uma função capaz de encontar um funcionário e editar seus dados
# 6. O sistema deve ter uma função para deletar um funcionário
# 7. Caso nao exista um funcionário o sistema nao devera executar as opções 2, 3, 4 e 5

import os

funcionarios = []


def cadastrar_funcionario(nome_Funcio, cpf_Funcio, cargo_Funcio,
                          salario_Funcio, telefones_Funcio):
    novo_Funcionario = {
        "nome_Funcio": nome_Funcio,
        "cpf_Funcio": cpf_Funcio,
        "cargo_Funcio": cargo_Funcio,
        "salario_Funcio": salario_Funcio
    }

    telefones = [telefones_Funcio]
    novo_Funcionario["telefones_Funcio"] = telefones

    print("Cadastro de Funcionário Completo !\n")
    return novo_Funcionario


def pesquisar_funcionario(cpf):
    for i in funcionarios:
        if i["cpf_Funcio"] == cpf:
            print("Funcionário Encontrado! ")
            return i


def cadastro_telefone():
    cpf = input("Digite o CPF do Funcionário: ")
    funcionario = pesquisar_funcionario(cpf)
    funcionario["telefones_Funcio"].append(input("Digite o novo numero: "))
    print("Numero cadastrado com sucesso! ")


def remover_funcionario(funcionario):
    funcionarios.remove(funcionario)
    print("Funcionario excluido! ")


def modificar_funcionario():
  funcionario = input("Digite o CPF do funcionario a ser editado: ")
  editarFuncio = pesquisar_funcionario(funcionario)

  sair = None
  while sair != 0:
    
    print("\n--------Menu de Edição--------")
    print("1 - Modificar Nome")
    print("2 - Modificar CPF")
    print("3 - Modificar Cargo")
    print("4 - Modificar Salario")
    print("5 - Modificar Telefones")
    print("0 - Sair da Edição")
    print("--------------------\n")

    opcao = int(input("Escolha a opcao de modificação: "))

    if opcao == 1:
      nome=input("Digite o nome para modificar Funcionário: ")
      editarFuncio["nome_Funcio"] = nome
    elif opcao == 2:
      cpf=input("Digite o CPF para modificar Funcionário: ")
      editarFuncio["cpf_Funcio"] = cpf
    elif opcao == 3:
      cargo=input("Digite o para modificar Funcionário: ")
      editarFuncio["cargo_Funcio"] = cargo
    elif opcao == 4:
      salario=input("Digite o Salario para modificar Funcionário: ")
      editarFuncio["salario_Funcio"] = salario
    elif opcao == 5:
      telefones = input("Digite o Telefone para modificar Funcionário: ")
      editarFuncio["telefones_Funcio"] = telefones
    elif opcao == 0:
      sair = 0

  


def clear():
    os.system('clear') or None


def menu():

    sair=None

    while sair != 0:
        print("\n--------Menu--------")
        print("1 - Cadastrar Funcionário")
        print("2 - Pesquisar Funcionários")
        print("3 - Cadastra novo telefone")
        print("4 - Editar Funcionarios")
        print("5 - Deletar Funcionarios")
        print("0 - Sair do Programa")
        print("--------------------\n")

        op=int(input("Escolha a opção: "))

        clear()

        if op == 1:
            nome=input("Digite o nome do novo Funcionário: ")
            cpf=input("Digite o CPF do novo Funcionário: ")
            cargo=input("Digite o Cargo do novo Funcionário: ")
            salario=input("Digite o Salario do novo Funcionário: ")
            telefone=input("Digite o Telefone do novo Funcionário: ")

            clear()

            funcionarios.append(
                cadastrar_funcionario(nome, cpf, cargo, salario, telefone))

        elif op == 2:
            if not funcionarios:
              print("Nao tem funcionarios")
            else:
              cpf=input("Informe o CPF do funcionario a pesquisar: ")
              funcionario=pesquisar_funcionario(cpf)
              if funcionario != None:
                print("Nome :", funcionario["nome_Funcio"], "\n"
                      "CPF: ", funcionario["cpf_Funcio"], "\n"
                      "Cargo: ", funcionario["cargo_Funcio"], "\n"
                      "Salario : ", funcionario["salario_Funcio"], "\n"
                      "Telefone's: ", funcionario["telefones_Funcio"])
              else:
                  print("Funcionario não existe ")

        elif op == 3:
            if not funcionarios:
              print("Nao tem funcionarios")
            else:
              cadastro_telefone()

        elif op == 4:
            if not funcionarios:
              print("Nao tem funcionarios")
            else:
              modificar_funcionario()


        elif op == 5:
            if not funcionarios:
              print("Nao tem funcionarios")
            else:
             funcionario=input("Digite o CPF do funcionario: ")
             desempregado=pesquisar_funcionario(funcionario)
             remover_funcionario(desempregado)

        elif op == 0:
            sair=0
        else:
            print("Opção Invalida ")


menu()

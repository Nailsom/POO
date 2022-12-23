from funcionario import *
from funcao import *
import os

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='nailson123',
                             database='prova03',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def cadastrar_funcao(cod_funcao, nome):
    nova = funcao(cod_funcao, nome)
    print("Função cadastrada.")
    return nova


def cadastrar_funcionario(nome, cpf, funcao, salario, telefone):
    nova = funcionario(nome, cpf, funcao, salario, telefone)
    print("Funcionário cadastrado.")
    return nova


def menu_funcao():
    os.system('cls') or None
    print("======Menu das funções======\n1. Cadastrar função\n2.Pesquisar função\n3.Editar "
          "função\n4.Deletar função\n0.Voltar ao Menu Principal")
    op = int(input("Digite o número da opção: "))
    os.system('cls') or None
    print("=" * 30)
    if op == 1:
        cod_funcao = int(input("Digite um código para função: "))
        nome = input("Digite o nome da função: ")
        cadastrar_funcao(cod_funcao, nome)
        print("Funcao criada com sucesso!")
        menu_funcao()
    elif op == 2:
        codi = int(input("Digite o código da função: "))
        try:
            funcao.pesquisar(codi)
            menu_funcao()
        except:
            print("Funcionario não encontrado")
            menu_funcao()
    elif op == 3:
        codi = int(input("Digite o código da função: "))
        nome = input("Digite o novo nome da função")
        try:
            funcao.alterar(codi, nome)
            print("Função alterada com sucesso!")
            menu_funcao()
        except:
            print("Alteração mal sucedida!")
            menu_funcao()
    elif op == 4:
        codi = int(input("Digite o código da função: "))
        try:
            funcao.apagar(codi)
            print("Função apagada com sucesso!")
            menu_funcao()
        except:
            print("Não foi possível apagar a função pois existem funcionários alocado nela.")
            menu_funcao()
    elif op == 0:
        menu()
    else:
        print("Valor incorreto!")
        menu_funcao()


def menu_funcionario():
    os.system('cls') or None
    print("======Menu dos funcionários======\n1. Cadastrar funcionário\n2.Pesquisar funcionário\n3.Editar "
          "funcionário\n4.Deletar funcionário\n0.Voltar ao Menu Principal")
    op = int(input("Digite o número da opção: "))
    os.system('cls') or None
    if op == 1:
        nome = input("NOME: ")
        cpf = int(input("CPF: "))
        funcao = int(input("FUNÇÃO(código): "))
        salario = float(input("SALÁRIO: "))
        telefone = input("TELEFONE: ")
        try:
            cadastrar_funcionario(nome, cpf, funcao, salario, telefone)
            print("Cadastro bem sucedido!")
            menu_funcionario()
        except:
            print(("Nao foi possivel cadastrar o funcionario, pois a função nao existe!"))
            menu_funcionario()


    elif op == 2:
        cpf = int(input("Digite o cpf do funcionário: "))
        try:
            funcionario.pesquisar(cpf)
            menu_funcionario()
        except:
            print("Funcionario não encontrado!")
            menu_funcionario()
    elif op == 3:
        cod = input("Digite o cpf: ")
        aux = funcionario.pesquisar(cod)
        print('=' * 30, "Digite os novos dados do funcionario: ")
        nome = input("NOME: ")
        cpf = int(input("CPF: "))
        funcao = int(input("FUNÇÃO(código): "))
        salario = float(input("SALÁRIO: "))
        telefone = input("TELEFONE: ")
        try:
            aux.alterar(nome, cpf, funcao, salario, telefone)
            menu_funcionario()
        except:
            print("Edição de funcionario Mal sucedida")
            menu_funcionario()
    elif op == 4:
        codi = input("Digite o cpf do funcionario: ")
        try:
            funcionario.apagar(codi)
            print("Funcionario apagado com sucesso!")
            menu_funcionario()
        except:
            print("Funcionario não encontrado!")
            menu_funcionario()

    elif op == 0:
        menu()
    else:
        print("Valor incorreto!")
        menu_funcionario()


def menu():
    os.system('cls') or None
    print("======Menu======\n1- Manter funções\n2- Manter funcionários\n3- Sair")
    op = int(input("Digite o número da opção: "))
    os.system('cls') or None
    print('=' * 30)
    if op == 1:
        menu_funcao()
    elif op == 2:
        menu_funcionario()
    elif op == 3:
        pass


menu()

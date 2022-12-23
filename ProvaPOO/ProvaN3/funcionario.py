import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',  # Usuário que irá conectar ao banco
                             password='nailson123',  # Senha da conexão
                             database='prova03',  # Nome o banco que será utilizado
                             charset='utf8mb4',  # Conjunto de caracteres a utilizar
                             cursorclass=pymysql.cursors.DictCursor)  # Classe do cursor que será gerado


class funcionario:
    def __init__(self, nome, cpf, funcao, salario, telefone):
        self.nome = nome
        self.cpf = cpf
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
        self.cadrastar()

    def cadrastar(self):
        with connection.cursor() as c:
            sql = "INSERT INTO funcionario (nome, cpf, funcao, salario, telefone) VALUES (%s, %s, (SELECT id " \
                  "FROM funcao WHERE cod = %s), %s, %s)"
            c.execute(sql,
                      (self.nome, self.cpf, self.funcao, self.salario, self.telefone))
            connection.commit()

    @staticmethod
    def pesquisar(cpf):
        with connection.cursor() as c:
            sql = (f"SELECT funcionario.nome, funcao.nome FROM funcionario, funcao "
                   f"WHERE funcionario.funcao = funcao.id AND funcionario.cpf = {cpf}")
            pes = (f"SELECT * FROM funcionario WHERE funcionario.cpf= {cpf} ")
            c.execute(sql)
            res_one = c.fetchone()
            print(res_one)
            return pes
        connection.commit()

    @staticmethod
    def alterar(nome, cpf, funcao, salario, telefone):
        with connection.cursor() as cursor:
            sql = ("UPDATE funcionario SET nome=%s, cpf=%s, funcao=%s,salario=%s,telefone=%s WHERE cpf=%s")
            cursor.execute(sql, (nome, cpf, funcao, salario, telefone))
        connection.commit()

    @staticmethod
    def apagar(cpf):
        with connection.cursor() as cursor:
            sql = (f"DELETE FROM funcionario where cpf={cpf} ")
            cursor.execute(sql)
        connection.commit()

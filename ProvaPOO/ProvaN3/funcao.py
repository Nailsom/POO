import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',  # Usuário que irá conectar ao banco
                             password='nailson123',  # Senha da conexão
                             database='prova03',  # Nome o banco que será utilizado
                             charset='utf8mb4',  # Conjunto de caracteres a utilizar
                             cursorclass=pymysql.cursors.DictCursor)  # Classe do cursor que será gerado


class funcao:
    def __init__(self, cod_funcao, nome):
        self.cod_funcao = cod_funcao
        self.nome = nome
        self.transferir()

    def transferir(self):
        with connection.cursor() as c:
            sql = " INSERT INTO funcao (cod, nome)VALUES (%s,%s)"
            c.execute(sql, (self.cod_funcao, self.nome))
        connection.commit()

    @staticmethod
    def pesquisar(codi):
        with connection.cursor() as c:
            sql = (f"SELECT * FROM funcao WHERE cod={codi}")
            c.execute(sql)
            res_one = c.fetchone()
            print(res_one)
        connection.commit()

    @staticmethod
    def alterar(codi, nome):
        with connection.cursor() as cursor:
            sql = ("UPDATE funcao SET nome=%s WHERE cod=%s")
            cursor.execute(sql, (nome, codi))
        connection.commit()

    @staticmethod
    def apagar(codi):
        with connection.cursor() as cursor:
            sql = (f"DELETE FROM funcao where cod={codi} ")
            cursor.execute(sql)
        connection.commit()

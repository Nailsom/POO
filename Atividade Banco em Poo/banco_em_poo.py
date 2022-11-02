class Pix:

  def __init__(self, pix: str):
    self.chave = pix


class Conta:

  def __init__(self, numero_conta: int, agencia: str, valor: float):
    self.__conta = numero_conta
    self.__agencia = agencia
    self.__valor = valor
    self.chave_pix = []

  @property
  def conta(self):
    return self.__conta

  @conta.setter
  def conta(self, numero_conta):
    self.__conta = numero_conta

  @property
  def valor(self):
    return self.__valor

  @valor.setter
  def valor(self, valor):
    self.__valor = valor

  @property
  def agencia(self):
    return self.__agencia

  @agencia.setter
  def agencia(self, agencia):
    self.__agencia = agencia

  def depositar(self, deposito):
    self.__valor += deposito

  def ver_saldo(self):
    print(f"Seu saldo é {self.__valor}")

  def transferencia(self, valor, Conta):
    self.__valor -= valor
    Conta.__valor += valor

  def adicionar_chave_pix(self, chave: str):
    pix = Pix(chave)
    self.chave_pix.append(pix)

  def mostrar_pix(self):
    for i in self.chave_pix:
      print(i.chave)


class Contatos:

  def __init__(self, nome: str, telefone: str):
    self.__nome = nome
    self.telefone = telefone

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome):
    self.__nome = nome


class Cliente:

  def __init__(self, nome: str):
    self.nome = nome
    self.conta = None
    self.contatos = []

  def criar_conta(self, numero_conta: int, agencia: str, valor: float):
    self.conta = Conta(numero_conta, agencia, valor)

  def adicionar_contatos(self, nome_contato: str, telefone: str):
    contato = Contatos(nome_contato, telefone)
    self.contatos.append(contato)

  def mostrar_contatos(self):
    for i in self.contatos:
      print(i.nome, i.telefone)


cliente1 = Cliente("Onesio")
cliente1.nome = "Nailson"
cliente1.criar_conta(26, "6666", 1800)
print(cliente1.conta.valor)
cliente1.conta.adicionar_chave_pix("88406550")
cliente1.adicionar_contatos("Nathalia", "40028922")
cliente1.conta.valor = 800
print(cliente1.conta.valor)
print(cliente1.nome, cliente1.conta.valor)
cliente1.mostrar_contatos()
cliente1.conta.mostrar_pix()

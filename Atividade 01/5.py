salario = int(input("Digite o salario :\n"))
pres = int(input("Digite o valor da prestação:\n"))

empre = salario*0.2
empre = empre+salario

if (pres>empre):
    print("Emprestimo negado")
else:
    print("Emprestimo concedido")




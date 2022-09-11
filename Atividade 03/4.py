numero = int(input("Digite um numero inteiro entre 100 e 999 : \n"))
if (numero < 100 or numero > 999):
    print("Numero Invalialga2o\n")
    exit()



alga3 = int(numero % 10)

alga2 = int(numero % 100)
alga2 = int(alga2 - alga3)
alga2 = int(alga2 / 10)

alga1 = int(numero % 1000)
alga1 = int((alga1 - alga2) - alga3)
alga1 = int(alga1 / 100)

print(alga1)
print(alga2)
print(alga3)




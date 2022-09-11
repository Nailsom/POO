numero = int(input("Digite um numero Natural par: \n"))
if (numero <= 0):
    print("Numero é negativo")
    exit()
if (numero%2) == 1:
    print("Numero não é par.\n")

for i in range(0, numero+2, 2):
   print(i)
    


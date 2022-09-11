lista = []

med = 0

print('Digite as 4 notas : \n')

for i in range(4):

    lista.append(float(input('Nota ' + str(i+1) + ':\n')))

    med += lista[i]

med = med/4

print(lista)

print("A media é :", med)

lista = []

print('Digite os 10 numeros reais : \n')

for i in range(10):

    lista.append(float(input('Numero ' + str(i+1) + ':\n')))

lista.reverse()

print(lista)

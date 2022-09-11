listaPar = []
listaImpar = []
listaNumeros = []
numero = 0
print('Digite os numeros :\n')
for i in range(20):
    listaNumeros.append((int(input('Numero: ' + str(i+1) + ':\n'))))
    numero = listaNumeros[i]
    print(numero)
    if (numero % 2 == 0):
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
print(listaNumeros)
print(listaPar)
print(listaImpar)

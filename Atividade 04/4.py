lista = []

conso = 0

print('Digite os caracteres : \n')

for i in range(10):
    lista.append((input('caracteres  ' + str(i+1) + ':\n')))
    carac = lista[i]

    if (carac not in ('a', 'e', 'i', 'o', 'u')):
        conso += 1

print(conso)

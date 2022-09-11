def posi_nega(num):
    if (num > 0):
        return 1
    elif (num < 0):
        return -1
    else:
        return 0


numero = int(input("Digite o numero: \n"))

numero = posi_nega(numero)

print(numero)

def maior(num, num2):
    if (num > num2):
        return "O primeiro é maior"
    elif (num == num2):
        return "Numeros iguais"
    else:
        return "O segundo é maior"


numero1 = int(input("Digite o primeiro numero: \n"))
numero2 = int(input("Digite o segundo numero: \n"))

resultado = maior(numero1, numero2)

print(resultado)

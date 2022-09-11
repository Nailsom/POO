
num = int(input("Digite o numero: \n"))
f1 = 0
f2 = 1
f3 = None

if (num < 0) :
    print("Numero Invalido")
else :
    print("0 - 1")
while (f2 <= num) :
    f3 = f2 + f1
    print(" - ", f3)
    f1 = f2
    f2 = f3

print("\n")

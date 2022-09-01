nota1 = int(input("Digite a primeira nota :\n"))
nota2 = int(input("Digite a segunda nota :\n"))

if (nota1>10 or nota1<0):
    print("Notas Invalidas")
    exit()
if (nota2>10 or nota2<0):
    print("Notas Invalidas")
    exit()

print("A media da notas é : ",(nota1+nota2)/2)



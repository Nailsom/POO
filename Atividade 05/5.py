raio = float(input("Digite o valor do raio: \n"))
altura = float(input("Digite o valor da altura: \n"))


def volume_esfera(raio, altura):
    pi = 3.14159265359
    volume = pi*(raio**2)*altura
    return volume


volumefinal = volume_esfera(raio, altura)

print("O volume do cilindro é : ", round(volumefinal, 2), "m³")

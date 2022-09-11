raio = float(input("Digite o valor do raio: \n"))


def volume_esfera(raio):
    pi = 3.14159265359
    volume = (4/3)*pi*(raio**3)
    return volume


volumefinal = volume_esfera(raio)

print("O volume da esfera é : ", round(volumefinal, 2), "m³")

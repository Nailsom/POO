qtd_num = int(input('Entre com a quantidade de números a serem lidos: '))
maior = float('-inf')
cont = {}
for _ in range(qtd_num):
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    c = cont.get(num, 0)
    cont[num] = c + 1

print(f'O maior valor é {maior} e ele ocorre {cont[maior]} vezes')
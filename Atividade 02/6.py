lista = []
i = 0
quant = 10
while i < quant:
   val = int(input("Digite um valor:\n"))
   i = i + 1
   lista.append(val)
else:
   print("Menor valor:", (min(lista)))
   print("Maior valor:", (max(lista)))

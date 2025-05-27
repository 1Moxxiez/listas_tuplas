'''
Crie uma lista com n´umeros de 1 a 100 e filtre os m´ultiplos de 3.
'''
lista = []

for i in range (1, 101):
    lista.append(i)

multiplo_3 = [(num) for num in lista if num % 3 == 0]

print(multiplo_3)

#  tudo numa linha só, sem criar a lista antes:
multiplo_3 = [num for num in range(1, 101) if num % 3 == 0]
print(multiplo_3)

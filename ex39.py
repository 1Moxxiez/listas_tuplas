'''
'''

# Usando .extend():

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Copiando a primeira lista
uniao = list(lista1)
uniao.extend(lista2)

print("União das listas:", uniao)



# Usando for:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

uniao = []
for item in lista1:
    uniao.append(item)
for item in lista2:
    uniao.append(item)

print("União das listas:", uniao)

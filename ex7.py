'''
Use um la¸co while para imprimir os elementos de uma lista um por um
'''

lista = [1, 2, 3, 4, 5, 6]
n = len(lista)

i = 0

while i < n:
    for i in range( len(lista)):
        print (lista [i])
    i += 1
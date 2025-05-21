'''
6. Solicite 5 n´umeros ao usu´ario e armazene em uma lista. Em seguida, imprima o
maior e o menor n´umero.

'''
lista = []

for i in range(1, 6):
    n = int(input('Digite número: '))
    lista.append (n)

    lista.sort()

print( lista [-1] )
print(  lista [0] )
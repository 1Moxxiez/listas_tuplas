'''
Crie uma fun¸c˜ao que recebe uma lista e retorna uma nova lista com apenas os
elementos ´unicos.
'''

lista = []

for i in range(5):
    n = int(input('Digite u número: '))
    lista.append(n)
    
    
def unicos(lista):
    
    nova_lista = []
    
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
   
    return nova_lista

print(unicos(lista))
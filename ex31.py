'''
Crie uma fun¸c˜ao que verifique se uma lista est´a ordenada.
'''

lista = []

def ordenada (lista):
    
    return lista == sorted(lista)
    
    

for i in range(5):
    n = int(input(f'Digite o {i} numero: '))
    lista.append(n)

if ordenada (lista):
    print('Esta ordenada')
else:
   print('Não esta ordenada')
    
    

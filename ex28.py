'''
Crie uma fun¸c˜ao que receba uma lista e retorne a soma de todos os elementos
num´ericos.

'''

def soma (lista):

    soma = 0

    for item in lista:
        if isinstance(item, (int, float)):
            soma += item
    
    return soma

lista = [2, 2, 2, 2, 2, 'sdadda', 2, 'paola']

print(soma(lista))
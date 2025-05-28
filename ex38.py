'''
. Implemente uma fun¸c˜ao que receba uma lista e retorne os elementos na ordem
inversa.
'''

def inverter_lista(lista):
    return lista[::-1]



minha_lista = [1, 2, 3, 4, 5]

lista_invertida = inverter_lista(minha_lista)


print("Lista invertida:", lista_invertida)

'''
. Implemente uma fun¸c˜ao que conte quantas vezes um valor aparece em uma lista.
'''

def contar_ocorrencias(lista, valor):
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    return contador


minha_lista = [1, 2, 3, 2, 4, 2, 5]
valor = 2
ocorrencias = contar_ocorrencias(minha_lista, valor)
print(f"O valor {valor} aparece {ocorrencias} vezes na lista.")

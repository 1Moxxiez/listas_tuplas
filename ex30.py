'''
. Dada uma lista de strings, crie uma nova lista com o tamanho (n´umero de caracteres)
de cada string.

'''

lista = ["banana", 'pera', 'uva', 'maçã']

tamanho = [len(item) for item in lista]

print(tamanho)
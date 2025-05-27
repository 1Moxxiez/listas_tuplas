'''
Dada uma lista de nomes, retorne uma nova lista com os nomes em letras mai´usculas.
'''

lista = ['Pedro', 'Paulo', 'Alex', 'Roberto', 'Mingau']

nova_lista = [nome.upper() for nome in lista]

print(nova_lista)
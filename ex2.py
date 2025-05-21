'''
2 - Solicite ao usu´ario 5 nomes e armazene em uma lista. Depois, imprima cada nome
em uma linha
'''

lista = []

for i in range(1, 6):
    n = input("Digite nome: ")
    
    lista.append(n)
    
for j in lista:
    print(j)
    
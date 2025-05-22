'''
Solicite nomes at´e que o usu´ario digite ”sair”. Armazene em uma lista e imprima.

'''


n = ""
lista = []

while n != 'Sair':
    n = input('Digite um nome: ').lower().title()
    
    if n != 'Sair':
        lista.append(n)
        
print(lista)
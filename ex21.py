'''
1. Solicite ao usu´ario 10 n´umeros, armazene em uma lista e remova todos os n´umeros
pares usando remove.

'''

lista = []

for i in range(10):
    n = int(input("Digite um número: "))
    lista.append(n)
    
for num in lista[:]:
    if num % 2 == 0:
        lista.remove(num)
    

print(lista)
    
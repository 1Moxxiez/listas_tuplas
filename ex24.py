'''
Separe uma lista de n´umeros em duas: uma com pares e outra com ´ımpares.

'''

lista = []
# lpar = []
# limpar = []

for i in range (1, 15):
    lista.append(i)

# for item in lista:
#     if item % 2 == 0:
#         lpar.append(item)
        
#     else:
#         limpar.append(item)

#print(lpar)
#print(limpar)
        
def impa_par(lista):
    par = []
    impar = []
    
    for item in lista:
        if item % 2 == 0:
            par.append(item)
        
        else:
            impar.append(item)

    return par, impar

lista_pares, lista_impares = impa_par(lista)

print( lista_pares)
print( lista_impares)


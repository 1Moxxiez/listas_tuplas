'''
Crie uma fun¸c˜ao que retorne o segundo maior n´umero de uma lista.
'''

def segundo_maior(lista):
    lista_unica = list(set(lista))
    if len(lista_unica) < 2:
        
        return None 
    
    lista_unica.sort(reverse=True)
    
    return lista_unica[1]


numeros = [10, 20, 5, 8, 20, 3]
resultado = segundo_maior(numeros)


if resultado is not None:
    print(resultado)
    
    
else:
    print("Num tem.")

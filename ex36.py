'''
Crie uma fun¸c˜ao que retorne o segundo maior n´umero de uma lista.
'''

# def segundo_maior(lista):
#     # Remove duplicatas e ordena a lista em ordem decrescente
#     lista_unica = list(set(lista))
#     if len(lista_unica) < 2:
        
#         return None  # Não há segundo maior
    
#     lista_unica.sort(reverse=True)
#     return lista_unica[1]


numeros = [10, 20, 5, 8, 20, 3]
resultado = segundo_maior(numeros)


if resultado is not None:
    print("O segundo maior número é:", resultado)
else:
    print("Não há segundo maior número na lista.")

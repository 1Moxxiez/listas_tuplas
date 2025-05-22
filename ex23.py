'''
Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a
ordem.

'''

lista = ['Samara','Jetulio Vargas' ,'Jaiminho' , 'Samara','Jetulio Vargas','Pedro']

def unicos(lista):
    
    nova_lista = []
    
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    
    return nova_lista

# def unicos(lista):
#     return(set(lista))


print (unicos(lista))
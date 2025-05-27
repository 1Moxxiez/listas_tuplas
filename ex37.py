'''
Crie uma lista de palavras e remova as que tiverem menos de 4 letras
'''

lista = ["sol", "casa", "mar", "livro", "paz", "janela", "céu"]


palavras_filtradas = [item for item in lista if len(item) >= 4]


print("Palavras com 4 letras ou mais:")
print(palavras_filtradas)

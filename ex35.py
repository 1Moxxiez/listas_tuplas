'''
Crie uma lista de tuplas contendo nomes e idades. Imprima os nomes das pessoas
com mais de 18 anos.
'''


pessoas = [("Ana", 17), ("Carlos", 25), ("Mariana", 19), ("Pedro", 15), ("Fernanda", 22)]


print("Pessoas com mais de 18 anos:")
for nome, idade in pessoas:
    if idade > 18:
        print(nome)

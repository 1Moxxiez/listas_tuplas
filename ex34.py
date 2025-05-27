'''
Fa¸ca um programa que leia n´umeros do usu´ario at´e digitar -1. Depois, imprima a
m´edia.

'''

soma = 0
quantidade = 0


while True:
    numero = float(input("Digite um número ou -1 para sair: "))
    if numero == -1:
        break
    
    soma += numero
    quantidade += 1


if quantidade > 0:
    media = soma / quantidade
    print(f"A média dos números digitados é: {media}")
else:
    print("Nenhum número foi digitado.")

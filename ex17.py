'''
. Crie uma lista com 5 n´umeros e calcule a m´edia usando la¸co for.
'''
media = 0

# lista = []
# for i in range(1, 6):
#     lista.append(i)
#     media += i

# print(f'A média é: {media/5}')

lista = [1, 10, 5, 6, 2]

for i in lista:
    media += i
    
print(f'A média é: {media/5}')
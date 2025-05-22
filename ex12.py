'''
Leia 5 n´umeros do usu´ario e verifique se cada um deles ´e maior que 10
'''

contador= 0

for i in range(5):
    n = int(input('Digite um número: '))
    
    if n > 10:
        contador += 1

print(contador)
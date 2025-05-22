'''
Verifique se o n´umero 7 est´a presente na lista [3, 6, 9, 12].
'''

verific = False

lista = [3, 6, 9, 12]

for i in lista:
    if i == 7:
        verific = True
        break
  
if verific:
    print("Verdadeiro")
else:
    print('Ta aki nn')
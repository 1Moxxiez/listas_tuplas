'''
. Simule uma pilha usando append e pop. Mostre a pilha a cada opera¸c˜ao

'''
#Carga iniicial da pilha
pilha = [0]

#pilha carregando:
for i in range(1, 101):
    pilha.append(i)

#Pilha carregada
print(pilha)

#pilha sendo usada
for i in range(100):
    pilha.pop()

#pilha descarregada
print(pilha)


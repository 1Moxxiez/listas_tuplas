'''
Crie um menu interativo que permita adicionar, remover, listar ou sair de um programa que manipula listas.
'''
import tkinter as tk
from tkinter import messagebox

lista = []

def adiciona ():
   item = entrada.get()
   
   if item:
       lista.append(item)
       entrada.delete(0,tk.END) #Limpa o campo de texto depois que o item é adicionado.
                                #entrada.delete(início, fim)
    #    atualizar_lista()
    
   else:
        messagebox.showinfo("Adicionar", "Nenhum item foi informado.")
       
       
       
       
def remove ():
    selecao = lista_box.curselection() # retorna uma tupla com os índices selecionados
    
    if selecao:
        indice = selecao[0]
        lista.pop(indice) #n posso dar pop direto em seleção pq ela é uma tupla de indice, n entendi na vdd essa bosta
        
        atualizar_lista()
    
    else:
         messagebox.showinfo("Remove", "Nenhum item foi selecionado.")
    
    
    
    
def listar ():
    if not lista:
        messagebox.showinfo("Lista", "A lista está vazia.")
        
    atualizar_lista()
        # Lista exibida
    lista_box.pack(pady=10, fill=tk.BOTH, expand=True)
    
    
    
    
    
def  atualizar_lista():
    lista_box.delete(0, tk.END)
    
    for item in lista:
        lista_box.insert(tk.END, item)



# Criar janela menu
menu = tk.Tk()
menu.title("Menu")
menu.geometry("300x300") #tamanho   

#inserir valor a ser adicionado
# Campo de entrada
entrada = tk.Entry(menu)
entrada.pack(pady=5) #espaçamento

# Criar botão
tk.Button(menu, text = "Adicionar", command = adiciona).pack(pady=5)
tk.Button(menu, text= "Remover", command= remove).pack(pady=5)
tk.Button(menu, text= "Listar", command= listar).pack(pady=5)
tk.Button(menu, text= "Sair", command= menu.quit).pack(pady=5)

# Lista exibida
lista_box = tk.Listbox(menu, selectmode=tk.SINGLE) #permite seleção ao clicar no item
lista_box.pack(pady=10, fill=tk.BOTH, expand=True)

'''
tk.Listbox:	Widget do tkinter que exibe uma lista de itens rolável e visual.

(menu):	Significa que esse Listbox vai ser colocado dentro da janela menu.

lista_box =: ...	Armazena esse componente na variável lista_box, que você usa depois para inserir ou limpar itens 
com lista_box.insert(...) ou lista_box.delete(...).

pady=10:	Adiciona espaço vertical (10 pixels em cima e embaixo) para não ficar colado em outros elementos.

fill=tk.BOTH:	Faz com que a lista se expanda tanto na horizontal quanto na vertical, ocupando todo o espaço disponível.

expand=True:	Permite que a lista cresça junto com a janela, se ela for redimensionada.
'''

# Iniciar janela e manter aberta
menu.mainloop()


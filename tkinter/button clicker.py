import tkinter

presses = 0
#cria a janela e a configura:

window = tkinter.Tk()
window.geometry("200x100")
window.title("Contador de Cliques")

#definindo funções:

def addClick():
    global presses
    presses += 1
    lbl.configure(text=presses)

#cria os elementos da tela:

lbl = tkinter.Label(window, text="Você não clicou nenhuma vez")
btn = tkinter.Button(window, text="Clique!", fg="ghost white", command=addClick)

#adiciona os elementos criados no loop principal da janela:

lbl.pack()
btn.pack()
window.mainloop()
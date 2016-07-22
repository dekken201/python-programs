import tkinter

#cria a janela e a configura:

window = tkinter.Tk()
window.geometry("220x120")
window.title("Color Shifter")

#definindo funções:

def makeRed():
    window.configure(background="red")
    lbl.configure(text="VERMELHO", bg="red", fg="ghost white")

def makeBlue():
    window.configure(background="blue")
    lbl.configure(text="AZUL", bg="blue", fg="ghost white")

def makeYellow():
    window.configure(background="yellow")
    lbl.configure(text="AMARELO", bg="yellow", fg="black")


#cria os elementos da tela:

lbl = tkinter.Label(window, text="Clique no botão com a cor desejada")
btn = tkinter.Button(window, text="Red", command=makeRed)
btn2 = tkinter.Button(window, text="Blue", command=makeBlue)
btn3 = tkinter.Button(window, text="Yellow", command=makeYellow)

#adiciona os elementos criados no loop principal da janela:

lbl.pack()
btn.pack()
btn2.pack()
btn3.pack()
window.mainloop()
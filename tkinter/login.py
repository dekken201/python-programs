import tkinter
#cria a janela e a configura:
window = tkinter.Tk()
window.geometry("400x600")
window.configure(background="light slate gray")
window.title("Login Screen")
#cria os elementos da tela:
lbl = tkinter.Label(window, text="Username:", bg="light slate gray", fg="ghost white")
lbl2 = tkinter.Label(window, text="Password:", bg="light slate gray", fg="ghost white")
ent = tkinter.Entry(window)
ent2 = tkinter.Entry(window)
btn = tkinter.Button(window, text="Login", fg="ghost white")

#adiciona os elementos criados no loop principal da janela:
lbl.pack()
ent.pack()
lbl2.pack()
ent2.pack()
btn.pack()
window.mainloop()

from tkinter import *


class Main:
    def __init__(self, parent):
        self.parent = parent
        self.fr1 = Frame(parent)
        self.botao1 = Button(self.fr1, text="Green", background='green')
        self.botao2 = Button(self.fr1, bg="red", text="Red")

        self.initUI()


    def initUI(self):
        self.parent.title("Frankie")
        self.fr1.pack()
        self.botao1.pack()
        self.botao2.pack()




def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Main(root)
    root.mainloop()


if __name__ == '__main__':
    main()

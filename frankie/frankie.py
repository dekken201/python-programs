"""FALTA: Definir função de saída de frame reconfigurada (fatorial, average)

"""
import tkinter as tk


class MainMenu:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Frankie")
        self.frame = tk.Frame(self.parent)
        self.frame.pack()

        self.botao1 = tk.Button(self.frame, text="Math Stuff", background='green', command=self.newWindow)
        self.botao1.pack()


        #self.botao2 = tk.Button(self.fr1, bg="red", text="Red")
        #self.botao2.pack()


    def newWindow(self):
        self.newWindow = tk.Toplevel(self.parent)
        self.app = MathWindow(self.newWindow)


class MathWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Math Functions")
        self.frame = tk.Frame(self.parent)
        self.frame.pack()

        self.btn1 = tk.Button(self.frame, text="Factorial", command=self.factorial)
        self.btn1.pack()

        self.btn2 = tk.Button(self.frame, text="Average", command=self.average)
        self.btn2.pack()


    def factorial(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.parent)
        self.frame.pack()
        self.label = tk.Label(self.parent, text="hey")
        self.label.pack()
        #self.button = tk.Button(self.parent, text="Go Back!")
        #self.button.pack()



    def average(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.parent)
        self.frame.pack()
        self.label = tk.Label(self.parent, text="sup")
        self.label.pack()
        #self.button = tk.Button(self.parent, text="Go Back!")
        #self.button.pack()



def main():
    root = tk.Tk()
    root.geometry("250x150+300+300")
    app = MainMenu(root)
    root.mainloop()


if __name__ == '__main__':
    main()

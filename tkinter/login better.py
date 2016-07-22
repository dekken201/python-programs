#Simples janela de login, que usa um dicionário contendo os logins e senhas,
#com janela de registro com entradas pra adicionar ao dicionário e realizar o login na
#janela inicial.
#TO DO : Arrumar janela de registro


from tkinter import *

#create the initial class
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.headerFont = ("Liberation Sans", "16", "bold")
        self.title("Aperture Science")
        self.setInfo()
        self.database = {"login" : "password"}

#define basic information and labels
    def setInfo(self):
        Label(self, text = "Login Screen", font = self.headerFont).grid(columnspan = 6)

        Label(self, text = "Username: ").grid(row = 1, column = 0)
        self.login = Entry(self)
        self.login.grid(row = 1, column = 1)

        Label(self, text = "Password: ").grid(row = 2, column = 0)
        self.password = Entry(self)
        self.password.grid(row = 2, column = 1)

        Label(self, text = "").grid(row = 5, column = 0)
        self.lblOutput = Label(self, bg = "dim gray")
        self.lblOutput.grid(row = 3, column = 1, sticky = "we")

        self.btnClick = Button(self, text = "Login", padx=18, pady=8)
        self.btnClick.grid(row = 4, columnspan = 5)
        self.btnClick["command"] = self.Login

        self.btnClick = Button(self, text = "Register", padx=10, pady=8)
        self.btnClick.grid(row = 5, columnspan = 5)
        self.btnClick["command"] = self.Register

#active functions
    def Login(self):
        if (self.login.get()) in (list(self.database.keys())):
            if (self.password.get()) in (list(self.database.values())):
                self.lblOutput.configure(text="Login Sucessful!")
            else:
                self.lblOutput.configure(text="Incorrect Password!")
        else:
            self.lblOutput.configure(text="Incorrect Login!")


    def Register(self):
        reg_window = Toplevel()
        reg_window.wm_title("Register Screen")
        Label(reg_window, text = "Register here!", font = self.headerFont).grid(columnspan = 6)
        Label(reg_window, text = "Type your desired username \n and your desired password twice.").grid(row = 1, column = 0)

        Label(reg_window, text = "Username: ").grid(row = 2, column = 0)
        reg_window.reg_login = Entry(reg_window)
        reg_window.reg_login.grid(row = 2, column = 1)

        Label(reg_window, text = "Password: ").grid(row = 3, column = 0)
        reg_window.reg_password = Entry(reg_window)
        reg_window.reg_password.grid(row = 3, column = 1)

        Label(reg_window, text = "Confirm Password: ").grid(row = 4, column = 0)
        reg_window.reg_password2 = Entry(reg_window)
        reg_window.reg_password2.grid(row = 4, column = 1)

        Label(reg_window, text = "").grid(row = 5, column = 0)
        reg_window.regOutput = Label(reg_window, bg = "dim gray")
        reg_window.regOutput.grid(row = 5, column = 1, sticky = "we")

        reg_window.btnClick = Button(reg_window, text = "Register!", padx=18, pady=8)
        reg_window.btnClick.grid(row = 6, column = 0)
        reg_window.btnClick["command"] = self.checkRegister


    def checkRegister(reg_window):
        if (reg_window.reg_login.get()) in (list(self.database.keys())):
            reg_window.regOutput.configure(text="Login already exists!")
        else:
            if (reg_window.reg_password.get()) == (reg_window.reg_password2.get()):
                self.database[reg_window.reg_login.get()] = (reg_window.reg_password.get())
                reg_window.regOutput.configure(text="Registered sucessfully")
            else:
                reg_window.regOutput.configure(text="Both passwords don't match!")



#main loopś
def main():
    a = App()
    a.mainloop()


if __name__ == "__main__":
    main()
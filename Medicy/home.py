import tkinter as tk

class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="This is the home page").pack(pady=10)
        
        tk.Button(self, text="Go to Login",
                  command=lambda: controller.show_frame("Login")).pack()
        tk.Button(self, text="Go to Register",
                  command=lambda: controller.show_frame("Register")).pack()
        
        # self.ventana1= Ventana.fondo()


        self.miFrame = tk.Frame(ventana1)
        self.miFrame.pack()
        self.miFrame.config(bg="#DDF7F5")
        self.miFrame.config(width="10", height="10")

        titulo = Label(miFrame, text="MEDICY", bg="#DDF7F5", fg="pink", width="100", height="3", font=("Arial Black", 15))
        titulo.pack()
        self.framel = LabelFrame(self.ventana1, text="Login", width=300, height=50, padx=50, pady=10)
        self.framel.config(bg="#DDF7F5")
        self.framel.pack()

        self.userLabel = Label(self.framel, text="Usuario: ")
        self.userLabel.grid(row=1, column=0, sticky="w")
        self.userLabel.config(fg="black", bg="white")
        self.userTexto = Entry(self.framel)
        self.userTexto.grid(row=1, column=1, padx=10, pady=10)
        self.userTexto.config(fg="black", bg="white")

        self.passLabel = Label(self.framel, text="Contraseña: ")
        self.passLabel.grid(row=2, column=0, sticky="w")
        self.passLabel.config(fg="black", bg="white")
        self.passTexto = Entry(self.framel)
        self.passTexto.grid(row=2, column=1, padx=50, pady=10)
        self.passTexto.config(fg="black", bg="white")

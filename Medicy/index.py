from tkinter import *
from ventana import Ventana
from registro import Registrarse
from lista_turnos import MostrarTurnos


class VentanaPrincipal():
    
    def __init__(self):
        
        self.ventana1= Ventana.fondo()

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

        self.btn_login()
        self.btn_registro()
        
              
        self.ventana1.mainloop()

    def inicio(self):
        self.ventana1.destroy() 
        MostrarTurnos()

    def abrir_registro(self):
        self.ventana1.destroy() 
        Registrarse()
        
   
    def btn_login(self):
        self.boton_login = Button(self.framel, text="Iniciar Sesión ", command=self.inicio)
        self.boton_login.config(bg="#C1E2F3")
        self.boton_login.grid(row=3, column=1)

    def btn_registro(self):
        self.boton_registro=Button(self.framel, text="Registrarse ", command=self.abrir_registro)
        self.boton_registro.config(bg="#F9DBED")
        self.boton_registro.grid(row=5,column=1, padx=10, pady=10)

    
App1 = VentanaPrincipal()


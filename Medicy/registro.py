from tkinter import *
from ventana import Ventana
from lista_turnos import MostrarTurnos

class Registrarse():

    def __init__(self):
        
        self.ventana1= Ventana.fondo()

        self.framel=LabelFrame(self.ventana1, text="Registrarse", width=300, height=50, padx=50, pady=10)
        self.framel.config(bg="#DDF7F5")
        self.framel.pack()

        self.nombreLabel= Label(self.framel, text= "Nombre: ")
        self.nombreLabel.grid(row=1, column=0, sticky="w")
        self.nombreLabel.config(fg="black", bg="white" )
        self.nombreTexto = Entry(self.framel)
        self.nombreTexto.grid(row=1, column=1,padx=10, pady=10)
        self.nombreTexto.config(fg="black", bg="white" )

        self.apellidoLabel= Label(self.framel, text= "Apellido: ")
        self.apellidoLabel.grid(row=2, column=0, sticky="w")
        self.apellidoLabel.config(fg="black", bg="white" )
        self.apellidoTexto = Entry(self.framel)
        self.apellidoTexto.grid(row=2, column=1,padx=10, pady=10)
        self.apellidoTexto.config(fg="black", bg="white" )

        self.telefonoLabel= Label(self.framel, text= "Telefono: ")
        self.telefonoLabel.grid(row=3, column=0, sticky="w")
        self.telefonoLabel.config(fg="black", bg="white" )
        self.telefonoTexto = Entry(self.framel)
        self.telefonoTexto.grid(row=3, column=1,padx=10, pady=10)
        self.telefonoTexto.config(fg="black", bg="white" )

        self.correoLabel= Label(self.framel, text= "Correo Electronico: ")
        self.correoLabel.grid(row=4, column=0, sticky="w")
        self.correoLabel.config(fg="black", bg="white" )
        self.correoTexto = Entry(self.framel)
        self.correoTexto.grid(row=4, column=1,padx=10, pady=10)
        self.correoTexto.config(fg="black", bg="white" )

        self.contraseñaLabel= Label(self.framel, text= "Contraseña : ")
        self.contraseñaLabel.grid(row=5, column=0, sticky="w")
        self.contraseñaLabel.config(fg="black", bg="white")
        self.contraseñaTexto= Entry(self.framel)
        self.contraseñaTexto.grid(row=5, column=1, padx=50, pady=10,)
        self.contraseñaTexto.config(fg="black", bg="white")

        self.btn_inicio()
        

    def inicio(self):
        self.ventana1.destroy()
        MostrarTurnos()
        

    def btn_inicio(self):
        self.boton_inicio = Button(self.framel, text="Iniciar Sesión ", command=self.inicio)
        self.boton_inicio.config(bg="#C1E2F3")
        self.boton_inicio.grid(row=6, column=1)


   









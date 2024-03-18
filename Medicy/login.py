import tkinter as tk
from usuarios import Usuario
from tkinter import messagebox

class Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#DDF7F5")

        center_frame = tk.Frame(self, bg="#DDF7F5")
        center_frame.pack(expand=True)

        framel = tk.LabelFrame(center_frame, text="Login", bg="#DDF7F5", padx=50, pady=50)
        framel.pack()


        userLabel = tk.Label(framel, text="Usuario: ", fg="black", bg="white")
        userLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.userTexto = tk.Entry(framel, fg="black", bg="white")
        self.userTexto.grid(row=0, column=1, padx=10, pady=10)

        passLabel = tk.Label(framel, text="Contraseña: ", fg="black", bg="white")
        passLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        self.passTexto = tk.Entry(framel, fg="black", bg="white")
        self.passTexto.grid(row=1, column=1, padx=10, pady=10)

        boton_login = tk.Button(framel, text="Iniciar Sesión", bg="#C1E2F3", command=self.login)
        boton_login.grid(row=2, column=1, pady=10)

        boton_registro = tk.Button(framel, text="Registrarse", bg="#F9DBED", command=lambda: controller.show_frame("Registro"))
        boton_registro.grid(row=6, column=1, pady=10)

    def login(self):
        username = self.userTexto.get()
        password = self.passTexto.get()
        
        authenticated, user_id = Usuario.verificar_credenciales(username, password)
        
        if authenticated:
            self.controller.id_usuario = user_id
            self.controller.show_frame("MostrarTurnos")
        else:
            messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrecta")
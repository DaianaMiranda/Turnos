import tkinter as tk
from tkinter import messagebox
from usuarios import Usuario  

class Registro(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#DDF7F5")

        center_frame = tk.Frame(self, bg="#DDF7F5")
        center_frame.pack(expand=True)

        framel = tk.LabelFrame(center_frame, text="Registrarse", bg="#DDF7F5", padx=50, pady=50)
        framel.pack()

        self.entries = {}
        fields = ["Nombre", "Apellido", "Telefono", "Correo Electronico", "Contraseña"]
        
        for i, field in enumerate(fields):
            tk.Label(framel, text=f"{field}: ", fg="black", bg="white").grid(row=i, column=0, sticky="w", padx=10, pady=10)
            entry = tk.Entry(framel, fg="black", bg="white")
            entry.grid(row=i, column=1, padx=10, pady=10)
            self.entries[field] = entry
        

        boton_registrar = tk.Button(framel, text="Registrarse", bg="#C1E2F3", command=self.registrar_usuario)
        boton_registrar.grid(row=len(fields), column=1, pady=10)

        boton_inicio = tk.Button(framel, text="Volver", bg="#F9DBED", command=lambda: controller.show_frame("Login"))
        boton_inicio.grid(row=len(fields)+1, column=1, pady=10)

    def registrar_usuario(self):
        nombre = self.entries["Nombre"].get()
        apellido = self.entries["Apellido"].get()
        telefono = self.entries["Telefono"].get()
        correo = self.entries["Correo Electronico"].get()
        contra = self.entries["Contraseña"].get()

        
        try:
    # Verificar si algún campo está vacío
            if not all((nombre, contra, apellido, telefono, correo)):
                messagebox.showerror("Error", "Por favor, complete todos los campos")
            else:
                Usuario.crear_usuario(nombre, contra, apellido, telefono, correo)
                messagebox.showinfo("Éxito", "Usuario registrado con éxito")
                self.controller.show_frame("Login")
        except Exception as e:
            messagebox.showerror("Error", str(e))

        

       
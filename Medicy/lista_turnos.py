# import tkinter as tk
# from tkinter import ttk
# # Assuming Medico class is in medico.py and has been updated as described
# from medico import Medico

# class MostrarTurnos(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         self.controller = controller
#         self.config(bg="#DDF7F5")
#         self.medicos = Medico.obtener_medicos()  # Fetching medicos
#         self.create_widgets()

#     def create_widgets(self):
#         self.create_treeview()
#         self.create_buttons()

#     def create_treeview(self):
#         # Set up the treeview
#         self.treeview = ttk.Treeview(self, columns=("col1", "col2", "col3"))
#         self.treeview.column("#0", width=100, anchor=tk.CENTER)
#         self.treeview.column("col1", width=80, anchor=tk.CENTER)
#         self.treeview.column("col2", width=120, anchor=tk.CENTER)
#         self.treeview.column("col3", width=50, anchor=tk.CENTER)

#         self.treeview.heading("#0", text="Nombre y Apellido", anchor=tk.CENTER)
#         self.treeview.heading("col1", text="Especialidad", anchor=tk.CENTER)
#         self.treeview.heading("col2", text="Fecha", anchor=tk.CENTER)
#         self.treeview.heading("col3", text="Hora", anchor=tk.CENTER)

#         for medico in self.medicos:
#             horarios = medico.obtener_horarios_medico()
#             for horario in horarios:
#                 self.treeview.insert("", "end", text=medico.nombre_apellido, values=(medico.especialidad, horario[0], horario[1]))

#         self.treeview.pack(expand=True, fill=tk.BOTH)

#     def create_buttons(self):
#         self.boton_solicitar_turno = tk.Button(self, text="Solicitar Turno", bg="pink", command=self.solicitar_turno)
#         self.boton_solicitar_turno.pack(side=tk.BOTTOM, pady=10)

#         self.boton_salir = tk.Button(self, text="Salir", bg="pink", command=self.salir)
#         self.boton_salir.pack(side=tk.BOTTOM, pady=10)

#     def solicitar_turno(self):
#         self.controller.show_frame("SolicitudTurnos")


#     def salir(self):
#         self.controller.show_frame("Login")

#     def actualizar_turnos(self, turnos):
#         self.treeview.delete(*self.treeview.get_children())  # Borra los datos existentes en el treeview
#         for turno in turnos:
#             self.treeview.insert("", "end", values=turno)

import tkinter as tk
from tkinter import ttk, messagebox

class MostrarTurnos(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#DDF7F5")
        self.turnos = []
        self.create_widgets()

    def create_widgets(self):
        self.create_treeview()
        self.create_buttons()  # Llamar al método para crear botones

    def create_treeview(self):
        # Set up the treeview
        self.treeview = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4"))
        self.treeview.column("#0", width=100, anchor=tk.CENTER)
        self.treeview.column("col1", width=80, anchor=tk.CENTER)
        self.treeview.column("col2", width=120, anchor=tk.CENTER)
        self.treeview.column("col3", width=120, anchor=tk.CENTER)
        
        self.treeview.heading("#0", text="Nombre y Apellido", anchor=tk.CENTER)
        self.treeview.heading("col1", text="Especialidad", anchor=tk.CENTER)
        self.treeview.heading("col2", text="Fecha", anchor=tk.CENTER)
        self.treeview.heading("col3", text="Hora", anchor=tk.CENTER)
      

        self.treeview.pack(expand=True, fill=tk.BOTH)

    def create_buttons(self):
        self.boton_solicitar_turno = tk.Button(self, text="Solicitar Turno", bg="pink", command=self.boton_solicitar_turno)
        self.boton_solicitar_turno.pack(side=tk.BOTTOM, pady=10)

        self.boton_salir = tk.Button(self, text="Salir", bg="pink", command=self.salir)
        self.boton_salir.pack(side=tk.BOTTOM, pady=10)



    def solicitar_turno(self):
        self.controller.show_frame("SolicitudTurnos")

    def salir(self):
        self.controller.show_frame("Login")

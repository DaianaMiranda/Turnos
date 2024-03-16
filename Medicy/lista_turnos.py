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
        self.treeview = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4", "col5"))
        self.treeview.column("#0", width=100, anchor=tk.CENTER)  # Often used for an ID or main identifier
        self.treeview.column("col1", width=80, anchor=tk.CENTER)
        self.treeview.column("col2", width=120, anchor=tk.CENTER)
        self.treeview.column("col3", width=120, anchor=tk.CENTER)
        self.treeview.column("col4", width=120, anchor=tk.CENTER)  # New column
        
        self.treeview.heading("#0", text="ID", anchor=tk.CENTER)  # If #0 is used for IDs
        self.treeview.heading("col1", text="Nombre y Apellido", anchor=tk.CENTER)
        self.treeview.heading("col2", text="Especialidad", anchor=tk.CENTER)
        self.treeview.heading("col3", text="Fecha", anchor=tk.CENTER)
        self.treeview.heading("col4", text="Hora", anchor=tk.CENTER)  # Heading for the new column
        # Adjust the heading text to match your data

        self.treeview.pack(expand=True, fill=tk.BOTH)

    def cargar_turnos_usuario(self):
        id_usuario = self.controller.id_usuario
        if id_usuario is not None:
            turnos = self.controller.datos_turnos.obtener_turnos_usuario(id_usuario)
            for turno in turnos:
                # Assuming turno includes the additional piece of data as the 5th element
                id_med, nombre_medico, especialidad, fecha, hora = turno
                # Adjust as per your actual data structure
                self.treeview.insert("", "end", text=id_med, values=(nombre_medico, especialidad, fecha, hora))
        else:
            messagebox.showerror("Error", "No se pudo cargar los turnos del usuario.")

    def create_buttons(self):
        # Adjusted to use a different method for the command
        self.boton_solicitar_turno = tk.Button(self, text="Solicitar Turno", bg="pink", command=self.on_solicitar_turno_click)
        self.boton_solicitar_turno.pack(side=tk.BOTTOM, pady=10)

        self.boton_salir = tk.Button(self, text="Salir", bg="pink", command=self.salir)
        self.boton_salir.pack(side=tk.BOTTOM, pady=10)

    def on_solicitar_turno_click(self):
        # This method is called when the "Solicitar Turno" button is clicked
        self.controller.show_frame("SolicitudTurnos")

    def salir(self):
        # This method is called when the "Salir" button is clicked
        self.controller.show_frame("Login")

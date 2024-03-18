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
        self.create_buttons()

    def create_treeview(self):

        self.treeview = ttk.Treeview(
            self, columns=("col1", "col2", "col3", "col4", "col5")
        )
        self.treeview.column("#0", width=100, anchor=tk.CENTER)
        self.treeview.column("col1", width=80, anchor=tk.CENTER)
        self.treeview.column("col2", width=120, anchor=tk.CENTER)
        self.treeview.column("col3", width=120, anchor=tk.CENTER)
        self.treeview.column("col4", width=120, anchor=tk.CENTER)

        self.treeview.heading("#0", text="ID", anchor=tk.CENTER)
        self.treeview.heading("col1", text="Nombre y Apellido", anchor=tk.CENTER)
        self.treeview.heading("col2", text="Especialidad", anchor=tk.CENTER)
        self.treeview.heading("col3", text="Fecha", anchor=tk.CENTER)
        self.treeview.heading("col4", text="Hora", anchor=tk.CENTER)

        self.treeview.pack(expand=True, fill=tk.BOTH)

    def cargar_turnos_usuario(self):
        id_usuario = self.controller.id_usuario
        if id_usuario is not None:
            turnos = self.controller.datos_turnos.obtener_turnos_usuario(id_usuario)
            print(f"turnos: {turnos}")
            for turno in turnos:

                id_med, nombre_medico, especialidad, fecha, hora = turno

                self.treeview.insert(
                    "",
                    "end",
                    text=id_med,
                    values=(nombre_medico, especialidad, fecha, hora),
                )
        else:
            messagebox.showerror("Error", "No se pudo cargar los turnos del usuario.")

    def create_buttons(self):

        self.btn_solicitar_turno = tk.Button(
            self,
            text="Solicitar Turno",
            bg="pink",
            command=self.on_solicitar_turno_click,
        )
        self.btn_solicitar_turno.pack(side=tk.BOTTOM, pady=10)

        self.btn_salir = tk.Button(self, text="Salir", bg="pink", command=self.salir)
        self.btn_salir.pack(side=tk.BOTTOM, pady=10)

    def on_solicitar_turno_click(self):

        self.controller.show_frame("SolicitudTurnos")

    def salir(self):

        self.controller.show_frame("Login")


    def reset_state(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)
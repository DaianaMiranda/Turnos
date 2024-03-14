import tkinter as tk
from tkinter import ttk, messagebox

class SolicitudTurnos(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#DDF7F5")
        self.create_widgets()

    def create_widgets(self):
        # Turno Frame Configuration
        self.turnoFrame = tk.Frame(self, bg="#DDF7F5", padx=50, pady=10)
        self.turnoFrame.pack(pady=20)

        # Especialidad
        tk.Label(self.turnoFrame, text="Especialidad:", bg="white").grid(row=0, column=0, sticky="w")
        lista_especialidades = ["Clínico", "Pediatría", "Ginecología"]
        self.esp_seleccionable = ttk.Combobox(self.turnoFrame, values=lista_especialidades, state="readonly")
        self.esp_seleccionable.grid(row=0, column=1, sticky="w", pady=5)

        # Nombre del Medico
        tk.Label(self.turnoFrame, text="Nombre del Medico:", bg="white").grid(row=1, column=0, sticky="w")
        elementos = ["Marcos Montero", "Lucia Gambardi", "Marcela Pereyra"]
        self.nom_medico = ttk.Combobox(self.turnoFrame, values=elementos, state="readonly")
        self.nom_medico.grid(row=1, column=1, sticky="w", pady=5)

        # Fecha
        tk.Label(self.turnoFrame, text="Fecha:", bg="white").grid(row=2, column=0, sticky="w")
        lista_fechas = ["03/04/2024", "07/04/2024", "10/04/2024"]
        self.fechas = ttk.Combobox(self.turnoFrame, values=lista_fechas, state="readonly")
        self.fechas.grid(row=2, column=1, sticky="w", pady=5)

        # Hora
        tk.Label(self.turnoFrame, text="Hora:", bg="white").grid(row=3, column=0, sticky="w")
        lista_horarios = ["8:00", "10:00", "15:00"]
        self.horarios = ttk.Combobox(self.turnoFrame, values=lista_horarios, state="readonly")
        self.horarios.grid(row=3, column=1, sticky="w", pady=5)

        # Botones
        tk.Button(self.turnoFrame, text="Solicitar Turno", bg="#C1E2F3", command=self.solicitar_turno).grid(row=4, column=1, sticky="w", pady=10)
        tk.Button(self.turnoFrame, text="Volver", bg="pink", command=self.volver).grid(row=5, column=1, sticky="w", pady=10)

    def solicitar_turno(self):
        messagebox.showinfo("Mensaje", "Turno solicitado correctamente")

    def volver(self):
        # Assuming 'Home' is your main menu or starting screen
        self.controller.show_frame("MostrarTurnos")

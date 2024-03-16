
import tkinter as tk
from tkinter import ttk, messagebox
from medico import DatosTurnos

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
        self.esp_seleccionable = ttk.Combobox(self.turnoFrame, state="readonly")
        self.esp_seleccionable.grid(row=0, column=1, sticky="w", pady=5)
        self.esp_seleccionable.bind("<<ComboboxSelected>>", self.cargar_medicos)

        # Nombre del Medico
        tk.Label(self.turnoFrame, text="Nombre del Medico:", bg="white").grid(row=1, column=0, sticky="w")
        self.nom_medico = ttk.Combobox(self.turnoFrame, state="readonly")
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

    #     # Cargar datos
    #     self.cargar_especialidades()

    # def cargar_especialidades(self):
    #     especialidades = [medico.especialidad for medico in Medico.obtener_medicos()]
    #     self.esp_seleccionable['values'] = especialidades

    # def cargar_medicos(self, event=None):
    #     especialidad_seleccionada = self.esp_seleccionable.get()
    #     medicos = [medico.nombre_apellido for medico in Medico.obtener_medicos() if medico.especialidad == especialidad_seleccionada]
    #     self.nom_medico['values'] = medicos

    
    
    # def solicitar_turno(self):
    #     especialidad = self.esp_seleccionable.get()
    #     nombre_medico = self.nom_medico.get()

        # messagebox.showinfo("Mensaje", "Turno(s) solicitado(s) correctamente")

  
    


      

    def volver(self):
      
        self.controller.show_frame("MostrarTurnos")



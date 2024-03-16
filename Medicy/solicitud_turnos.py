
import tkinter as tk
from tkinter import ttk, messagebox
from medico import DatosTurnos

class SolicitudTurnos(tk.Frame):


    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#DDF7F5")
        self.datos_turnos = DatosTurnos()
        self.create_widgets()
        self.cargar_especialidades()

    def create_widgets(self):
        # Turno Frame Configuration
        self.turnoFrame = tk.Frame(self, bg="#DDF7F5", padx=50, pady=10)
        self.turnoFrame.pack(pady=20)

        # Nombre del Medico
        tk.Label(self.turnoFrame, text="Nombre del Medico:", bg="white").grid(row=1, column=0, sticky="w")
        self.nom_medico = ttk.Combobox(self.turnoFrame, state="readonly")
        self.nom_medico.grid(row=1, column=1, sticky="w", pady=5)

        # Especialidad
        tk.Label(self.turnoFrame, text="Especialidad:", bg="white").grid(row=0, column=0, sticky="w")
        self.esp_seleccionable = ttk.Combobox(self.turnoFrame, state="readonly")
        self.esp_seleccionable.grid(row=0, column=1, sticky="w", pady=5)
        self.esp_seleccionable.bind("<<ComboboxSelected>>", self.cargar_medicos)

        # Fecha
        tk.Label(self.turnoFrame, text="Fecha:", bg="white").grid(row=2, column=0, sticky="w")
        lista_fechas = ["03/04/2024", "07/04/2024", "10/04/2024"]
        self.fechas = ttk.Combobox(self.turnoFrame, values=lista_fechas, state="readonly")
        self.fechas.grid(row=2, column=1, sticky="w", pady=5)

        # Hora
        tk.Label(self.turnoFrame, text="Hora:", bg="white").grid(row=3, column=0, sticky="w")
        lista_horarios = ["8:00", "10:00", "15:00"]
        self.horarios = ttk.Combobox(self.turnoFrame, values=[], state="readonly")
        self.horarios.grid(row=3, column=1, sticky="w", pady=5)

        # Botones
        tk.Button(self.turnoFrame, text="Solicitar Turno", bg="#C1E2F3", command=self.solicitar_turno).grid(row=4, column=1, sticky="w", pady=10)
        tk.Button(self.turnoFrame, text="Volver", bg="pink", command=self.volver).grid(row=5, column=1, sticky="w", pady=10)

    def cargar_especialidades(self):
        # Method to fetch and load especialidades into self.esp_seleccionable
        especialidades = self.datos_turnos.obtener_especialidades()
        self.esp_seleccionable['values'] = especialidades
        self.esp_seleccionable.bind("<<ComboboxSelected>>", self.cargar_medicos_por_especialidad)


    def cargar_fechas_disponibles(self, event=None):
        nombre_medico = self.nom_medico.get()
        fechas = self.datos_turnos.obtener_fechas_disponibles(nombre_medico)
        self.fechas['values'] = fechas
        self.fechas.bind("<<ComboboxSelected>>", self.cargar_horas_disponibles)

    def cargar_horas_disponibles(self, event=None):
        nombre_medico = self.nom_medico.get()
        fecha_seleccionada = self.fechas.get()
        if not nombre_medico or not fecha_seleccionada:
            self.horarios.set('')
            self.horarios['values'] = []
            return

        horas = self.datos_turnos.obtener_horas_disponibles(nombre_medico, fecha_seleccionada)
        self.horarios['values'] = horas
        if horas:
            self.horarios.set(horas[0])  # Optionally set to first available hour
        else:
            self.horarios.set('')

    def cargar_medicos_por_especialidad(self, event=None):
        especialidad_seleccionada = self.esp_seleccionable.get()
        medicos = self.datos_turnos.obtener_medicos_por_especialidad(especialidad_seleccionada)
        self.nom_medico['values'] = medicos
        self.nom_medico.bind("<<ComboboxSelected>>", self.cargar_fechas_disponibles)

    def cargar_datos_iniciales(self):
        # Load all médicos and their specialties
        self.medicos_info = self.datos_turnos.obtener_todos_los_medicos_con_especialidades()
        especialidades = sorted({medico['especialidad'] for medico in self.medicos_info.values()})
        self.esp_seleccionable['values'] = especialidades
        self.esp_seleccionable.bind("<<ComboboxSelected>>", self.cargar_medicos)

    def cargar_medicos(self, event=None):
        especialidad_seleccionada = self.esp_seleccionable.get()
        medicos = [nombre for nombre, info in self.medicos_info.items() if info['especialidad'] == especialidad_seleccionada]
        self.nom_medico['values'] = medicos

    def solicitar_turno(self):
        nombre_medico = self.nom_medico.get()
        especialidad = self.esp_seleccionable.get()
        fecha = self.fechas.get()
        hora = self.horarios.get()
        
        # Example user ID, replace with actual logic to get current user's ID
        id_usuario = self.controller.id_usuario
        
        if not all([nombre_medico, especialidad, fecha, hora]):
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return
        
        try:
            reserva_exitosa = self.datos_turnos.reservar_turno(nombre_medico, especialidad, fecha, hora, id_usuario)
            if reserva_exitosa:
                messagebox.showinfo("Éxito", "Turno reservado correctamente.")
                self.limpiar_campos()
                # Add any additional logic needed after successful reservation
            else:
                messagebox.showerror("Error", "No se pudo reservar el turno.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def cargar_nombres_medicos(self):
        medicos = self.datos_turnos.obtener_nombres_medicos()
        self.nom_medico['values'] = medicos
        self.nom_medico.bind("<<ComboboxSelected>>", self.actualizar_datos_medico)

    def cargar_fechas_horas(self, event=None):
        nombre_medico = self.nom_medico.get()
        disponibilidad = self.datos_turnos.obtener_disponibilidad_medico(nombre_medico)
        fechas = sorted(set([fecha for fecha, _ in disponibilidad]))
        self.fechas['values'] = fechas
        if fechas:
            self.fechas.set(fechas[0])  # Optionally set to first available date
            horas = [hora for fecha, hora in disponibilidad if fecha == fechas[0]]
            self.horarios['values'] = horas

    def actualizar_datos_medico(self, event=None):
        nombre_medico = self.nom_medico.get()
        if not nombre_medico:
            self.limpiar_campos()
            return

        especialidad_medico = self.datos_turnos.obtener_especialidad_por_medico(nombre_medico)
        self.esp_seleccionable.set(especialidad_medico)
        self.esp_seleccionable['values'] = [especialidad_medico] if especialidad_medico else []
        self.esp_seleccionable.set(especialidad_medico)
        

        fechas_disponibles = self.datos_turnos.obtener_fechas_disponibles(nombre_medico)
        self.fechas['values'] = fechas_disponibles
        if fechas_disponibles:
            self.fechas.set(fechas_disponibles[0])
            self.actualizar_horas_disponibles(fechas_disponibles[0])
        else:
            self.fechas.set('')
            self.horarios.set('')
            self.horarios['values'] = []

        self.cargar_fechas_horas()

    def actualizar_horas_disponibles(self, fecha):
        nombre_medico = self.nom_medico.get()
        horas_disponibles = self.datos_turnos.obtener_horas_disponibles(nombre_medico, fecha)
        self.horarios['values'] = horas_disponibles
        if horas_disponibles:
            self.horarios.set(horas_disponibles[0]) 
        else:
            self.horarios.set('')


    def volver(self):
        self.controller.show_frame("MostrarTurnos")

    def limpiar_campos(self):
        self.esp_seleccionable.set('')
        self.fechas.set('')
        self.fechas['values'] = []
        self.horarios.set('')
        self.horarios['values'] = []

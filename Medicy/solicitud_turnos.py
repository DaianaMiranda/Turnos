from tkinter import Tk, Frame, Label, Button, ttk, messagebox
from ventana import Ventana


class SolicitudTurnos:
    def __init__(self):
        
        self.ventana1= Ventana.fondo()
      
        self.turnoFrame = Frame(self.ventana1, width=300, height=50, padx=50, pady=10)
        self.turnoFrame.config(bg="#DDF7F5")
        self.turnoFrame.pack()

        self.especialidadLabel = Label(self.turnoFrame, text= "Especialidad: ")
        self.especialidadLabel.grid(row=1, column=0, sticky="w")
        self.especialidadLabel.config(fg="black", bg="white" )

        lista_especialidades = ["Clínico", "Pediatría", "Ginecología"]
        self.esp_seleccionable = ttk.Combobox(self.turnoFrame, values=lista_especialidades, state="readonly")
        self.esp_seleccionable.grid(row=1, column=1, sticky="w")
        self.esp_seleccionable.bind("<<ComboboxSelected>>", self.especialidad)

        self.nomMedicoLabel = Label(self.turnoFrame, text= "Nombre del Medico: ")
        self.nomMedicoLabel.grid(row=3, column=0, sticky="w")
        self.nomMedicoLabel.config(fg="black", bg="white" )

        elementos = ["Marcos Montero", "Lucia Gambardi", "Marcela Pereyra"]
        self.nom_medico = ttk.Combobox(self.turnoFrame, values=elementos, state="readonly")
        self.nom_medico.grid(row=3, column=1, sticky="w", pady=20)
        self.nom_medico.bind("<<ComboboxSelected>>", self.medico)

        self.fechaLabel = Label(self.turnoFrame, text= "Fecha: ")
        self.fechaLabel.grid(row=4, column=0, sticky="w")
        self.fechaLabel.config(fg="black", bg="white" )

        lista_fechas = ["03/04/2024", "07/04/2024", "10/04/2024"]
        self.fechas = ttk.Combobox(self.turnoFrame, values=lista_fechas, state="readonly")
        self.fechas.grid(row=4, column=1, sticky="w", pady=20)
        self.fechas.bind("<<ComboboxSelected>>", self.dias)

        self.horaLabel = Label(self.turnoFrame, text= "Hora: ")
        self.horaLabel.grid(row=5, column=0, sticky="w")
        self.horaLabel.config(fg="black", bg="white" )

        lista_horarios = ["8:00", "10:00", "15:00"]
        self.horarios = ttk.Combobox(self.turnoFrame, values=lista_horarios, state="readonly")
        self.horarios.grid(row=5, column=1, sticky="w", pady=20)
        self.horarios.bind("<<ComboboxSelected>>", self.hora)

        self.btn_turno()
        self.btn_volver()

    def btn_turno(self):
        self.boton_turno = Button(self.turnoFrame, text="Solicitar Turno ", command=self.solicitar_turno)
        self.boton_turno.config(bg="#C1E2F3")
        self.boton_turno.grid(row=6,column=1)

    def btn_volver(self):
        self.boton_volver = Button(self.turnoFrame, text="volver ", command=self.volver)
        self.boton_volver.config(bg="pink")
        self.boton_volver.grid(row=7,column=1)

         

    def volver(self):
        self.ventana1.destroy()
   
        
       
        
        

    def especialidad(self, event):
        self.seleccion = self.esp_seleccionable.get()

    def medico(self,event):
        self.seleccion = self.nom_medico.get()

    def dias(self, event):
        self.seleccion = self.fechas.get()

    def hora(self,event):
        self.seleccion = self.horarios.get()

    def solicitar_turno(self):
        messagebox.showinfo("Mensaje", "Turno solicitado correctamente")



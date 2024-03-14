from tkinter import *
from tkinter import ttk
from ventana import Ventana
from solicitud_turnos import SolicitudTurnos
# from medico import Medico

class MostrarTurnos:
    def __init__(self):
        self.ventana1 = Ventana.fondo()
        self.cargar_datos_base()
        self.cuadro_turnos()

    def cargar_datos_base(self):
        pass
        # self.medicos = Medico.obtener_medicos()

    def cuadro_turnos(self):
        self.grid = ttk.Treeview(self.ventana1, columns=("col1", "col2", "col3"))

        self.grid.column("#0", width=100, anchor=CENTER) 
        self.grid.column("col1", width=80, anchor=CENTER)
        self.grid.column("col2", width=50, anchor=CENTER)
        self.grid.column("col3", width=50, anchor=CENTER)

        self.grid.heading("#0", text="Nombre y Apellido", anchor=CENTER)
        self.grid.heading("col1", text="Especialidad", anchor=CENTER)
        self.grid.heading("col2", text="Fecha", anchor=CENTER)
        self.grid.heading("col3", text="Hora", anchor=CENTER)

        # for medico in self.medicos:
        #     horarios = medico.obtener_horarios_medico()
        #     for fecha, hora in horarios:
        #         self.grid.insert("", "end", text=medico.nombre_apellido, values=(medico.especialidad, fecha, hora))

        self.grid.place(x=150, y=250, width=400, height=300)

        self.boton_solicitar_turno = Button(self.ventana1, text="Solicitar Turno", command=self.solicitar_turno, bg="pink")
        self.boton_solicitar_turno.place(x=400, y=520)

        self.boton_salir = Button(self.ventana1, text="Salir", command=self.salir, bg="pink")
        self.boton_salir.place(x=350, y=520, )

    def solicitar_turno(self):
        self.ventana1.destroy()
        SolicitudTurnos()

    def salir(self):
        self.ventana1.destroy()








       
        




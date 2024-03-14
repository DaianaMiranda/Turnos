from conexion import *

class Medico:
    def __init__(self, con, cursor, id_med, especialidad, nombre_apellido):
        self.con = con
        self.cursor = cursor
        self.id_med = id_med
        self.especialidad = especialidad
        self.nombre_apellido = nombre_apellido
        self.horarios = []

    def agregar_horario_turno(self, fecha, hora):
        self.horarios.append((fecha, hora))

    def obtener_horarios(self):
        return self.horarios

   
    def obtener_medicos():
        conexion_bd = ConexionBD()
        con = conexion_bd.con
        cursor = conexion_bd.cursor
        query = "SELECT id_med, especialidad, nombre_apellido FROM medicos"  
        cursor.execute(query)
        resultados = cursor.fetchall()
    
        medicos = [Medico(con, cursor, id_med, especialidad, nombre_apellido) for id_med, especialidad, nombre_apellido in resultados]
        conexion_bd.cerrar_conexion()
        return medicos

    def obtener_horarios_medico(self):
        query = "SELECT fecha, hora FROM horarios WHERE id_med = %s"
        self.cursor.execute(query, (self.id_med,))
        return self.cursor.fetchall()




# from conexion import ConexionBD

# class Medico:
#     def __init__(self, con, cursor, especialidad, nombre_apellido):
#         self.con = con
#         self.cursor = cursor
#         self.especialidad = especialidad
#         self.nombre_apellido = nombre_apellido
#         self.horarios = []

#     def agregar_horario_turno(self, fecha, hora):
#         self.horarios.append((fecha, hora))

#     def obtener_horarios(self):
#         return self.horarios

#     # @staticmethod
#     def obtener_medicos(conexion, cursor):
#         query = "SELECT especialidad, nombre_apellido FROM medicos"
#         cursor.execute(query)
#         resultados = cursor.fetchall()
#         return [Medico(conexion, cursor, especialidad, nombre_apellido) for especialidad, nombre_apellido in resultados]

#     def obtener_horarios_medico(self, id_medico):
#         query = "SELECT fecha, hora FROM horarios WHERE id_medico = %s"
#         self.cursor.execute(query, (id_medico,))
#         return self.cursor.fetchall()

# if __name__ == "__main__":
#     conexion_bd = ConexionBD()
#     con = conexion_bd.con
#     cursor = conexion_bd.cursor

#     medicos = Medico.obtener_medicos(con, cursor)

#     for medico in medicos:
#         horarios = medico.obtener_horarios_medico(id)
#         for fecha, hora in horarios:
#             medico.agregar_horario_turno(fecha, hora)

#     for medico in medicos:
#         print("Médico:", medico.nombre_apellido)
#         print("Especialidad:", medico.especialidad)
#         print("Horarios:")
#         for fecha, hora in medico.obtener_horarios():
#             print("- Fecha:", fecha, "- Hora:", hora)
#         print()

#     conexion_bd.cerrar_conexion() 

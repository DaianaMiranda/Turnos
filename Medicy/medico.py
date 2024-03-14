from conexion import ConexionBD  # Ensure you have the updated ConexionBD class that supports context management

class Medico:
    def __init__(self, id_med='', especialidad='', nombre_apellido=''):
        self.id_med = id_med
        self.especialidad = especialidad
        self.nombre_apellido = nombre_apellido

    @staticmethod
    def obtener_medicos():
        medicos = []
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = "SELECT id_med, especialidad, nombre_apellido FROM medicos"
            cursor.execute(query)
            for id_med, especialidad, nombre_apellido in cursor.fetchall():
                medicos.append(Medico(id_med, especialidad, nombre_apellido))
        return medicos

    def obtener_horarios_medico(self):
        horarios = []
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = "SELECT fecha, hora FROM horarios WHERE id_med = %s"
            cursor.execute(query, (self.id_med,))
            horarios = cursor.fetchall()
        return horarios

    @staticmethod
    def agregar_horario_turno(id_med, fecha, hora):
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = "INSERT INTO horarios (fecha, hora, id_med) VALUES (%s, %s, %s)"
            cursor.execute(query, (fecha, hora, id_med))
            conexion.con.commit()

# Usage example for obtaining medicos
# medicos = Medico.obtener_medicos()
# for medico in medicos:
#     print(f"Medico: {medico.nombre_apellido}, Especialidad: {medico.especialidad}")

# Usage example for obtaining horarios for a specific medico
# if medicos:
#     horarios = medicos[0].obtener_horarios_medico()
#     for fecha, hora in horarios:
#         print(f"Fecha: {fecha}, Hora: {hora}")

from conexion import ConexionBD
 
class DatosTurnos:
    def __init__(self, id_med="", nombre_medico="", especialidad="", fecha="", hora=""):
        self.id_med = id_med
        self.nombre_medico = nombre_medico
        self.especialidad = especialidad
        self.fecha = fecha
        self.hora = hora

    @staticmethod
    def obtener_especialidades():
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = "SELECT DISTINCT especialidad FROM turnos ORDER BY especialidad"
            cursor.execute(query)
            especialidades = cursor.fetchall()
            return [especialidad[0] for especialidad in especialidades]

    @staticmethod
    def obtener_todos_los_medicos_con_especialidades():
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = "SELECT id_med, nombre_medico, especialidad FROM turnos"
            cursor.execute(query)
            medicos = cursor.fetchall()
            medicos_info = {
                medico[0]: {"nombre_medico": medico[1], "especialidad": medico[2]}
                for medico in medicos
            }
            return medicos_info

    @staticmethod
    def obtener_datos_turnos():
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = (
                "SELECT id_med, nombre_medico, especialidad, fecha, hora FROM turnos"
            )
            cursor.execute(query)
            turnos = cursor.fetchall()
            return turnos

    @staticmethod
    def obtener_nombres_medicos():
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = "SELECT DISTINCT nombre_medico FROM turnos ORDER BY nombre_medico"
            cursor.execute(query)
            return [item[0] for item in cursor.fetchall()]

    @staticmethod
    def obtener_disponibilidad_medico(nombre_medico):
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = """
            SELECT fecha, hora 
            FROM turnos 
            WHERE nombre_medico = %s
            AND fecha >= CURDATE()  # Assuming you want to filter out past dates
            ORDER BY fecha, hora
            """
            cursor.execute(query, (nombre_medico,))
            return cursor.fetchall()

    @staticmethod
    def obtener_fechas_disponibles(nombre_medico):
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = """
            SELECT DISTINCT fecha 
            FROM turnos 
            WHERE nombre_medico = %s AND fecha >= CURDATE() AND id_usuario IS NULL
            ORDER BY fecha;
            """
            cursor.execute(query, (nombre_medico,))
            return [fecha[0] for fecha in cursor.fetchall()]

    @staticmethod
    def obtener_horas_disponibles(nombre_medico, fecha):
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = """
            SELECT DISTINCT hora
            FROM turnos
            WHERE nombre_medico = %s AND fecha = %s AND id_usuario IS NULL
            ORDER BY hora;
            """
            cursor.execute(query, (nombre_medico, fecha))
            horas = cursor.fetchall()
            return [hora[0] for hora in horas]


    @staticmethod
    def obtener_especialidad_por_medico(nombre_medico):
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor(buffered=True)
            query = """
            SELECT especialidad
            FROM turnos
            WHERE nombre_medico = %s;
            """
            cursor.execute(query, (nombre_medico,))
            result = cursor.fetchone()
            return result[0] if result else ""

    @staticmethod
    def obtener_medicos_por_especialidad(especialidad):
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            # This might need adjustment depending on your actual database schema.
            query = """
            SELECT DISTINCT nombre_medico
            FROM turnos
            WHERE especialidad = %s
            ORDER BY nombre_medico;
            """
            cursor.execute(query, (especialidad,))
            medicos = cursor.fetchall()
            return [medico[0] for medico in medicos]

    @staticmethod
    def reservar_turno(nombre_medico, especialidad, fecha, hora, id_usuario):
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = """
            UPDATE turnos 
            SET id_usuario = %s 
            WHERE nombre_medico = %s
            AND especialidad = %s
            AND fecha = %s
            AND hora = %s;
            """

            cursor.execute(
                query, (id_usuario, nombre_medico, especialidad, fecha, hora)
            )
            conexion.con.commit()
            return True

    @staticmethod
    def obtener_turnos_usuario(id_usuario):
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = """
            SELECT id_med, nombre_medico, especialidad, fecha, hora
            FROM turnos
            WHERE id_usuario = %s
            ORDER BY fecha, hora;
            """
            cursor.execute(query, (id_usuario))
            return cursor.fetchall()
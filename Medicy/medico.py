from conexion import ConexionBD


class DatosTurnos:
    def __init__(self, id_med='', nombre_apellido='', especialidad='', fecha ='', hora=''):
        self.id_med = id_med
        self.nombre_apellido = nombre_apellido
        self.especialidad = especialidad
        self.fecha = fecha
        self.hora = hora


    @staticmethod
    def obtener_datos_turnos():
       
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = "SELECT id_med, nombre_apellido, especialidad, fecha, hora FROM turnos"
            cursor.execute(query)
            turnos = cursor.fetchall()
            conexion.con.commit()
            
            return turnos





import mysql.connector

class ConexionBD:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=""
        )
        self.cursor = self.con.cursor()     
    
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS bd_medicy")
        self.cursor.execute("USE bd_medicy")

        # Crea la tabla de medicos si no existe
        sql_medicos = ("""
        CREATE TABLE IF NOT EXISTS medicos (
            id_med INT AUTO_INCREMENT PRIMARY KEY,
            especialidad VARCHAR(45),
            nombre_apellido VARCHAR(45)
        )
        """)
        self.cursor.execute(sql_medicos)

        # Crea la tabla de horarios si no existe
        sql_horarios = ("""
        CREATE TABLE IF NOT EXISTS horarios (
            fecha DATE,
            hora TIME,
            id_med integer,
            FOREIGN KEY(id_med) REFERENCES medicos(id_med)
          
        )
        """)
        self.cursor.execute(sql_horarios)

        sql_turnos=(""" INSERT INTO medicos (nombre_apellido, especialidad) VALUES 
    ('Juan Pérez', 'Pediatría'),
    ('María García', 'Ginecología'),
    ('Carlos López', 'Clínico'),
    ('Ana Martínez', 'Dermatología'),
    ('Luis Rodríguez', 'Oftalmología'); 


""")
        self.cursor.execute(sql_turnos)

        sql_horario_turnos=("""INSERT  horarios (fecha, hora, id_med) VALUES
    ('2024-03-15', '10:00', 1),
    ('2024-03-16', '14:30', 1),
    ('2024-03-17', '09:00', 3),
    ('2024-03-18', '11:15', 4),
    ('2024-03-19', '16:45', 2),
    ('2024-03-20', '08:30', 1),
    ('2024-03-21', '13:00', 2),
    ('2024-03-22', '15:45', 2),
    ('2024-03-23', '12:30', 4),
    ('2024-03-24', '17:00', 3),
    ('2024-03-21', '13:00', 4),
    ('2024-03-22', '15:45', 3),
    ('2024-03-23', '12:30', 5),
    ('2024-03-24', '17:00', 1)

""")

        self.cursor.execute(sql_horario_turnos)

        self.con.commit()

    def cerrar_conexion(self):
        self.con.close()

conexion = ConexionBD()

conexion.cerrar_conexion()

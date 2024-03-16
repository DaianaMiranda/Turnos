import mysql.connector
from mysql.connector import Error

class ConexionBD:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database=""
            )
            if self.con.is_connected():
                self.cursor = self.con.cursor()
                self.setup_database()
        except Error as e:
            print("Error while connecting to MySQL", e)

    def setup_database(self):
        # Create database if not exists
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS bd_medicy")
        self.cursor.execute("USE bd_medicy")

        # Create tables if not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                apellido VARCHAR(255) NOT NULL,
                contraseña VARCHAR(255) NOT NULL,
                correo_electronico VARCHAR(255) NOT NULL UNIQUE,
                telefono VARCHAR(255) NOT NULL
            )
          """)
        
        self.cursor.execute("""
             CREATE TABLE IF NOT EXISTS turnos (
                id_med INT,
                nombre_medico VARCHAR(255),
                especialidad VARCHAR(255),
                fecha DATE,
                hora TIME,
                id_usuario INT,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
            )
        """)                                 


        # Add initial data if needed
        self.initialize_data()

        self.con.commit()

    def initialize_data(self):
        self.cursor.execute("""
            INSERT INTO turnos (id_med, nombre_medico, especialidad, fecha, hora) VALUES
            (1, 'Juan Pérez', 'Pediatría', '2024-03-15', '10:00'),
            (1, 'Juan Pérez', 'Pediatría', '2024-03-16', '14:30'),
            (3, 'Pablo Martínez', 'Pediatría', '2024-03-17', '09:00'),
            (4, 'Laura Sánchez', 'Ginecología', '2024-03-18', '11:15'),
            (2, 'María González', 'Pediatría', '2024-03-19', '16:45'),
            (1, 'Juan Pérez', 'Pediatría', '2024-03-20', '08:30'),
            (2, 'María González', 'Pediatría', '2024-03-21', '13:00'),
            (2, 'María González', 'Pediatría', '2024-03-22', '15:45'),
            (4, 'Laura Sánchez', 'Ginecología', '2024-03-23', '12:30'),
            (3, 'Pablo Martínez', 'Pediatría', '2024-03-24', '17:00'),
            (4, 'Laura Sánchez', 'Ginecología', '2024-03-21', '13:00'),
            (3, 'Pablo Martínez', 'Pediatría', '2024-03-22', '15:45'),
            (5, 'Roberto García', 'Clínico', '2024-03-23', '12:30'),
            (1, 'Juan Pérez', 'Pediatría', '2024-03-24', '17:00');
                            
        """)


    # def initialize_data(self):
    #     self.cursor.execute("SELECT COUNT(*) FROM medicos")
    #     if self.cursor.fetchone()[0] == 0:
    #         # If no records exist, insert the initial data
    #         self.cursor.execute("""
    #             INSERT INTO medicos (nombre_apellido, especialidad) VALUES
    #             (('Juan Pérez', 'Pediatría'), ('María González', 'Pediatría'), ('Pablo Martínez', 'Pediatría')),
    #             (('Laura Sánchez', 'Ginecología'), ('Ana Rodríguez', 'Ginecología'), ('Carlos Fernández', 'Ginecología')),
    #             (('Roberto García', 'Clínico'), ('Marta López', 'Clínico'), ('Javier Ruiz', 'Clínico')),
    #             (('María Fernández', 'Dermatología'), ('José Martínez', 'Dermatología'), ('Elena Gómez', 'Dermatología')),
    #             (('David Pérez', 'Oftalmología'), ('Sandra Rodríguez', 'Oftalmología'), ('Francisco Ruiz', 'Oftalmología'));
    #         """)
    #         self.cursor.execute("""
    #             INSERT INTO turnos (fecha, hora, id_med) VALUES
    #             ('2024-03-15', '10:00', 1),
    #             ('2024-03-16', '14:30', 1),
    #             ('2024-03-17', '09:00', 3),
    #             ('2024-03-18', '11:15', 4),
    #             ('2024-03-19', '16:45', 2),
    #             ('2024-03-20', '08:30', 1),
    #             ('2024-03-21', '13:00', 2),
    #             ('2024-03-22', '15:45', 2),
    #             ('2024-03-23', '12:30', 4),
    #             ('2024-03-24', '17:00', 3),
    #             ('2024-03-21', '13:00', 4),
    #             ('2024-03-22', '15:45', 3),
    #             ('2024-03-23', '12:30', 5),
    #             ('2024-03-24', '17:00', 1)
    #         """)

    def query(self, sql, params=None):
        with self.con.cursor() as cursor:
            cursor.execute(sql, params or ())
            return cursor.fetchall()

    def execute(self, sql, params=None):
        with self.con.cursor() as cursor:
            cursor.execute(sql, params or ())
            self.con.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cerrar_conexion()

    def cerrar_conexion(self):
        if self.con.is_connected():
            self.cursor.close()
            self.con.close()


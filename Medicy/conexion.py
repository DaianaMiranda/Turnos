import mysql.connector
from mysql.connector import Error

class ConexionBD:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="bd_medicy"
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
            CREATE TABLE IF NOT EXISTS medicos (
                id_med INT AUTO_INCREMENT PRIMARY KEY,
                especialidad VARCHAR(45),
                nombre_apellido VARCHAR(45)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                apellido VARCHAR(255) NOT NULL,
                contraseña VARCHAR(255) NOT NULL,
                correo_electronico VARCHAR(255) NOT NULL UNIQUE,
                telefono VARCHAR(255) NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS horarios (
                fecha DATE,
                hora TIME,
                id_med INT,
                FOREIGN KEY(id_med) REFERENCES medicos(id_med)
            )
        """)

        # Add initial data if needed
        self.initialize_data()

        self.con.commit()

    def initialize_data(self):
        self.cursor.execute("SELECT COUNT(*) FROM medicos")
        if self.cursor.fetchone()[0] == 0:
            # If no records exist, insert the initial data
            self.cursor.execute("""
                INSERT INTO medicos (nombre_apellido, especialidad) VALUES 
                ('Juan Pérez', 'Pediatría'), 
                ('María García', 'Ginecología'), 
                ('Carlos López', 'Clínico'), 
                ('Ana Martínez', 'Dermatología'), 
                ('Luis Rodríguez', 'Oftalmología');
            """)
            self.cursor.execute("""
                INSERT INTO horarios (fecha, hora, id_med) VALUES
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

# Example usage:
# with ConexionBD() as conexion:
#     results = conexion.query("SELECT * FROM medicos")
#     for row in results:
#         print(row)

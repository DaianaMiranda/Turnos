import mysql.connector
from mysql.connector import Error

# Define una clase para manejar la conexión a la base de datos
class ConexionBD:
    def __init__(self):
        try:
            #  Se intenta establecer la conexion con MySQL
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database=""
            )
            
            if self.con.is_connected():
                # Crea un cursor para ejecutar consultas SQL
                self.cursor = self.con.cursor()
                # Configura la base de datos y las tablas
                self.setup_database()
        # Captura cualquier error que pueda ocurrir durante la conexion
        except Error as e:
            print("Error while connecting to MySQL", e)

    # Metodo para configurar la base de datos y las tablas
    def setup_database(self):
      
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS bd_medicy")
        self.cursor.execute("USE bd_medicy")

       
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


        # Agrega datos iniciales si es necesario
        self.initialize_data()

        # Confirmamos los cambios 
        self.con.commit()

    # Metodo para agregar datos iniciales a la tabla turnos
    def initialize_data(self):
        # Verifica si la tabla turnos esta vacia
        self.cursor.execute("SELECT COUNT(*) FROM turnos")
        # Si la tabla esta vacia, insertamos datos iniciales
        if self.cursor.fetchone()[0] == 0:  
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

    # Metodo para ejecutar consultas SELECT
    def query(self, sql, params=None):
        with self.con.cursor() as cursor:
            cursor.execute(sql, params or ())
            return cursor.fetchall()

    # Metodo para ejecutar consultas que modifican la base de datos
    def ejecutar(self, sql, params=None):
        with self.con.cursor() as cursor:
            cursor.execute(sql, params or ())
            
            self.con.commit()

    # Metodo llamado cuando se utiliza la instancia de la clase en un contexto "with"
    def __enter__(self):
        return self

    # Metodo llamado al salir del contexto "with"
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cerrar_conexion()

    # Metodo para cerrar la conexión con la base de datos
    def cerrar_conexion(self):
        if self.con.is_connected():
            self.cursor.close()
            self.con.close()

from conexion import ConexionBD 
# import mysql.connector

class Usuario:
    def __init__(self, nombre, contra, apellido="", telefono="", correo=""):
        self.nombre = nombre
        self.contra = contra
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.conectado = False

    @staticmethod
    def crear_usuario(nombre, contra, apellido="", telefono="", correo=""):
        
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = """INSERT INTO usuarios (nombre, apellido, telefono, correo_electronico, contraseña) 
                       VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query, (nombre, apellido, telefono, correo, contra))
            conexion.con.commit()
            print("Usuario creado con éxito")

    def conectar(self):
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            query = "SELECT contra FROM usuarios WHERE nombre = %s"
            cursor.execute(query, (self.nombre,))
            result = cursor.fetchone()
            if result and result[0] == self.contra:
                print("Se ha conectado con éxito")
                self.conectado = True
            else:
                print("Contraseña incorrecta, inténtelo de nuevo.. ")

    @classmethod
    def verificar_credenciales(cls, nombre, contraseña):
        with ConexionBD() as conexion:
            cursor = conexion.con.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE nombre = %s AND contraseña = %s", (nombre, contraseña))
            result = cursor.fetchone()
            return result is not None
        
    def desconectar(self):
        if self.conectado:
            print("Se cerró la sesión correctamente")
            self.conectado = False
        else:
            print("Error, sesión no iniciada")

    def __str__(self):
        conect = "conectado" if self.conectado else "desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {conect}"

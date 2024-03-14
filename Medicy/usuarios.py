
class usuario():
    numUsers = 0
    pass
    
    def __init__(self,nombre,contra):
        self.nombre = nombre
        self.contraseña = contra
        self.conectado = False
        self.intentos = ""

        usuario.numUsers+=1

    def conectar(self):
        myPass = input("Ingrese contraseña: ")    
        if myPass==self.contra:
            print("Se ha conectado con exito")
            self.conectado = True
        else:
            print("Contraseña incorrecta, intentelo de nuevo.. ")

    def desconectar(self):
        if self.conectado:
            print("Se cerro la sesion correctamente")
            self.conectado = False
        else:
            print("Error, sesion no iniciada")

    def __str__(self):
        if self.conectado:
            conect = "conectado"
        else:
            conect = "desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {conect}"
user1 = usuario(input("Ingrese un nombre: "), input("Ingrese una contraseña: "))
print(user1)
user1.conectar()
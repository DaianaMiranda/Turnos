from tkinter import *
from tkinter import messagebox
import pymysql
from registro import *

def registro_datos():
    miConexion=pymysql.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="bd_medicy")

    
    miCursor= miConexion.cursor()
    
    sql = "INSERT INTO registros(nombre, apellido, telefono, correo_electronico , contraseña) VALUES ('{0}', '{1}','{2}','{3}','{4}')".format(nombreTexto.get(), apellidoTexto.get(), telefonoTexto.get(),correoTexto.get(), contraseñaTexto.get())

    try:
        miCursor.execute(sql)
        miConexion.commit()
        messagebox.showinfo(message = "Registro Exitoso" , title= "Aviso")

    except:
        miConexion.rollback()
        messagebox.showinfo(message = " Error" , title = "Aviso")

    miConexion.close()

registro_datos()





# def registro_datos():
#     miConexion=pymysql.connect(
#                             host="localhost",
#                             user="root",
#                             password="",
#                             database="bd_medicy")

    
#     miCursor= miConexion.cursor()
    
#     sql = "INSERT INTO registros(nombre, apellido, telefono, correo_electronico, contraseña) VALUES ('{0}', '{1}','{2}','{3}','{4}')".format(nombreTexto.get(), apellidoTexto.get(), telefonoTexto.get(),correoTexto.get(), contraseñaTexto.get())

#     try:
#         miCursor.execute(sql)
#         miConexion.commit()
#         messagebox.showinfo(message = "Registro Exitoso" , title= "Aviso")

#     except pymysql.Error as error:
#         messagebox.showerror(message="Error al registrar en la base de datos: " + str(error), title="Aviso")
#         # miConexion.rollback()
#         # messagebox.showinfo(message = " Error" , title = "Aviso")

#     miConexion.close()


# def verificar_correo():
#     if correoTexto.contains("@"):
#         print("El correo electrónico contiene '@'.")
#     else:
#         print("El correo electrónico no contiene '@'.") 

# def abrir_turno():
#     ventana2.destroy()  # Cierra la ventana actual
#     os.system("python turno.py")  # Ejecuta el  archivo turno

# def volver():
#     ventana2.destroy()  # Cierra la ventana actual
#     os.system("python index.py")  # Ejecuta el  index


# ventana registro
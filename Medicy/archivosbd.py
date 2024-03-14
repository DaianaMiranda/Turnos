from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import messagebox
import pymysql


def insertar_datos():
    miConexion=pymysql.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="bd_medicy")

    
    miCursor= miConexion.cursor()
    
    sql = "SELECT  FROM login(usuario, contraseña) "

    try:
        miCursor.execute(sql)
        miConexion.commit()
        messagebox.showinfo(message = "Conexion Exitosa" , title= "Aviso")

    except:
        miConexion.rollback()
        messagebox.showinfo(message = " Error" , title = "Aviso")

    miConexion.close()






def abrir_registro():
     ventana.destroy() # Cierra la ventana actual
     os.system("python registro.py")  # Ejecuta registro


ventana= Tk()
ventana.geometry("1000x800")
ventana.title("Medicy")
ventana.resizable(False,False)
ventana.config(bg="#DDF7F5")
ventana.config(cursor="plus")

margen= Frame()
margen.pack()
margen.config(bg="#DDF7F5")
margen.config(width="30", height="30")

    # logo
    # imagen=ImageTk.PhotoImage(Image.open("img/salud.png"))
    # label_imagen=Label(image=imagen)
    # label_imagen.pack()


miFrame= Frame()
miFrame.pack()
miFrame.config(bg="#DDF7F5")
miFrame.config(width="10", height="10")

titulo=Label(miFrame, text="MEDICY", bg="#DDF7F5", fg="pink", width="100", height="3", font=("Arial Black",15)).pack()

framel=LabelFrame(ventana, text="Login", width=300, height=50, padx=50, pady=10)
framel.config(bg="#DDF7F5")
framel.pack()

userLabel= Label(framel, text= "Usuario: ")
userLabel.grid(row=1, column=0, sticky="w")
userLabel.config(fg="black", bg="white" )
userTexto = Entry(framel)
userTexto.grid(row=1, column=1,padx=10, pady=10)
userTexto.config(fg="black", bg="white" )

passLabel= Label(framel, text= "pass : ")
passLabel.grid(row=2, column=0, sticky="w")
passLabel.config(fg="black", bg="white")
passTexto= Entry(framel)
passTexto.grid(row=2, column=1, padx=50, pady=10,)
passTexto.config(fg="black", bg="white")

    # botones
btn_login=Button(framel, text="Iniciar Sesion ", command= insertar_datos)
btn_login.config(bg="#C1E2F3")
btn_login.grid(row=3,column=1, )


btn_registro=Button(framel, text="Registrarse ",command=abrir_registro )
btn_registro.config(bg="#F9DBED")
btn_registro.grid(row=5,column=1, padx=10, pady=10)

mainloop()


    




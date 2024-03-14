from tkinter import *
from PIL import ImageTk, Image


class Ventana():
    def fondo():
        ventana1 = Tk()
        ventana1.geometry("700x600")
        ventana1.title("Medicy")
        ventana1.resizable(False, False)
        ventana1.config(bg="#DDF7F5")
        ventana1.config(cursor="plus")

        margen = Frame(ventana1)
        margen.pack()
        margen.config(bg="#DDF7F5")
        margen.config(width="30", height="30")

        imagen = Image.open("img/salud.png")
        imagen = imagen.resize((100, 100))
        imagen = ImageTk.PhotoImage(imagen)
        label_imagen = Label(ventana1, image=imagen)
        label_imagen.image = imagen
        label_imagen.pack()


        miFrame = Frame(ventana1)
        miFrame.pack()
        miFrame.config(bg="#DDF7F5")
        miFrame.config(width="10", height="10")

        titulo = Label(miFrame, text="MEDICY", bg="#DDF7F5", fg="pink", width="100", height="3", font=("Arial Black", 15))
        titulo.pack()

        
        return (ventana1)
import tkinter as tk
from PIL import Image, ImageTk
from login import Login
from register import Register
from solicitud_turnos import SolicitudTurnos
from lista_turnos import MostrarTurnos
from medico import DatosTurnos

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Medicy')
        self.geometry('700x600')
        self.resizable(False, False)
        self.id_usuario = None
        self.datos_turnos = DatosTurnos()
        # Persistent background or elements
        self.configure(bg="#DDF7F5")
        
        # Frame for navigable content
        self.content_frame = tk.Frame(self, bg="#DDF7F5")
        # Load and place a persistent image
        self.place_persistent_image()
        self.content_frame.pack(fill="both", expand=True)
        

        self.frames = {}
        for F in (Login, Register, SolicitudTurnos, MostrarTurnos):
            frame = F(parent=self.content_frame, controller=self)
            self.frames[F.__name__] = frame
            self.content_frame.grid_rowconfigure(0, weight=1)
            self.content_frame.grid_columnconfigure(0, weight=1)
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if page_name == "MostrarTurnos":
            if self.id_usuario is not None:
                frame.reset_state()
                frame.cargar_turnos_usuario()
        frame.tkraise()
    
    def place_persistent_image(self):
        image = Image.open("img/salud.png").resize((100, 100))
        photo_image = ImageTk.PhotoImage(image)
        self.label_image = tk.Label(self, image=photo_image, bg="#DDF7F5")
        self.label_image.image = photo_image 
        self.label_image.pack(side="top") 

if __name__ == "__main__":
    app = App()
    app.mainloop()

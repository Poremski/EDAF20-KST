from . import configurations
from . import controller
try:
    from Tkinter import *
    from Tkinter.ttk import *
except:
    from tkinter import *
    from tkinter import *


class View(Frame):
    """
    Vy:   Klassen hanterar element som kretsar kring användargränssnittet.
          -- Kontrollern kan skicka meddelanden till Vyn.
          -- Vyn kan anropa metoder i Kontrollern när en händelse inträffar.
          -- Vyn kommunicerar ALDRIG med Modellen.
          -- Vyn har setters och getters som den använder för att kommunicerar 
             med Kontrollern.
    """
    def __init__(self, vc):
        self.vc = vc
        self.frame = Frame()
        self.frame.grid(row = 0, column = 0)
        self.load_view()

    def load_view(self):
        pass

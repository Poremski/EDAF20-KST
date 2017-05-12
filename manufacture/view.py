from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


class View():
    """
    Vy:   Klassen hanterar element som kretsar kring användargränssnittet.
          -- Kontrollern kan skicka meddelanden till Vyn.
          -- Vyn kan anropa metoder i Kontrollern när en händelse inträffar.
          -- Vyn kommunicerar ALDRIG med Modellen.
          -- Vyn har setters och getters som den använder för att kommunicerar 
             med Kontrollern.
    """
    def __init__(self, vc, parent):
        self.vc = vc  # delegate/callback pointer

        self.main_frame = Frame(parent)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.notebook = Notebook(self.main_frame)
        self.notebook.pack(fill=BOTH, expand=True)

        self.listbox_blocked = Listbox()

        self.blocked_var = []
        self.blocked_value = StringVar()

        self.widget_blocked_pallets()

    def widget_blocked_pallets(self):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text='Blockerade pallar')

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox_blocked.__init__(frame)
        self.listbox_blocked.pack(fill=BOTH, expand=True)

        scrollbar.config(command=self.listbox_blocked)

    def set_list_blocked(self, list):
        self.blocked_var = list
        for b in self.blocked_var:
            self.listbox_blocked.insert(END, 'Barcode: ' + str(b))

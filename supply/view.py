from .configurations import *
from .controller import *
from tkinter import *
from tkinter.ttk import *


class View(Frame):
    """
    Vy:   Klassen hanterar element som kretsar kring användargränssnittet.
          -- Kontrollern kan skicka meddelanden till Vyn.
          -- Vyn kan anropa metoder i Kontrollern när en händelse inträffar.
          -- Vyn kommunicerar ALDRIG med Modellen.
          -- Vyn har setters och getters som den använder för att kommunicerar 
             med Kontrollern.
    """
    def __init__(self, vc, parent, recipes):
        self.vc = vc  # delegate/callback pointer

        self.main_frame = Frame(parent)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.notebook = Notebook(self.main_frame)
        self.notebook.pack(fill=BOTH, expand=True)

        self.recipes_var = recipes

        self.widget_recipes()
        # self.widget_config()

    def widget_recipes(self):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text='Recept')

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        tree = Treeview(frame, yscrollcommand=scrollbar.set)
        tree['columns'] = ('A', 'B')
        tree.column('A', width=200)
        tree.column('B', width=50)
        tree.heading('A', text='Ingrediens')
        tree.heading('B', text='Mängd')
        tree.pack(fill=BOTH, expand=True)

        scrollbar.config(command=tree.yview)


        last_product = 0
        for value in self.recipes_var:
            if value[0] is not last_product:
                tree.insert("", value[0], value[0], text=value[1])
                last_product = value[0]
            tree.insert(value[0], value[0], '', values=(value[2], '%s %s' % (str(value[3]), value[4])))




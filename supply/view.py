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
        self.products_var = dict()
        self.ingredients_var = dict()
        self.units_var = dict()

        self.widget_recipes()
        self.widget_config()

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

    def widget_config(self):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text='Administration')

        self.widget_config_delete_product(frame)
        self.widget_config_delete_recipe(frame)
        self.widget_config_add_product(frame)
        self.widget_config_add_ingredient(frame)
        self.widget_config_add_ingredient_to_product(frame)

    def widget_config_delete_product(self, frame):
        p = Panedwindow(frame, orient=VERTICAL)
        f = Labelframe(p, text='Ta bort produkt')
        p.add(f)
        Label(f, text='Produkt:').pack(side=LEFT)
        Button(f, text='Ta bort').pack(side=RIGHT)
        v_var = StringVar()
        v = Combobox(f, textvariable=v_var, state='readonly')
        v['values'] = sorted(list({1:1}))
        v.pack(side=RIGHT, fill=X, expand=TRUE)
        p.pack(side=TOP, anchor=W, fill=X, expand=NO)

    def widget_config_delete_recipe(self, frame):
        p = Panedwindow(frame, orient=VERTICAL)
        f = Labelframe(p, text='Ta bort recept')
        p.add(f)
        Label(f, text='Recept:').pack(side=LEFT)
        Button(f, text='Ta bort').pack(side=RIGHT)
        v_var = StringVar()
        v = Combobox(f, textvariable=v_var, state='readonly')
        v['values'] = sorted(list({1: 1}))
        v.pack(side=RIGHT, fill=X, expand=TRUE)
        p.pack(side=TOP, anchor=W, fill=X, expand=NO)

    def widget_config_add_product(self, frame):
        p = Panedwindow(frame, orient=VERTICAL)
        f = Labelframe(p, text='Lägg till produkt')
        p.add(f)

        Label(f, text='Produkt:').pack(side=LEFT)
        Button(f, text='Lägg till').pack(side=RIGHT)
        Entry(f).pack(side=RIGHT, fill=X, expand=TRUE)

        p.pack(side=TOP, anchor=W, fill=X, expand=NO)

    def widget_config_add_ingredient(self, frame):
        p = Panedwindow(frame, orient=VERTICAL)
        f = Labelframe(p, text='Lägg till ingrediens')
        p.add(f)

        Label(f, text='Ingrediens:').pack(side=LEFT)
        Button(f, text='Lägg till').pack(side=RIGHT)
        Entry(f).pack(side=RIGHT, fill=X, expand=TRUE)

        p.pack(side=TOP, anchor=W, fill=X, expand=NO)

    def widget_config_add_ingredient_to_product(self, frame):
        p = Panedwindow(frame, orient=VERTICAL)
        f = Labelframe(p, text='Lägg till ingrediens till produkt')
        p.add(f)

        #####

        p.pack(side=TOP, anchor=W, fill=X, expand=NO)




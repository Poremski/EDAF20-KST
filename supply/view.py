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

        self.tree = Treeview()

        self.products_var = []
        self.recipes_var = []
        self.ingredients_var = []
        self.units_var = []

        self.products_form = Combobox()
        self.products_value = StringVar()

        self.ingredients_form = Combobox()
        self.ingredients_value = StringVar()

        self.widget_recipes()
        self.widget_config()

    def showerror(self, title, message):
        messagebox.showerror(title, message)

    def set_recipes_var(self, recipes):
        self.recipes_var = recipes
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.tree_recipes()

    def get_recipes_var(self):
        return self.recipes_var

    def set_products_var(self, products):
        self.products_var = products
        list = []
        for value in self.get_products_var():
            list += ['(art.nr. %s) %s' % (value[0], value[1])]
        if len(list) > 0:
            self.products_form['values'] = list
        else:
            self.products_form['values'] = ['']
        self.products_form.current(0)

    def get_products_var(self):
        return self.products_var

    def set_ingredients_var(self, ingredients):
        self.ingredients_var = ingredients
        list = []
        for value in self.get_ingredients_var():
            list += ['(art.nr. %s) %s' % (value[0], value[1])]
        if len(list) > 0:
            self.ingredients_form['values'] = list
        else:
            self.ingredients_form['values'] = ['']
        self.ingredients_form.current(0)

    def get_ingredients_var(self):
        return self.ingredients_var

    def set_units_var(self, units):
        self.units_var = units

    def get_units_var(self):
        return self.units_var

    def widget_recipes(self):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text='Recept')

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.tree.__init__(frame, yscrollcommand=scrollbar.set)
        self.tree['columns'] = ('A', 'B')
        self.tree.column('A', width=200)
        self.tree.column('B', width=100)
        self.tree.heading('A', text='Ingrediens')
        self.tree.heading('B', text='Mängd')
        self.tree.pack(fill=BOTH, expand=True)

        self.tree_recipes()

        scrollbar.config(command=self.tree.yview)

    def tree_recipes(self):
        last_product = 0
        for value in self.get_recipes_var():
            if value is not None:
                if value[0] is not last_product:
                    self.tree.insert("", value[0], value[0], text=value[1])
                    last_product = value[0]
                self.tree.insert(value[0], value[0], '', values=(value[2], '%s %s' % (str(value[3]), value[4])))

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
        Button(f, text='Ta bort', command=self.vc.btn_delete_product).pack(side=RIGHT)
        self.products_form.__init__(f, textvariable=self.products_form, values=self.products_var, state='readonly')
        self.products_form.pack(side=RIGHT, fill=X, expand=TRUE)
        p.pack(side=TOP, anchor=W, fill=X, expand=NO)

    def widget_config_delete_recipe(self, frame):
        p = Panedwindow(frame, orient=VERTICAL)
        f = Labelframe(p, text='Ta bort ingrediens')
        p.add(f)
        Label(f, text='Ingrediens:').pack(side=LEFT)
        Button(f, text='Ta bort', command=self.vc.btn_delete_ingredient).pack(side=RIGHT)
        self.ingredients_form.__init__(f, textvariable=self.ingredients_form, state='readonly')
        self.ingredients_form.pack(side=RIGHT, fill=X, expand=TRUE)
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




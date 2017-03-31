#!/usr/bin/env python3
from tkinter import *
from tkinter.ttk import *
from .model import Model
import platform
import os


class View(object):
    """
    Vynivån.
    """
    def __init__(self, master, debug=False):
        """
        Konstruktorn för vynivån.
        Argument:
            master: Tar in ett Tk()-objekt
        """
        self.master = master
        self.debug = debug
        self.master.title('Krustys övervakningsverktyg')
        self.menu()
        self.model = Model()
        self.notebook()

    def menu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label='Arkiv', menu=file_menu)

        if platform.system() in ['Windows', 'Linux']:
            help_menu = Menu(menu, tearoff=0)
            menu.add_cascade(label='Hjälp', menu=help_menu)
            help_menu.add_command(label='Om...', command=self.about_dlg)
        else:
            file_menu.add_command(label='Om...', command=self.about_dlg)
            file_menu.add_separator()
        file_menu.add_command(label='Avsluta', command=self.master.quit)

    def about_dlg(self):
        """
        Dialogfönstret "Om…"
        """
        about = Toplevel()
        about.title('Om Krustys övervakningsverktyg')
        about.resizable(FALSE, FALSE)
        about.geometry('+200+200')

        frame = Frame(about)
        frame.pack()

        with open(os.path.join(os.getcwd(), 'application/KST.base64'), 'r') as file:
            img_data = file.readlines()
       
        img = PhotoImage(data=img_data)
        logo = Label(frame, image=img)
        logo.image = img
        logo.grid(row=1, column=0)

        Label(frame, text='Krustys övervakningsverktyg').grid(row=0, columnspan=2)

        txtmsg = 'Detta program är utformat som en del av ett projekt i kursen Databasteknik (EDAF20) \n' \
                 'vid LTH Campus Helsingborg, där ett verktyg utifrån specifika funktionalitetsönskemål\n' \
                 'skulle implementeras.\n\n' \
                 'Genom den teoretiska kunskap vi har tillägnat oss under kursens gång, har vi kunnat \n' \
                 'tillämpa kunskapen praktiskt och utveckla programgränssnitt till en databas med \n' \
                 'efterfrågad funktionalitet.\n\n' \
                 'Vi har genom detta därmed uppnått de mål som uttrycks i kursplanen för den berörda \n' \
                 'kursen.\n\n' \
                 'De involverade i projektet:\n     Javier Poremski och Simon Farre\n' \
                 'Datum:\n     2017-03-31'

        Label(frame, text=txtmsg).grid(row=1, column=1)

        Button(frame, text='Stäng', command=about.destroy).grid(row=2, columnspan=2)

    def notebook(self):
        """
        Renderar ut flik-komponenter för att representera lager-, produktions- 
        och leveransenheten genom att användaren klickar på respektive flik.
        Om debug är True, renderas även en Debug-flik.
        """
        notebook = Notebook(self.master)
        notebook.pack(fill=BOTH, expand=True)
        title = ['Lagerenheten', 'Produktionsenheten', 'Leveransenheten']
        if self.debug is True:
            title += ['Debug']
        for i in range(len(title)):
            frame = Frame(notebook)
            notebook.add(frame, text=title[i])
            self.set_unit_frame(title[i], frame)

    def set_unit_frame(self, unit, frame):
        """
        Returnerar efterfrågan flik-komponent
        Argument:
            unit:   Sträng av motsvarades 'Lagerenheten', 'Produktionsenheten', 
                    'Leveransenheten' eller 'Debug'.
            frame:  Referens till underliggande framelager

        Returnerar: Returnerar metod som renderar efterfrågad filk-komponent.

        """
        if unit is 'Lagerenheten': self.supply_unit(frame)
        elif unit is 'Produktionsenheten': self.production_unit(frame)
        elif unit is 'Leveransenheten': self.delivery_unit(frame)
        elif unit is 'Debug': self.debug_simulator(frame)
        else:
            raise AssertionError('FEL: Flik-komponenten är okänd i view.set_unit_frame().', unit)

    def supply_unit(self, frame):
        """
        Renderar tabb-vyn för lagerenheten.
        """
        notebook = Notebook(frame)
        notebook.pack(fill=BOTH, expand=True)

        frame1 = Frame(notebook)
        self.supply_unit_recipes_view(frame1)
        notebook.add(frame1, text='Recept')

        frame2 = Frame(notebook)
        self.supply_unit_recipes_edit(frame2)
        notebook.add(frame2, text='Ändra')

    def supply_unit_recipes_view(self, frame):
        """
        Renderar vyn för: Lagerenheten -> Recept.
        Args:
            frame:  Tar in underliggade vylager.
        """
        tree = Treeview(frame)
        tree['columns'] = ('A', 'B')
        tree.column('A', width=200)
        tree.column('B', width=50)
        tree.heading('A', text='Ingrediens')
        tree.heading('B', text='Mängd')

        recipes = self.model.get_recipes()
        last_product = 0
        for recipe in recipes:
            if last_product is not recipe[0]:
                tree.insert("", recipe[0], recipe[0], text=recipe[1])
                last_product = recipe[0]
            tree.insert(recipe[0], recipe[0], '', values=(recipe[2], '%s %s' % (str(recipe[3]), recipe[4])))

        tree.pack(fill=BOTH, expand=True)

    def supply_unit_recipes_edit(self, frame):
        """
        Renderar vyn för: Lagerenheten -> Ändra.
        Args:
            frame:  Tar in underliggande vylager.
        """
        self.supply_unit_recipes_edit_delete_product(frame)
        self.supply_unit_recipes_edit_delete_ingredient(frame)
        self.supply_unit_recipes_edit_add_product(frame)
        self.supply_unit_recipes_edit_add_ingredient(frame)
        self.supply_unit_recipes_edit_add_ingredient_to_product(frame)

    def supply_unit_recipes_edit_delete_product(self, frame):
        """
        Renderar formulärvyn för borttagnings av produkter.
        Args:
            frame: Tar in underliggande vylager.
        """
        p = Panedwindow(frame, orient=VERTICAL)
        f = Labelframe(p, text='Ta bort produkt')
        p.add(f)
        Label(f, text='Produkt:').pack(side=LEFT)
        btn = Button(f, text='Ta bort').pack(side=RIGHT)
        product_var = StringVar()
        products = Combobox(f, textvariable=product_var, state='readonly')
        product_dict = self.model.get_products()
        products['values'] = sorted(list(product_dict.values()))
        products.pack(side=RIGHT, fill=X, expand=TRUE)
        p.pack(fill=BOTH, expand=1)

    def supply_unit_recipes_edit_delete_ingredient(self, frame):
        """
        Renderar formulärvyn för borttagnings av ingredienser.
        Args:
            frame: Tar in underliggande vylager.
        """
        p = Panedwindow(frame, orient=VERTICAL)
        f = Labelframe(p, text='Ta bort ingrediens')
        p.add(f)
        Label(f, text='Ingrediens:').pack(side=LEFT)
        btn = Button(f, text='Ta bort').pack(side=RIGHT)
        ingredient_var = StringVar()
        ingredient = Combobox(f, textvariable=ingredient_var, state='readonly')
        ingredient_dict = self.model.get_ingredients()
        ingredient['values'] = sorted(list(ingredient_dict.values()))
        ingredient.pack(side=RIGHT, fill=X, expand=TRUE)
        p.pack(fill=BOTH, expand=1)

    def supply_unit_recipes_edit_add_product(self, frame):
        """
        Renderar formulärvyn för tilläggning av produkter.
        Args:
            frame: Tar in underliggande vylager.
        """
        p = Panedwindow(frame, orient=VERTICAL)
        f = Labelframe(p, text='Skapa produkt')
        p.add(f)
        Label(f, text='Produkt:').pack(side=LEFT)
        btn = Button(f, text='Lägg till').pack(side=RIGHT)
        product = Entry(f).pack(side=RIGHT, fill=X, expand=TRUE)
        p.pack(fill=BOTH, expand=1)

    def supply_unit_recipes_edit_add_ingredient(self, frame):
        """
        Renderar formulärvyn för tilläggning av ingredienser.
        Args:
            frame: Tar in underliggande vylager.
        """
        p = Panedwindow(frame, orient=VERTICAL)
        f = Labelframe(p, text='Skapa ingrediens')
        p.add(f)
        Label(f, text='Ingrediens:').pack(side=LEFT)
        btn = Button(f, text='Lägg till').pack(side=RIGHT)
        product = Entry(f).pack(side=RIGHT, fill=X, expand=TRUE)
        p.pack(fill=BOTH, expand=1)

    def supply_unit_recipes_edit_add_ingredient_to_product(self, frame):
        """
        Renderar formulärvyn för koppling av viss ingrediens till given produkt.
        Args:
            frame: Tar in underliggande vylager.
        """
        p = Panedwindow(frame, orient=VERTICAL)
        f = Labelframe(p, text='Lägg till ingrediens till produkt')
        p.add(f)

        p1 = PanedWindow(f)
        Label(p1, text='Produkt:').pack(side=LEFT)
        product_var = StringVar()
        products = Combobox(p1, textvariable=product_var, state='readonly')
        product_dict = self.model.get_products()
        products['values'] = sorted(list(product_dict.values()))
        products.pack(side=RIGHT, fill=X, expand=TRUE)
        p1.pack(fill=BOTH, expand=1)

        p2 = PanedWindow(f)
        Label(p2, text='Ingrediens:').pack(side=LEFT)
        ingredient_var = StringVar()
        ingredient = Combobox(p2, textvariable=ingredient_var, state='readonly')
        ingredient_dict = self.model.get_ingredients()
        ingredient['values'] = sorted(list(ingredient_dict.values()))
        ingredient.pack(side=RIGHT, fill=X, expand=TRUE)
        p2.pack(fill=BOTH, expand=1)

        p3 = PanedWindow(f)
        Label(p3, text='Mängd:').pack(side=LEFT)
        btn = Button(f, text='Lägg till').pack(side=RIGHT)
        unit_var = StringVar()
        units = Combobox(p3, textvariable=unit_var, state='readonly')
        units_dict = self.model.get_units()
        units['values'] = sorted(list(units_dict.keys()))
        units.pack(side=RIGHT)
        amount = Entry(p3).pack(side=RIGHT, fill=X, expand=TRUE)
        p3.pack(fill=BOTH, expand=1)

        p.pack(fill=BOTH, expand=1)


    def production_unit(self, master):
        """
        Renderar tabb-vyn för produktionsenheten.
        """
        None

    def delivery_unit(self, master):
        """
        Renderar tabb-vyn för leveransenheten.
        """
        None

    def debug_simulator(self, master):
        """
        Renderar tabb-vyn för simulatorn.
        """
        None

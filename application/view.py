from tkinter import *
from tkinter.ttk import *
from .model import Model


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
        self.model = Model()
        self.notebook()

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
        self.supply_unit_recipes(frame1)

        notebook.add(frame1, text='Recept')
        frame2 = Frame(notebook)
        notebook.add(frame2, text='Ändra')

    def supply_unit_recipes(self, frame):
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

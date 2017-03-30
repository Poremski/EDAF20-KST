from tkinter import *
from tkinter.ttk import *


class View(object):
    """
    Vynivån.
    """
    def __init__(self, master, debug=False):
        """
        Konstruktorn för vynivån.
        Args:
            master: Tar in ett Tk()-objekt
        """
        self.master = master
        self.debug = debug
        self.master.title('Krustys övervakningsverktyg')
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

    def supply_unit(self):
        """
        Renderar tabb-vyn för lagerenheten.
        """
        None

    def production_unit(self):
        """
        Renderar tabb-vyn för produktionsenheten.
        """
        None

    def delivery_unit(self):
        """
        Renderar tabb-vyn för leveransenheten.
        """
        None

    def simulation(self):
        """
        Renderar tabb-vyn för simulatorn.
        """
        None

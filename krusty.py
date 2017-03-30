#!/usr/bin/env python3.6
import sqlite3
from tkinter import *
from tkinter.ttk import *


class Controller(object):
    """
    Kontroller.
    """
    def __init__(self, size=None, debug=False):
        """
        Konstruktor för kontrollern.
        Args:
            size:       Tar in en sträng motsvarandes fönstrets storlek och dess position (BREDDxHLJD+X+Y). 
                        Vid None, anpassas förnstret responsivt till dess innehåll och hamnar i position 1x1.
            debug:      Booleanisk uttryck där True aktiverar debug-tabben. False som standard.
        """
        self.root = Tk()
        self.root.geometry(size)
        self.debug = debug
        self.model = Model()
        self.view = View(self.root, self.debug)

    def run(self):
        """
        Kör igång applikationen.
        """
        self.root.mainloop()


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


class Model(object):
    """
    Modellnivån.
    """
    None


class Database(object):
    """
    Databashanterare som sköter all kommunikation med databasen.
    """
    def __init__(self):
        """
        Konstruktorn för databashanteraren.
        """
        self.conn = None

    def open(self):
        """
        Öppnar en förbindelse med databasen.
        """
        self.conn = sqlite3.connect('krusty.db')

    def close(self):
        """
        Stänger en förbindelse med databasen.
        """
        self.conn.close()

# MAIN
if __name__ == '__main__':
    app = Controller('800x600+100+100', debug=True)
    app.run()

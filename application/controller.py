#!/usr/bin/env python3
from tkinter import *
from . import model
from . import view


class Controller(object):
    """
    Kontroller.
    """
    def __init__(self, size=None, debug=False):
        """
        Konstruktor för kontrollern.
        Argument:
            size:       Tar in en sträng motsvarandes fönstrets storlek och dess position (BREDDxHLJD+X+Y). 
                        Vid None, anpassas förnstret responsivt till dess innehåll och hamnar i position 1x1.
            debug:      Booleanisk uttryck där True aktiverar debug-tabben. False som standard.
        """
        self.root = Tk()
        self.root.geometry(size)
        self.debug = debug
        self.model = model.Model()
        self.view = view.View(self.root, self.debug)

    def run(self):
        """
        Kör igång applikationen.
        """
        self.root.mainloop()

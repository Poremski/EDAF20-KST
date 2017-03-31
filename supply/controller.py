from .configurations import *
from .model import *
from .view import *


class Controller:
    """
    Kontrollern:    Klassen kopplar samman Vyn med klassen Modellen.
                    -- Kontrollern genomför åtgärd baserat på händelser i Vyn.
                    -- Kontrollern skickar meddelanden till Modellen och 
                       till Vyn och erhåller respons.
                    -- Kontrollern har delegater.
    """
    def __init__(self, parent):
        self.parent = parent
        self.parent.title(APP_NAME)
        self.parent.geometry(WIN_GEOMETRY)
        self.model = Model(self)
        self.view = View(self)

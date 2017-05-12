from .configurations import *
from .view import *
from .model import *


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
        #self.parent.title(APP_NAME)
        #self.parent.geometry(WIN_GEOMETRY)
        self.model = Model(self)
        self.view = View(self, self.parent)
        self.update_data()

    def update_data(self):
        self.view.set_list_blocked(self.model.get_blocked_var())

    def data_changed_delegate(self):
        pass

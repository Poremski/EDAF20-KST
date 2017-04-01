from .database import *
class Model:
    """
    Modellen:   Klassen innehåller datastrukturen.
                -- Kontrollern kan skicka meddelanden till Modellen
                   och Modellen kan besvara dem.
                -- Modellen använder delegater för att sända meddelanden
                   till Kontrollern vid förändring.
                -- Modellen kommunicerar ALDRIG med Vyn.
                -- Modellen har getters och setters för att kommunicera
                   med Kontrollern.
    """
    def __init__(self, vc):
        self.vc = vc
        self.db = Database()
        self.recipes_var = None
        self.products_var = None
        self.ingredients_var = None
        self.units_var = None

    def data_changed_delegate(self):
        self.vc.data_changed_delegate()

    def get_recipes_var(self):
        return self.recipes_var

    def set_recipes_var(self):
        self.recipes_var = [list(i) for i in self.db.get_recipes()]
        self.data_changed_delegate()

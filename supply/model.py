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
        self.recipes_var = self.get_recipes_dict()

    def get_recipes_dict(self):
        self.set_recipes_dict()
        return self.recipes_var

    def set_recipes_dict(self):
        self.recipes_var = self.db.get_recipes()

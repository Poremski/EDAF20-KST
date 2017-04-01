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
        self.parent.title(APP_NAME)
        self.parent.geometry(WIN_GEOMETRY)
        self.model = Model(self)
        self.view = View(self, self.parent)
        self.update_recipes()
        self.view.set_recipes_var(self.model.get_recipes_var())

    def update_recipes(self):
        self.model.set_recipes_var()

    def data_changed_delegate(self):
        pass

    def handler_set_recipes(self, recipes):
        self.view.set_recipes_var(recipes)

    def handler_set_products(self, products):
        self.view.set_products_var(products)

    def handler_set_ingredients(self, ingredients):
        self.view.set_ingredients_var(ingredients)

    def handler_set_units(self, units):
        self.view.set_ingredients_var(units)

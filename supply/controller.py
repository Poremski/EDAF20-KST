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
        self.update_data()

    def update_data(self):
        self.model.set_recipes_var()
        self.view.set_recipes_var(self.model.get_recipes_var())
        self.view.set_products_var(self.model.get_products_var())
        self.view.set_ingredients_var(self.model.get_ingredients_var())

    def data_changed_delegate(self):
        pass

    def btn_delete_product(self):
        list = self.view.products_form.get()
        if len(list) is not 0:
            self.model.del_products_var(self.view.products_form.get().split()[1][:-1])
            self.update_data()
        else:
            self.view.showerror('Inget att ta bort', 'Det finns ingen produkt att ta bort.')

    def btn_delete_ingredient(self):
        list = self.view.ingredients_form.get()
        if len(list) is not 0:
            self.model.del_ingredients_var(self.view.ingredients_form.get().split()[1][:-1])
            self.update_data()
        else:
            self.view.showerror('Inget att ta bort', 'Det finns ingen ingrediens att ta bort.')

    def btn_add_product(self):
        name = self.view.products_entry.get().strip()
        if len(name) is not 0:
            self.model.set_products_var(name)
            self.update_data()
            self.view.showerror('Produkten är skapad', 'Den önskade produkten «%s» har nu skapats' % (str(name)))
        else:
            self.view.showerror('Inget att lägga till', 'Det finns ingen produkt att lägga till.')

    def btn_add_ingredient(self):
        name = self.view.ingredients_entry.get().strip()
        if len(name) is not 0:
            self.model.set_ingredients_var(name)
            self.update_data()
            self.view.showerror('Ingrediensen är skapad', 'Den önskade ingrediensen «%s» har nu skapats' % (str(name)))
        else:
            self.view.showerror('Inget att lägga till', 'Det finns ingen ingrediens att lägga till.')


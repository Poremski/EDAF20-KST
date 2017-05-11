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
        self.model = Model(self)
        self.view = View(self, self.parent)
        self.update_data()

    def update_data(self):
        pass

    def data_changed_delegate(self):
        pass

    def btn_add_customer(self):
        customer = self.view.customer_entry.get()
        address = self.view.address_entry.get()
        country = self.view.country_entry.get()

        if len(customer) and len(address) and len(country) is not 0:
            self.model.set_new_user(customer, address, country)
            self.update_data()
            self.view.showerror('Kund är nu inlagd', 'Kunden «%s» med adressen «%s» i landet «%s» har nu lagts till i databasen.' % (str(customer), str(address), str(country)))
        else:
            self.view.showerror('Inget att lägga till', 'Fyll i alla fält för att lägga in en ny kund till databasen.')

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
        self.view.set_order_list_var(self.model.get_order_list_var(self.view.get_chk_list()))
        self.view.set_blocked_var(self.model.get_unblocked_var())
        self.view.set_unblocked_var(self.model.get_blocked_var())
        self.view.set_order_pall_var(self.model.get_order_pall_var())
        self.update_products()
        self.view.set_pallet_var(self.model.get_pallet_var())
        self.view.set_location_var(['production', 'freezing', 'packbags', 'packbox', 'loadpallet', 'storage', 'ramp', 'delivering', 'delivered'])

    def unblock_pallet(self):
        list = self.view.unblocked_form.get()
        if len(list) is not 0:
            self.model.unblock_blocked_var(self.view.unblocked_form.get())
            self.update_data()
            self.view.showerror('Pall avblockerad', 'Pallen med pallkod «%s» har nu blivit avblockerad' % (str(list)))
        else:
            self.view.showerror('Inget att avblockera', 'Det finns ingen pall att avblockera.')

    def block_pallet(self):
        list = self.view.blocked_form.get()
        if len(list) is not 0:
            self.model.block_unblocked_var(self.view.blocked_form.get())
            self.update_data()
            self.view.showerror('Pall blockerad', 'Pallen med pallkod «%s» har nu blivit blockerad' % (str(list)))
        else:
            self.view.showerror('Inget att blockera', 'Det finns ingen pall att blockera.')

    def create_pallet(self):
        order = self.view.order_pall_form.get()
        if len(order) > 0:
            order = order.split(' ')[1]

        product = self.view.order_product_form.get()
        if len(product) > 0:
            product = product.split(' (pall ')[0]

        if len(order) is not 0 and len(product) is not 0:
            self.model.create_pallet(order, product)
            self.update_data()
            self.view.showerror('Pall skapad', 'Pallen med produkt «%s» har nu blivit skapad för order «%s»' % (product, order))
        else:
            self.view.showerror('Ingen pall att skapa', 'Det finns ingen pall att skapa.')

    def update_pallet(self):
        pallet = self.view.pallet_form.get()
        if len(pallet) > 0:
            pallet = pallet.split('Pallkod ')[1]
        location = self.view.location_form.get()

        if len(pallet) is not 0 and len(location) is not 0:
            self.model.update_location(pallet, location)
            self.update_data()
            self.view.showerror('Pall ändrad', 'Pallen med pallkod «%s» har nu blivit ändrad till «%s»' % (pallet, location))
        else:
            self.view.showerror('Ingen pall att ändra', 'Det finns ingen pall att ändra.')

    def update_products(self):
        order = self.view.order_pall_form.get()
        if len(order) > 0:
            order = order.split(' ')[1]
        self.view.set_product_var(self.model.get_order_products(order))


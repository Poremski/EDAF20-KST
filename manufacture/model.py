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

    def data_changed_delegate(self):
        self.vc.data_changed_delegate()

    def get_blocked_var(self):
        return [list(i) for i in self.db.get_blocked_pallets()]

    def get_unblocked_var(self):
        return [list(i) for i in self.db.get_unblocked_pallets()]

    def get_order_list_var(self,  chk_list):
        return [list(i) for i in self.db.get_order_list(chk_list)]

    def unblock_blocked_var(self, pallet):
        self.db.unblock_blocked_pallet(pallet)

    def block_unblocked_var(self, pallet):
        self.db.block_unblocked_pallet(pallet)

    def get_order_pall_var(self):
        return [list(i) for i in self.db.get_order_pall_list()]

    def get_order_products(self, order):
        return [list(i) for i in self.db.get_order_products(order)]

    def create_pallet(self, order, product):
        self.db.create_pallet(order, product)

    def get_pallet_var(self):
        return [list(i) for i in self.db.get_pallets()]

    def update_location(self, pallet, location):
        self.db.update_location(pallet, location)
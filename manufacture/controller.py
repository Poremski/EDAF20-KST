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

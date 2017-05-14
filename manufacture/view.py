from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


class View():
    """
    Vy:   Klassen hanterar element som kretsar kring användargränssnittet.
          -- Kontrollern kan skicka meddelanden till Vyn.
          -- Vyn kan anropa metoder i Kontrollern när en händelse inträffar.
          -- Vyn kommunicerar ALDRIG med Modellen.
          -- Vyn har setters och getters som den använder för att kommunicerar 
             med Kontrollern.
    """
    def __init__(self, vc, parent):
        self.vc = vc  # delegate/callback pointer

        self.main_frame = Frame(parent)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.notebook = Notebook(self.main_frame)
        self.notebook.pack(fill=BOTH, expand=True)

        self.listbox_blocked = Listbox()
        self.treeview_pallets = Treeview()

        self.blocked_var = []
        self.blocked_value = StringVar()
        self.order_var = []

        self.check_blocked = BooleanVar()
        self.check_unblocked = BooleanVar()
        self.check_production = BooleanVar()
        self.check_freezing = BooleanVar()
        self.check_packbags = BooleanVar()
        self.check_packbox = BooleanVar()
        self.check_loadpallet = BooleanVar()
        self.check_storage = BooleanVar()
        self.check_ramp = BooleanVar()
        self.check_delivering = BooleanVar()
        self.check_delivered = BooleanVar()

        for i in [self.check_blocked, self.check_unblocked, self.check_production,
                  self.check_freezing, self.check_packbags, self.check_packbox,
                  self.check_loadpallet, self.check_storage, self.check_ramp,
                  self.check_delivering, self.check_delivered]:
            i.set(True)

        self.widget_pallets()
        self.widget_blocked_pallets()

    def widget_pallets(self):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text='Pall och order')

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.treeview_pallets.__init__(frame, yscrollcommand=scrollbar.set)
        self.treeview_pallets['columns'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
        self.treeview_pallets.column('A', width=100)
        self.treeview_pallets.column('B', width=100)
        self.treeview_pallets.column('C', width=50)
        self.treeview_pallets.column('D', width=150)
        self.treeview_pallets.column('E', width=100)
        self.treeview_pallets.column('F', width=50)
        self.treeview_pallets.column('G', width=50)
        self.treeview_pallets.heading('A', text='Orderdatum')
        self.treeview_pallets.heading('B', text='Palldatum')
        self.treeview_pallets.heading('C', text='Pallkod')
        self.treeview_pallets.heading('D', text='Produkt')
        self.treeview_pallets.heading('E', text='Placering')
        self.treeview_pallets.heading('F', text='Säljstopp')
        self.treeview_pallets.heading('G', text='Leverans')
        self.treeview_pallets.pack(side=LEFT, expand=True)

        self.tree_orders()

        chk_a = Checkbutton(frame, text='Blockerade pall', variable=self.check_blocked, onvalue=True,offvalue=False).pack(side=TOP, anchor=W)
        chk_b = Checkbutton(frame, text='Oblockerade pall', variable=self.check_unblocked, onvalue=True,offvalue=False).pack(side=TOP, anchor=W)
        chk_c = Checkbutton(frame, text='Produktion', variable=self.check_production, onvalue=True,offvalue=False).pack(side=TOP, anchor=W)
        chk_d = Checkbutton(frame, text='Frysning', variable=self.check_freezing, onvalue=True,offvalue=False).pack(side=TOP, anchor=W)
        chk_e = Checkbutton(frame, text='Påsning', variable=self.check_packbags, onvalue=True,offvalue=False).pack(side=TOP, anchor=W)
        chk_f = Checkbutton(frame, text='Lådning', variable=self.check_packbox, onvalue=True,offvalue=False).pack(side=TOP, anchor=W)
        chk_g = Checkbutton(frame, text='Pallning', variable=self.check_loadpallet, onvalue=True,offvalue=False).pack(side=TOP, anchor=W)
        chk_h = Checkbutton(frame, text='Förvaring', variable=self.check_storage, onvalue=True,offvalue=False).pack(side=TOP, anchor=W)
        chk_i = Checkbutton(frame, text='Lastning', variable=self.check_ramp, onvalue=True,offvalue=False).pack(side=TOP, anchor=W)
        chk_j = Checkbutton(frame, text='Levereras', variable=self.check_delivering, onvalue=True,offvalue=False).pack(side=TOP, anchor=W)
        chk_l = Checkbutton(frame, text='Levererat', variable=self.check_delivered, onvalue=True,offvalue=False).pack(side=TOP, anchor=W)

        scrollbar.config(command=self.treeview_pallets)

    def tree_orders(self):
        last_order = 0
        for value in self.get_pall_var():
            if value is not None:
                if value[0] is not last_order:
                    self.treeview_pallets.insert('', value[0], value[0], text='%s (Order %s)' % (value[1], value[0]))
                    last_order = value[0]
                if value[7] is 1:
                    blocked = 'S'
                else:
                    blocked = 'F'
                self.treeview_pallets.insert(value[0], value[0], '', values=(value[2], value[3], value[4], value[5], value[6], blocked, value[8]))

    def get_pall_var(self):
        return self.order_var

    def widget_blocked_pallets(self):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text='Blockerade pallar')

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox_blocked.__init__(frame)
        self.listbox_blocked.pack(fill=BOTH, expand=True)

        scrollbar.config(command=self.listbox_blocked)

    def set_list_blocked(self, list):
        self.blocked_var = list
        for b in self.blocked_var:
            self.listbox_blocked.insert(END, 'Barcode: ' + str(b))

    def set_order_list_var(self, order):
        self.order_var = order
        for i in self.treeview_pallets.get_children():
            self.treeview_pallets.delete(i)
        self.tree_orders()

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
        self.blocked_form = Combobox()
        self.unblocked_var = []
        self.unblocked_form = Combobox()

        self.order_pall_var = []
        self.order_pall_form = Combobox()
        self.order_product_var = []
        self.order_product_form = Combobox()

        self.pallet_var = []
        self.pallet_form = Combobox()
        self.location_var = []
        self.location_form = Combobox()

        self.order_var = []

        self.check_blocked = IntVar()
        self.check_unblocked = IntVar()
        self.check_production = IntVar()
        self.check_freezing = IntVar()
        self.check_packbags = IntVar()
        self.check_packbox = IntVar()
        self.check_loadpallet = IntVar()
        self.check_storage = IntVar()
        self.check_ramp = IntVar()
        self.check_delivering = IntVar()
        self.check_delivered = IntVar()

        for i in [self.check_blocked, self.check_unblocked, self.check_production,
                  self.check_freezing, self.check_packbags, self.check_packbox,
                  self.check_loadpallet, self.check_storage, self.check_ramp,
                  self.check_delivering, self.check_delivered]:
            i.set(1)

        self.widget_pallets()
        self.widget_blocked_pallets()
        self.widget_create_pallets()

    def showerror(self, title, message):
        messagebox.showerror(title, message)

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

        Checkbutton(frame, text='Blockerade pall', variable=self.check_blocked,
                    onvalue=True, offvalue=False,
                    command=self.update_list).pack(side=TOP, anchor=W)
        Checkbutton(frame, text='Oblockerade pall', variable=self.check_unblocked,
                    onvalue=True, offvalue=False,
                    command=self.update_list).pack(side=TOP, anchor=W)
        Checkbutton(frame, text='Produktion', variable=self.check_production,
                    onvalue=True, offvalue=False,
                    command=self.update_list).pack(side=TOP, anchor=W)
        Checkbutton(frame, text='Frysning', variable=self.check_freezing,
                    onvalue=True, offvalue=False,
                    command=self.update_list).pack(side=TOP, anchor=W)
        Checkbutton(frame, text='Påsning', variable=self.check_packbags,
                    onvalue=True, offvalue=False,
                    command=self.update_list).pack(side=TOP, anchor=W)
        Checkbutton(frame, text='Lådning', variable=self.check_packbox,
                    onvalue=True, offvalue=False,
                    command=self.update_list).pack(side=TOP, anchor=W)
        Checkbutton(frame, text='Pallning', variable=self.check_loadpallet,
                    onvalue=True, offvalue=False,
                    command=self.update_list).pack(side=TOP, anchor=W)
        Checkbutton(frame, text='Förvaring', variable=self.check_storage,
                    onvalue=True, offvalue=False,
                    command=self.update_list).pack(side=TOP, anchor=W)
        Checkbutton(frame, text='Lastning', variable=self.check_ramp,
                    onvalue=True, offvalue=False,
                    command=self.update_list).pack(side=TOP, anchor=W)
        Checkbutton(frame, text='Levereras', variable=self.check_delivering,
                    onvalue=True, offvalue=False,
                    command=self.update_list).pack(side=TOP, anchor=W)
        Checkbutton(frame, text='Levererat', variable=self.check_delivered,
                    onvalue=True, offvalue=False,
                    command=self.update_list).pack(side=TOP, anchor=W)

        scrollbar.config(command=self.treeview_pallets)

    def update_list(self):
        self.vc.update_data()

    def get_chk_list(self):
        return [self.check_blocked.get(), self.check_unblocked.get(),
                self.check_production.get(), self.check_freezing.get(),
                self.check_packbags.get(), self.check_packbox.get(),
                self.check_loadpallet.get(), self.check_storage.get(),
                self.check_ramp.get(), self.check_delivering.get(),
                self.check_delivered.get()]

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

    def get_pallet_var(self):
        return self.pallet_var

    def get_order_pall_var(self):
        return self.order_pall_var

    def get_blocked_var(self):
        return self.blocked_var

    def get_unblocked_var(self):
        return self.unblocked_var

    def get_location_var(self):
        return self.location_var

    def get_pallet_var(self):
        return self.pallet_var

    def get_order_product_var(self):
        return self.order_product_var

    def set_blocked_var(self, blocked):
        self.blocked_var = blocked
        list = []
        for value in self.get_blocked_var():
            list += ['%s' % (value[0])]
        if len(list) > 0:
            self.blocked_form['values'] = list
        else:
            self.blocked_form['values'] = ['']
        self.blocked_form.current(0)

    def set_location_var(self, locations):
        self.location_var = locations
        list = []
        for value in self.get_location_var():
            list += ['%s' % (value)]
        if len(list) > 0:
            self.location_form['values'] = list
        else:
            self.location_form['values'] = ['']
        self.location_form.current(0)

    def set_unblocked_var(self, unblocked):
        self.unblocked_var = unblocked
        list = []
        for value in self.get_unblocked_var():
            list += ['%s' % (value[0])]
        if len(list) > 0:
            self.unblocked_form['values'] = list
        else:
            self.unblocked_form['values'] = ['']
        self.unblocked_form.current(0)

    def set_order_pall_var(self, orders):
        self.order_pall_var = orders
        list = []
        for value in self.get_order_pall_var():
            list += ['Ordernummer %s (%s)' % (value[0], value[1])]
        if len(list) > 0:
            self.order_pall_form['values'] = list
        else:
            self.order_pall_form['values'] = ['']
        self.order_pall_form.current(0)

    def set_product_var(self, products):
        self.order_product_var = products
        list = []
        for value in self.get_order_product_var():
            list += ['%s (pall %s av %s)' % (value[0], value[2]+1, value[1])]
        if len(list) > 0:
            self.order_product_form['values'] = list
        else:
            self.order_product_form['values'] = ['']
        self.order_product_form.current(0)

    def set_pallet_var(self, pallets):
        self.pallet_var = pallets
        list = []
        for value in self.get_pallet_var():
            list += ['Pallkod %s' % (value[0])]
        if len(list) > 0:
            self.pallet_form['values'] = list
        else:
            self.pallet_form['values'] = ['']
        self.pallet_form.current(0)

    def widget_blocked_pallets(self):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text='Säljstopp')

        blocked_win = Panedwindow(frame, orient=VERTICAL)
        blocked_frame = Labelframe(blocked_win, text='Blockera pall')
        blocked_win.add(blocked_frame)
        Label(blocked_frame, text='Pallkod:').pack(side=LEFT)
        Button( blocked_frame, text='Blockera', command=self.vc.block_pallet).pack(side=RIGHT)
        self.blocked_form.__init__(blocked_frame, textvariable=self.blocked_form, values=self.blocked_var, state='readonly')
        self.blocked_form.pack(side=RIGHT, fill=X, expand=TRUE)
        blocked_win.pack(side=TOP, anchor=W, fill=X, expand=NO)

        unblocked_win = Panedwindow(frame, orient=VERTICAL)
        unblocked_frame = Labelframe(unblocked_win, text='Avblockera pall')
        unblocked_win.add(unblocked_frame)
        Label(unblocked_frame, text='Pallkod:').pack(side=LEFT)
        Button(unblocked_frame, text='Avblockera', command=self.vc.unblock_pallet).pack(side=RIGHT)
        self.unblocked_form.__init__(unblocked_frame, textvariable=self.unblocked_form, values=self.unblocked_var, state='readonly')
        self.unblocked_form.pack(side=RIGHT, fill=X, expand=TRUE)
        unblocked_win.pack(side=TOP, anchor=W, fill=X, expand=NO)

    def set_order_list_var(self, order):
        self.order_var = order
        self.treeview_pallets.delete(*self.treeview_pallets.get_children())
        """
        for i in self.treeview_pallets.get_children():
            self.treeview_pallets.delete(i)
        """
        self.tree_orders()

    def widget_create_pallets(self):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text='Administration')

        create_win = Panedwindow(frame, orient=VERTICAL)
        create_frame = Labelframe(create_win, text='Skapa pall')
        create_win.add(create_frame)
        Label(create_frame, text='Order:').pack(side=LEFT)
        Button(create_frame, text='Skapa pall', command=self.vc.create_pallet).pack(side=RIGHT)
        self.order_pall_form.__init__(create_frame, textvariable=self.order_pall_form, values=self.order_pall_var, state='readonly')
        self.order_pall_form.pack(side=LEFT, fill=X, expand=TRUE)
        self.order_pall_form.bind('<<ComboboxSelected>>', self.update_products)
        Label(create_frame, text='Produkt:').pack(side=LEFT)
        self.order_product_form.__init__(create_frame, textvariable=self.order_product_form, values=self.order_product_var, state='readonly')
        self.order_product_form.pack(side=LEFT, fill=X, expand=TRUE)
        create_win.pack(side=TOP, anchor=W, fill=X, expand=NO)

        update_win = Panedwindow(frame, orient=VERTICAL)
        update_frame = Labelframe(update_win, text='Uppdatera pall')
        update_win.add(update_frame)
        Label(update_frame, text='Pall:').pack(side=LEFT)
        Button(update_frame, text='Uppdatera pall', command=self.vc.update_pallet).pack(side=RIGHT)
        self.pallet_form.__init__(update_frame, textvariable=self.pallet_form, values=self.pallet_var, state='readonly')
        self.pallet_form.pack(side=LEFT, fill=X, expand=TRUE)
        Label(update_frame, text='Placering:').pack(side=LEFT)
        self.location_form.__init__(update_frame, textvariable=self.location_form, values=self.location_var, state='readonly')
        self.location_form.pack(side=LEFT, fill=X, expand=TRUE)
        update_win.pack(side=TOP, anchor=W, fill=X, expand=NO)

    def update_products(self, event):
        self.vc.update_products()

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

        self.tree = Treeview()

        self.customer_entry = StringVar()
        self.address_entry = StringVar()
        self.country_entry = StringVar()

        self.widget_add_customer()

    def showerror(self, title, message):
        messagebox.showerror(title, message)

    def widget_add_customer(self):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text='Lägg till')

        p = Panedwindow(frame, orient=VERTICAL)
        f = Labelframe(p, text='Lägg till kund')
        p.add(f)

        lbls = ['Land:', 'Företag:', 'Adress:', '']
        flds = []

        for i in range(4):
            f = Frame()
            f.pack(in_=frame, side=TOP, fill=X, padx=10)

            lbl = Label(text=lbls[i], width=10)

            if i == 1:
                e = Entry(textvariable=self.customer_entry, width=20)
            elif i == 2:
                e = Entry(textvariable=self.address_entry, width=20)
            elif i == 3:
                e = Button(text='Lägg till', command=self.vc.btn_add_customer)
            else:
                e = Combobox(width=20)
                e.__init__(textvariable=self.country_entry, state='readonly')
                e['values'] = ('SE')
                e.current(0)

            flds.append(e)

            lbl.pack(in_=f, side=LEFT, expand=Y, fill=X)
            e.pack(in_=f, side=LEFT, expand=Y, fill=X)

        flds[0].focus_set()
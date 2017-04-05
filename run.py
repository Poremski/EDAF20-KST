import platform
import os
from tkinter import *
from tkinter.ttk import *
from supply.controller import Controller as Supply
from manufacture.controller import Controller as Manufacture


class Krusty:

    def __init__(self):
        self.root = Tk()
        self.root.title('Krustys övervakningsverktyg')
        self.menu()
        main_frame = Frame(self.root).pack(fill=BOTH, expand=True)
        notebook = Notebook(main_frame)

        supply = Frame(notebook)
        notebook.add(supply, text='Sortimentenheten')
        Supply(supply)

        manufacture = Frame(notebook)
        notebook.add(manufacture, text='Tillverkningsenheten')
        Manufacture(manufacture)

        delivery = Frame(notebook)
        notebook.add(delivery, text='Leveransenheten')

        notebook.pack(fill=BOTH, expand=True)

        self.root.mainloop()

    def menu(self):
        """
        Menyn
        """
        menu = Menu(self.root)
        self.root.config(menu=menu)

        file_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label='Arkiv', menu=file_menu)

        if platform.system() in ['Windows', 'Linux']:
            help_menu = Menu(menu, tearoff=0)
            menu.add_cascade(label='Hjälp', menu=help_menu)
            help_menu.add_command(label='Om...', command=self.about_dlg)
        else:
            file_menu.add_command(label='Om...', command=self.about_dlg)
            file_menu.add_separator()
        file_menu.add_command(label='Avsluta', command=self.root.quit)

    def about_dlg(self):
        """
        Dialogfönstret "Om…"
        """
        about = Toplevel()
        about.title('Om Krustys övervakningsverktyg')
        about.resizable(FALSE, FALSE)
        about.geometry('+200+200')

        frame = Frame(about)
        frame.pack()

        with open(os.path.join(os.getcwd(), '../KST.base64'), 'r') as file:
            img_data = file.readlines()

        img = PhotoImage(data=img_data)
        logo = Label(frame, image=img)
        logo.image = img
        logo.grid(row=1, column=0)

        Label(frame, text='Krustys övervakningsverktyg').grid(row=0, columnspan=2)

        txtmsg = 'Detta program är utformat som en del av ett projekt i kursen Databasteknik (EDAF20) \n' \
                 'vid LTH Campus Helsingborg, där ett verktyg utifrån specifika funktionalitetsönskemål\n' \
                 'skulle implementeras.\n\n' \
                 'Genom den teoretiska kunskap vi har tillägnat oss under kursens gång, har vi kunnat \n' \
                 'tillämpa kunskapen praktiskt och utveckla programgränssnitt till en databas med \n' \
                 'efterfrågad funktionalitet.\n\n' \
                 'Vi har genom detta därmed uppnått de mål som uttrycks i kursplanen för den berörda \n' \
                 'kursen.\n\n' \
                 'De involverade i projektet:\n     Javier Poremski och Simon Farre\n' \
                 'Datum:\n     2017-04-05'

        Label(frame, text=txtmsg).grid(row=1, column=1)

        Button(frame, text='Stäng', command=about.destroy).grid(row=2, columnspan=2)


if __name__ == '__main__':
    Krusty()
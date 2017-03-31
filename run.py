from tkinter import *
from supply.controller import Controller as Supply


def main():
    root = Tk()
    frame = Frame(root, bg='#0555FF')
    app = Supply(root)
    root.mainloop()

if __name__ == '__main__':
    main()
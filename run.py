from tkinter import *
from supply.controller import Controller as Supply


def main():
    root = Tk()
    Frame(root, bg='#0555FF')
    Supply(root)
    root.mainloop()

if __name__ == '__main__':
    main()
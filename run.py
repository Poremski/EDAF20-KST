from tkinter import *
from supply.controller import Controller as Supply


def main():
    root = Tk()
    Supply(root)
    root.mainloop()

if __name__ == '__main__':
    main()
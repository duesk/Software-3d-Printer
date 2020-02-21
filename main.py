from tkinter import *
from Select_port import run_select_port




if __name__ == "__main__":


    puerto = run_select_port()
    print("puerto recibido : " + puerto)
    root = Tk()

    root.mainloop()

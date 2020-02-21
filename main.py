from tkinter import *
from tkinter import filedialog as Filedialog
from Select_port import run_select_port
from printrun.printcore import printcore

ruta = ""
gcode = ""

def send_gcode():
    printer.send("G28")

def select_file():
    global ruta 
    global gcode 
    ruta = Filedialog.askopenfilename(initialdir = "~/Escritorio", title = "Abrir archivo" , filetypes = (("Gcode", "*.gcode"),)  )
    print(ruta)
    if ruta != "":
        archivo = open(ruta, "r")
        gcode = archivo.readlines()
        archivo.close()
        print(gcode)
        printer.send("G28")
        printer.startprint(gcode = gcode)


if __name__ == "__main__":

    puerto = run_select_port()
    print("puerto recibido : " + puerto)

    #init printer
    printer =  printcore( puerto, 115200)


    root = Tk()


    Button(text = "send gcode", command = select_file).pack()

    root.mainloop()

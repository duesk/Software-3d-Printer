from tkinter import *
from tkinter import filedialog as Filedialog
from Select_port import run_select_port
from printrun.printcore import printcore
from printrun.gcoder import LightGCode as LightGCode 

import threading
import time

ruta = ""
gcode = ""
temp_global = ""
temp_lb = "20.0"

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
        gcode = [i.strip() for i in open(ruta)]
        gcode = LightGCode(gcode)
        printer.startprint(gcode)
        printer.send_now("G90")


def get_temp(printer):
    printer.send_now("M105")
    print("holas: "+ temp_global)


def temp_callback(a):
    global temp_global
    print('temp_callback', a)
    temp_global = a

if __name__ == "__main__":

    puerto = run_select_port()
    print("puerto recibido : " + puerto)


    #init printer
    printer =  printcore( puerto, 115200)
    printer.online
    printer.tempcb = temp_callback

    root = Tk()


    Button(root, text = "send gcode", command = select_file).pack()
    #Button(text = "get temp", command = lambda : get_temp(printer)).pack()

    ############# TEMP
    temp_label_extruder = StringVar()
    temp_label_extruder.set("Temperatura: " + temp_lb)
    lb_temp = Label(root, textvar = temp_label_extruder)
    lb_temp.pack(pady = 20, padx = 20)


    #inicio del thread.
    #tread_1 = threading.Thread(target = set_temp, args = () )


    root.mainloop()
    printer.disconnect()

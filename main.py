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
temp_state = ""
temp_set = 100

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
    print("holas:"+ temp_global)
    

def set_temp(printer,temp_label_extruder):
    global temp_state
    global temp_set
    temp_saved = 0
    while not printer.online:
        time.sleep(0.1)
    if (temp_set != temp_saved):
        temp_saved = temp_set
        printer.send_now("M104 S%d" %temp_set)
        print("temperatura seteada")
    time.sleep(1)
    get_temp(printer)
    time.sleep(3)
    while True:
        get_temp(printer)
        time.sleep(3)
        temp_label_extruder.set("Temperatura: " + temp_state)
        lb_temp.pack()
        print("ciclo")


def temp_callback(a):
    global temp_state 
    temp_state = ""
    print('temp_callback', a)
    for i in range(5,8):
        temp_state += a[i]
    #print("Parse:" + temp_state)


if __name__ == "__main__":

    #variables de estilo
    title_size_font = 16

    puerto = run_select_port()
    print("puerto recibido : " + puerto)


    #init printer
    printer =  printcore( puerto, 115200)
    printer.online
    printer.tempcb = temp_callback

    root = Tk()
    root.minsize(500,700)
    Label(root, text = "Temperatura",font = ("",title_size_font)).pack(anchor = "nw",padx = 15, pady = 15)

    Button(root, text = "send gcode", command = select_file).pack()
    #Button(text = "get temp", command = lambda : get_temp(printer)).pack()

    ############# TEMP
    temp_label_extruder = StringVar()
    temp_label_extruder.set("Temperatura: " + " 20.0")
    lb_temp = Label(root, textvar = temp_label_extruder)
    lb_temp.pack(pady = 20, padx = 20)



    #inicio del thread.
    thread_1 = threading.Thread(target = set_temp, args = (printer, temp_label_extruder, ) )
    thread_1.start()
    

    root.mainloop()
    printer.disconnect()


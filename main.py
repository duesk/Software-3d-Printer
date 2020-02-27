from tkinter import *
from tkinter import ttk
from tkinter import filedialog as Filedialog
from Select_port import run_select_port
from printrun.printcore import printcore
from printrun.gcoder import LightGCode as LightGCode 

import PIL
from PIL import Image
from PIL import ImageTk

import threading
import time

ruta = ""
gcode = ""
temp_global = ""
temp_state = ""
temp_set = 180

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
    #print("holas:"+ temp_global)
    

def set_temp(printer,temp_label_extruder):
    global temp_state
    global temp_set
    temp_saved = 0
    
    while not printer.online:
        print("impresora no online")
        time.sleep(0.1)

    while True:
        print("temp set: " + str(temp_set))
        print("temp saved: " + str(temp_saved))
        if (temp_set != temp_saved):
            temp_saved = temp_set
            printer.send_now("M104 S%d" %temp_set)
            print("temperatura seteada")
        get_temp(printer)
        time.sleep(3)
        temp_label_extruder.set("Temp. actual:     %s°C     de     " %temp_state)
        lb_temp.pack()
        print("ciclo")


def temp_callback(a):
    global temp_state 
    temp_state = ""
    print('temp_callback', a)
    for i in range(5,8):
        temp_state += a[i]
    #print("Parse:" + temp_state)

def high_temp(temp_set_var):
    global temp_set
    temp_set +=1
    temp_set_var.set(str(temp_set))
    lb_set_temp.pack()

def low_temp(temp_set_var):
    global temp_set
    temp_set -=1
    temp_set_var.set(str(temp_set))
    lb_set_temp.pack()

#########################################################################
##################               init               #####################
#########################################################################


if __name__ == "__main__":

    #variables de estilo
    title_size_font = 16
    content_size_font = 12
    color_theme = "snow"
    color_button = "deepskyblue3"
    color_text_button = "gray99"
    font = "Garuda"
    color_font_activate_button = "gray25"
    color_bg_activate_button = "deep sky Blue"



    puerto = run_select_port()
    print("puerto recibido : " + puerto)


    #init printer
    printer =  printcore( puerto, 115200)
    #printer.online
    printer.tempcb = temp_callback


    #########################################################################
    ##################            interfaz             ######################
    #########################################################################

    root = Tk()
    root.title( "Colibri 3D")
    root.minsize(500,310)
    #root.maxsize(500,700)
    root.resizable(0,0)
    root.config(bg = color_theme)

    im = PIL.Image.open("logo.png")
    logo = PIL.ImageTk.PhotoImage(im)


    #######################################
    ###             Textvar             ###
    #######################################

    temp_label_extruder = StringVar()
    temp_label_extruder.set("Temp. actual:     --°C     de     ")

    temp_set_var = StringVar()
    temp_set_var.set(str(temp_set))



    #frame con padiing 15px
    frame = Frame(root)
    frame.config(bg = color_theme)
    frame.pack(side = "top", anchor = "nw", padx = 15, pady = 15,fill = "both")
    
    #######################################
    ###           Temperatura           ###
    #######################################

    #frame  titulo e imagen
    sub_frame_1 = Frame(frame,)
    sub_frame_1.config(bg = color_theme)
    sub_frame_1.pack(side = "top", anchor = "nw",fill = "both")
    
    #Label title TEMPERATURA
    lb_title_temp = Label(sub_frame_1, text = "Temperatura",font = (font ,title_size_font),)
    lb_title_temp.config(bg = color_theme)
    lb_title_temp.pack(side = "left",anchor = "s")

    #Label IMAGEN LOGO.png
    lb_logo = Label(sub_frame_1, image = logo, )
    lb_logo.config(bg = color_theme)
    lb_logo.pack(side = "right",anchor = "n")

    #frame separador
    frame_2 = Frame(frame,)
    frame_2.config(bg = color_theme)
    frame_2.pack( fill = "both", expand = 1)

    ttk.Separator(frame_2, orient='horizontal').pack(side='top', fill='x') #linea separadora

    #label Temperatura 
    lb_temp = Label(frame_2, textvar = temp_label_extruder,font = (font ,content_size_font) )
    lb_temp.config(bg = color_theme)
    lb_temp.pack(side = "left", anchor = "nw", pady = 15)

    #Label(frame_2, text = "   /   ", font = (font ,content_size_font), bg = color_theme).pack(side = "left",pady = 15)
    
    btn_lower_temp = Button(frame_2, text = "—",font = (font ,content_size_font),bg = color_button, fg = color_text_button, command = lambda: low_temp(temp_set_var) )
    btn_lower_temp.config(activebackground = color_bg_activate_button, activeforeground = color_font_activate_button)
    btn_lower_temp.pack(side = "left", anchor = "nw", pady = 10)


    #separador
    Label(frame_2, text = " ", font = (font ,content_size_font), bg = color_theme).pack(side = "left",pady = 15)

    lb_set_temp = Label(frame_2, textvar = temp_set_var, font = (font ,content_size_font))
    lb_set_temp.config(bg = "gray87")
    lb_set_temp.pack(side = "left", anchor = "nw", pady = 15)

    #separador
    Label(frame_2, text = " ", font = (font ,content_size_font), bg = color_theme).pack(side = "left",pady = 15)

    btn_higher_temp = Button(frame_2, text = "+",font = (font ,content_size_font),bg = color_button, fg = color_text_button, command = lambda: high_temp(temp_set_var) )
    btn_higher_temp.config(activebackground = color_bg_activate_button, activeforeground = color_font_activate_button)
    btn_higher_temp.pack(side = "left", anchor = "nw",pady= 10)

    ########################################
    ###             Archivo             ####
    ########################################
    
    frame_3 = Frame(frame,)
    frame_3.config(bg = color_theme)
    frame_3.pack( side ="top", fill = "both", expand = 1)
    
    lb_title_archivo = Label(frame_3, text = "Archivo", font=(font ,title_size_font))
    lb_title_archivo.config(bg = color_theme)
    lb_title_archivo.pack(side = "top",anchor = "nw")

    ttk.Separator(frame_3, orient='horizontal').pack( fill='x') #linea separadora

    bt_select_file = Button(frame_3, text = " Seleccionar ",font = (font ,content_size_font),bg = color_button, fg = color_text_button )
    bt_select_file.config(activebackground = color_bg_activate_button, activeforeground = color_font_activate_button)
    bt_select_file.pack(side = "left", pady = 10)

    Label(frame_3, text = "   ", font = (font ,content_size_font), bg = color_theme).pack(side = "left",pady = 15)


    lb_Select_file = Label(frame_3, text = "Ningun archivo seleccionado", font = (font ,content_size_font))
    lb_Select_file.config(bg = color_theme)
    lb_Select_file.pack(side = "left",pady = 15)
    ########################################
    ###             imprimir             ###
    ########################################

    frame_4 = Frame(frame,)
    frame_4.config(bg = color_theme)
    frame_4.pack( side ="top", fill = "both", expand = 1)
    

    ttk.Separator(frame_4, orient='horizontal').pack( fill='x') #linea separadora

    btn_start_print = Button(frame_4, text = "Imprimir",font = (font ,content_size_font),bg = color_button, fg = color_text_button )
    btn_start_print.config(activebackground = color_bg_activate_button, activeforeground = color_font_activate_button)
    btn_start_print.pack(side = "left", pady = 10)

    Label(frame_4, text = "   ", font = (font ,content_size_font), bg = color_theme).pack(side = "left",pady = 15)


    btn_cancel = Button(frame_4, text = "Cancelar",font = (font ,content_size_font),bg = color_button, fg = color_text_button)
    btn_cancel.config(activebackground = color_bg_activate_button, activeforeground = color_font_activate_button)
    btn_cancel.pack(side = "left", pady = 10)


    ########################################
    ###             imprimir             ###
    ########################################
    frame_5 = Frame(frame,)
    frame_5.config(bg = color_theme)
    frame_5.pack(side= "left", fill = "both", expand = 1)

    progressbar = ttk.Progressbar(frame_5, length = 100, mode = "determinate", style = "red.Horizontal.TProgressbar")
    progressbar.pack(fill = "both", expand = 1, pady = 10)
    progressbar.step(90.0)

    

    #########################################################################
    ##################        inicio del thread        ######################
    #########################################################################

    #inicio del thread.
    thread_1 = threading.Thread(target = set_temp, args = (printer, temp_label_extruder, ) )
    thread_1.start()
    

    root.mainloop()
    printer.disconnect()


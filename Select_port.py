from tkinter import *
from Port_connect import *


puerto = []
send_port = None

#variables de stylo
title_size_font = 16
content_size_font = 12
color_theme = "snow"
color_button = "deepskyblue3"
color_text_button = "gray99"
font = "Garuda"
color_font_activate_button = "gray25"
color_bg_activate_button = "deep sky Blue"


def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   



def connect(lst_box_puertos, root):
    global send_port
    try:
        port = lst_box_puertos.curselection()
        port = lst_box_puertos.get(port)
        send_port = port
        root.destroy()
    except:
        pass



def w_select_port():
    
    root = Tk()
    root.minsize(400, 150 )
    root.config(bg = color_theme)
    


    #Preparacion de los puertos 
    puerto = serial_ports()
    #print("Puerto :" + str(puerto))

    #preparacion de la listbox para seleccionar los puertos 
    Label(text = "Selecciona el puerto donde esta conectada la impresora", bg = color_theme, font = (font, content_size_font)).pack(pady = 15, padx = 15)
    lst_box_puertos = Listbox(root)
    for i in puerto :
        print("puerto disponibles : " + i)
        lst_box_puertos.insert(1,i)  
    lst_box_puertos.config(font = ("",content_size_font))
    lst_box_puertos.pack()

    #interfaz grafica
    root.title("Colibri 3D")
    

    btn_connect = Button(text ="Conectar", command = lambda : connect(lst_box_puertos, root), )
    btn_connect.config(bg = color_button, fg = color_text_button ,font =(font,content_size_font))
    btn_connect.config( activebackground = color_bg_activate_button, activeforeground =color_font_activate_button, font = (font,content_size_font))
    btn_connect.pack(padx = 15, pady = 15)



    root.mainloop()


def run_select_port():
    w_select_port()
    return send_port

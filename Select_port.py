from tkinter import *
from Port_connect import *


puerto = []
send_port = ""

#variables de stylo
bg_color = "alice blue"
font_size = 11


def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   



def connect(lst_box_puertos, root):
    global send_port
    port = lst_box_puertos.curselection()
    port = lst_box_puertos.get(port)
    send_port = port
    root.destroy()
    



def w_select_port():
    
    root = Tk()
    root.minsize(400, 150 )
    root.config(bg = bg_color)
    


    #Preparacion de los puertos 
    puerto = serial_ports()
    #print("Puerto :" + str(puerto))

    #preparacion de la listbox para seleccionar los puertos 
    Label(text = "Selecciona el puerto donde esta conectada la impresora", bg = bg_color, font = ("", font_size)).pack(pady = 15, padx = 15)
    lst_box_puertos = Listbox(root)
    for i in puerto :
        print("puerto disponibles : " + i)
        lst_box_puertos.insert(1,i)  
    lst_box_puertos.config(font = ("",font_size))
    lst_box_puertos.pack()

    #interfaz grafica
    root.title("Colibri 3D")
    

    btn_connect = Button(text ="Conectar", command = lambda : connect(lst_box_puertos, root), )
    btn_connect.config(bg = "deep sky blue", fg = "white" ,font =("",font_size))
    btn_connect.config( activebackground = "deep sky blue", activeforeground = "white", font = ("",font_size))
    btn_connect.pack(padx = 15, pady = 15)



    root.mainloop()


def run_select_port():
    w_select_port()
    return send_port

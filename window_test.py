from tkinter import *
from tkinter import ttk

import PIL
from PIL import Image
from PIL import ImageTk

if __name__ == "__main__":


    title_size_font = 16
    content_size_font = 12



    root = Tk()
    root.minsize(500,700)
    #root.maxsize(500,700)
    root.resizable(0,0)

    im = PIL.Image.open("logo.png")
    logo = PIL.ImageTk.PhotoImage(im)


    #frame con padiing 15px
    frame = Frame(root)
    frame.pack(side = "top", anchor = "nw", padx = 15, pady = 15,fill = "both")
    
    #########################################################################
    ##################           Temperatura           ######################
    #########################################################################

    #frame  titulo e imagen
    sub_frame_1 = Frame(frame,)
    #frame.config(bg = "pink")
    sub_frame_1.pack(side = "top", anchor = "nw",fill = "both")
    
    #Label title TEMPERATURA
    lb_title_temp = Label(sub_frame_1, text = "Temperatura",font = ("",title_size_font))
    lb_title_temp.pack(side = "left",anchor = "s")

    #Label IMAGEN LOGO.png
    lb_logo = Label(sub_frame_1, image = logo, )
    lb_logo.pack(side = "right",anchor = "n")

    #frame separador
    frame_2 = Frame(frame,)
    #frame_2.config(bg = "blue")
    frame_2.pack( fill = "both", expand = 1)

    ttk.Separator(frame_2, orient='horizontal').pack(side='top', fill='x') #linea separadora

    lb_temp = Label(frame_2, text = "Temperatura: 200°C/",font = ("",content_size_font))
    lb_temp.pack(side = "left", anchor = "nw", pady = 15)
    
    btn_lower_temp = Button(frame_2, text = "—",font = ("",content_size_font))
    btn_lower_temp.pack(side = "left", anchor = "nw", pady = 10)

    lb_set_temp = Label(frame_2, text = "180°C", font = ("",content_size_font))
    lb_set_temp.pack(side = "left", anchor = "nw", pady = 15)

    btn_higher_temp = Button(frame_2, text = "+",font = ("",content_size_font))
    btn_higher_temp.pack(side = "left", anchor = "nw",pady= 10)

    #########################################################################
    ##################             Archivo             ######################
    #########################################################################
    
    frame_3 = Frame(frame,)
    #frame_3.config(bg = "red")
    frame_3.pack( side ="bottom", fill = "both", expand = 1)
    
    lb_title_archivo = Label(frame_3, text = "Archivo", font=("",title_size_font))
    lb_title_archivo.pack(side = "top",anchor = "nw")

    ttk.Separator(frame_3, orient='horizontal').pack( fill='x') #linea separadora

    bt_select_file = Button(frame_3, text = "Buscar",font = ("",content_size_font))
    bt_select_file.pack(side = "left", pady = 10)

    lb_Select_file = Label(frame_3, text = "Ningun archivo seleccionado", font = ("",content_size_font))
    lb_Select_file.pack(side = "left",pady = 15)

    root.mainloop()
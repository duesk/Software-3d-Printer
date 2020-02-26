from tkinter import *
from tkinter import ttk

import PIL
from PIL import Image
from PIL import ImageTk

if __name__ == "__main__":


    title_size_font = 16
    content_size_font = 12
    color_theme = "paleTurquoise1"
    color_button = "deep sky blue"

    root = Tk()
    root.minsize(500,310)
    #root.maxsize(500,700)
    root.resizable(0,0)
    root.config(bg = color_theme)

    im = PIL.Image.open("logo.png")
    logo = PIL.ImageTk.PhotoImage(im)


    #frame con padiing 15px
    frame = Frame(root)
    frame.config(bg = color_theme)
    frame.pack(side = "top", anchor = "nw", padx = 15, pady = 15,fill = "both")
    
    #########################################################################
    ##################           Temperatura           ######################
    #########################################################################

    #frame  titulo e imagen
    sub_frame_1 = Frame(frame,)
    sub_frame_1.config(bg = color_theme)
    sub_frame_1.pack(side = "top", anchor = "nw",fill = "both")
    
    #Label title TEMPERATURA
    lb_title_temp = Label(sub_frame_1, text = "Temperatura",font = ("",title_size_font),)
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

    lb_temp = Label(frame_2, text = "Temperatura: 200°C/  ",font = ("",content_size_font) )
    lb_temp.config(bg = color_theme)
    lb_temp.pack(side = "left", anchor = "nw", pady = 15)
    
    btn_lower_temp = Button(frame_2, text = "—",font = ("",content_size_font),bg = color_button, fg = "white" )
    btn_lower_temp.pack(side = "left", anchor = "nw", pady = 10)

    lb_set_temp = Label(frame_2, text = "180°C", font = ("",content_size_font))
    lb_set_temp.config(bg = color_theme)
    lb_set_temp.pack(side = "left", anchor = "nw", pady = 15)

    btn_higher_temp = Button(frame_2, text = "+",font = ("",content_size_font),bg = color_button, fg = "white" )
    btn_higher_temp.pack(side = "left", anchor = "nw",pady= 10)

    #########################################################################
    ##################             Archivo             ######################
    #########################################################################
    
    frame_3 = Frame(frame,)
    frame_3.config(bg = color_theme)
    frame_3.pack( side ="top", fill = "both", expand = 1)
    
    lb_title_archivo = Label(frame_3, text = "Archivo", font=("",title_size_font))
    lb_title_archivo.config(bg = color_theme)
    lb_title_archivo.pack(side = "top",anchor = "nw")

    ttk.Separator(frame_3, orient='horizontal').pack( fill='x') #linea separadora

    bt_select_file = Button(frame_3, text = "Buscar",font = ("",content_size_font),bg = color_button, fg = "white" )
    bt_select_file.pack(side = "left", pady = 10)

    lb_Select_file = Label(frame_3, text = "Ningun archivo seleccionado", font = ("",content_size_font))
    lb_Select_file.config(bg = color_theme)
    lb_Select_file.pack(side = "left",pady = 15)
    #########################################################################
    #################             imprimir             ######################
    #########################################################################

    frame_4 = Frame(frame,)
    frame_4.config(bg = color_theme)
    frame_4.pack( side ="top", fill = "both", expand = 1)
    

    ttk.Separator(frame_4, orient='horizontal').pack( fill='x') #linea separadora

    bt_start_print = Button(frame_4, text = "imprimir",font = ("",content_size_font),bg = color_button, fg = "white" )
    bt_start_print.pack(side = "left", pady = 10)

    Label(frame_4, text = "   ", font = ("",content_size_font), bg = color_theme).pack(side = "left",pady = 15)


    bt_cancel = Button(frame_4, text = "cancelar",font = ("",content_size_font),bg = color_button, fg = "white" )
    bt_cancel.pack(side = "left", pady = 10)


    #########################################################################
    #################             imprimir             ######################
    #########################################################################
    frame_5 = Frame(frame,)
    frame_5.config(bg = color_theme)
    frame_5.pack(side= "left", fill = "both", expand = 1)

    progressbar = ttk.Progressbar(frame_5, length = 100, mode = "determinate", style = "red.Horizontal.TProgressbar")
    progressbar.pack(fill = "both", expand = 1, pady = 10)
    progressbar.step(90.0)

    root.mainloop()
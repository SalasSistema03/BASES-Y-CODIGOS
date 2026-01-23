import tkinter
from tkinter import *
from LeePDFyESTAMPA import estampado


#IMPORT APP 2


#IMPORT APP 3



def aplicacion1():
    estampado()

def aplicacion2():
    print('ap2')

def aplicacion3():
    print('ap3')
    

ventana_principal = tkinter.Tk()
ventana_principal.geometry('400x150')
ventana_principal.title('NOMBRE DE LA APLICACION')
#ventana_principal.iconbitmap(rute_icon + 'ICON.ico')

#titulo y texto
label0 = tkinter.Label(ventana_principal,
text= ' API',
bg= 'blue', 
fg= 'white',
font= ('Consolas bold', 20))
label0.grid(row = 0 , column= 0 ,sticky= 'nsew')

#configuracion de la ventanma de los objetos
ventana_objetos = tkinter.Frame(ventana_principal, 
bg = 'green')
ventana_objetos.grid(row=1, column=0, sticky= 'nsew')
Grid.rowconfigure(ventana_principal, index = 1, weight = 1) 
Grid.columnconfigure(ventana_principal, index = 0, weight = 1)

Grid.columnconfigure(ventana_objetos, index = 0, weight = 1)
Grid.columnconfigure(ventana_objetos, index = 0, weight = 1)


#objetos

#etiquetas
label1 = tkinter.Label(ventana_objetos, 
text = 'Estampado', 
bg= 'darkblue', 
fg= 'white',
font= ('Consolas bold', 12))
label2  = tkinter.Label(ventana_objetos, 
text = 'lable2', 
bg= 'darkblue', 
fg= 'white',
font= ('Consolas bold', 12))
label3  = tkinter.Label(ventana_objetos, 
text = 'lable3', 
bg= 'darkblue', 
fg= 'white',
font= ('Consolas bold', 12))

#botones
button1 = Button(ventana_objetos, 
text ='CLICK',
font= ('Consolas', 12),
command= aplicacion1)
button2 = Button(ventana_objetos, 
text ='button2',
font= ('Consolas', 12),
command= aplicacion2)
button3 = Button(ventana_objetos, 
text ='button3',
font= ('Consolas', 12),
command= aplicacion3)


#grid
#etiquetas
label1.grid(row=0, column=0, sticky= 'nsew')
label2.grid(row=1, column=0, sticky= 'nsew')
label3.grid(row=2, column=0, sticky= 'nsew')
#botones
button1.grid(row=0, column=1, sticky= 'nsew')
button2.grid(row=1, column=1, sticky= 'nsew')
button3.grid(row=2, column=1, sticky= 'nsew')







ventana_principal.mainloop()


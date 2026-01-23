import tkinter
from tkinter import *
from descarga import descarga
from LeePDFyESTAMPA import estampado
import os
import sys
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)
from bot import nombrebot
num_bot = nombrebot()

def aplicacion1(num_bot):
    descarga(num_bot)


def aplicacion2():
    print("ap2") 



def aplicacion3(num_bot):
    estampado(num_bot)
   



    

ventana_principal = tkinter.Tk()
ventana_principal.geometry('400x150')
ventana_principal.title('NOMBRE DE LA APLICACION')

#titulo y texto
label0 = tkinter.Label(ventana_principal,
text= ' Aguas Santafesinas ',
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
text = 'DESCARGA', 
bg= 'darkblue', 
fg= 'white',
font= ('Consolas bold', 12))
label2  = tkinter.Label(ventana_objetos, 
text = '- - ', 
bg= 'darkblue', 
fg= 'white',
font= ('Consolas bold', 12))
label3  = tkinter.Label(ventana_objetos, 
text = 'ESTAMPA', 
bg= 'darkblue', 
fg= 'white',
font= ('Consolas bold', 12))

#botones
button1 = Button(ventana_objetos, 
text ='CLICK',
font= ('Consolas', 12),
command= lambda: aplicacion1(num_bot))
button2 = Button(ventana_objetos, 
text ='CLICK',
font= ('Consolas', 12),
command= aplicacion2)
button3 = Button(ventana_objetos, 
text ='CLICK',
font= ('Consolas', 12),
command= lambda: aplicacion3(num_bot))


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


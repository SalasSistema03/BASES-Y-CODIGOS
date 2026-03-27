import tkinter
from tkinter import *
from carga import carga
from LeePDFyESTAMPA import estampado
from descarga import descarga
from ordena import ordenar
import sys
import os
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)
from bot import nombrebot

rute = 'C:/PROGRAMAS/'
rute_txt = rute + "IMPUESTOS/GAS/TXT/"
numero_bot = nombrebot()
#print(f"numero_bot: {numero_bot}")
#now = datetime.now()
#fecha = str(now.year) + "-" + str(now.month).zfill(2) + "-" + str(now.day).zfill(2)
PATH = 'C:/PROGRAMAS/BASES Y CODIGOS/WEB DRIVER/' + "chromedriver.exe"


def desc():
  periodo = completable1.get().zfill(2)
  # Descargar usando el período como argumento
  descarga(periodo, numero_bot)
  
def aplicacion6():
    print("-")

def aplicacion7():
    print ("-")

ventana_principal = tkinter.Tk()
ventana_principal.geometry('650x270')
ventana_principal.title('GAS')
rute_icon = rute + 'BASES Y CODIGOS/INTERFAS GRAFICA/'
#ventana_principal.iconbitmap(rute_icon + 'ICON.ico')

#titulo y texto
label0 = tkinter.Label(ventana_principal,
text= ' GAS',
bg= 'GREY', 
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
text = 'Carga Gas en la pagina', 
bg= 'darkblue', 
fg= 'white',
font= ('Consolas bold', 16))
label2  = tkinter.Label(ventana_objetos, 
text = 'Ordena para imprimir', 
bg= 'darkblue', 
fg= 'white',
font= ('Consolas bold', 16))
label3  = tkinter.Label(ventana_objetos, 
text = 'Estampa', 
bg= 'darkblue', 
fg= 'white',
font= ('Consolas bold', 16))
label4  = tkinter.Label(ventana_objetos, 
text = 'Periodo', 
bg= 'blue', 
fg= 'white',
font= ('Consolas bold', 16))
label8  = tkinter.Label(ventana_objetos, 
text = 'Descarga por lista', 
bg= 'blue', 
fg= 'white',
font= ('Consolas bold', 16))
label9  = tkinter.Label(ventana_objetos, 
text = 'Lista Deuda', 
bg= 'blue', 
fg= 'white',
font= ('Consolas bold', 16))
label10  = tkinter.Label(ventana_objetos, 
text = 'Desvincula Factura', 
bg= 'darkblue', 
fg= 'white',
font= ('Consolas bold', 16))

#completables
completable1 =tkinter.Entry(ventana_objetos,
font= ('Consolas', 16)
)

#botones
button1 = Button(ventana_objetos, 
text ='Click',
font= ('Consolas', 12),
command= carga)
button2 = Button(ventana_objetos, 
text ='Click',
font= ('Consolas', 12),
command= lambda: ordenar(numero_bot))
button3 = Button(ventana_objetos, 
text ='Click',
font= ('Consolas', 12),
command= lambda: estampado(numero_bot))
button5 = Button(ventana_objetos, 
text ='Click',
font= ('Consolas', 12),
command= desc)
button6 = Button(ventana_objetos, 
text ='Click',
font= ('Consolas', 12),
command= aplicacion6)
button7 = Button(ventana_objetos, 
text ='Click',
font= ('Consolas', 12),
command= aplicacion7)


#grid
#etiquetas
label1.grid(row=0, column=0, sticky= 'nsew')
label2.grid(row=1, column=0, sticky= 'nsew')
label3.grid(row=2, column=0, sticky= 'nsew')
label4.grid(row=3, column=0, sticky= 'nsew')
label8.grid(row=7, column=0, sticky= 'nsew')
label9.grid(row=8, column=0, sticky= 'nsew')
label10.grid(row=9, column=0, sticky= 'nsew')
#botones
button1.grid(row=0, column=1, sticky= 'nsew')
button2.grid(row=1, column=1, sticky= 'nsew')
button3.grid(row=2, column=1, sticky= 'nsew')
button5.grid(row=7, column=1, sticky= 'nsew')
button6.grid(row=8, column=1, sticky= 'nsew')
button7.grid(row=9, column=1, sticky= 'nsew')
#completables
completable1.grid(row=3, column=1, sticky= 'nsew')





ventana_principal.mainloop()


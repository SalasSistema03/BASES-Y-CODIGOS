import tkinter
from tkinter import *
#IMPORT APP 1
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import shutil
from getpass import getuser
from os import mkdir
#IMPORT APP 2
import PyPDF2
from PyPDF2 import *
import re
#IMPORT APP 3


usuario = getuser()
rute = 'C:/PROGRAMAS/'
rute_txt = rute + "IMPUESTOS/GAS/TXT/"
now = datetime.now()
fecha = str(now.year) + "-" + str(now.month).zfill(2) + "-" + str(now.day).zfill(2)
pad_g =[]
carpeta_destino = 'C:/Users/' + usuario + '/Desktop/Escritorio/La Setubal'        
ubicacion = carpeta_destino +'/'+ str(fecha)
carpeta_estampado = carpeta_destino +'/'+ 'Estampado ' + str(fecha)

rute = 'C:/PROGRAMAS/'

def aplicacion1():
    PATH = 'C:/PROGRAMAS/BASES Y CODIGOS/WEB DRIVER/' + "chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    gas_web = 'https://www.setubalcoop.com.ar/factura-digital'
    try:
        mkdir(ubicacion)
    except:
        pass
    lasetubal = carpeta_destino + '/' + 'la setubal.txt'
    contador = 0
    with open (lasetubal,'r', encoding ='utf-8') as padron_g:
        line = [linea.split() for linea in padron_g]
    for linea in line:
        pad_g.append(linea)
    for p_g in pad_g:
        print('---------------------------------')
        cont_i = len(pad_g)
        contador += 1
        folio = p_g[0]
        cliente = p_g[1]
        xpath_numero_cliente = '/html/body/main/div/form/div[3]/div[2]/div/div/input'
        try:
                
            driver.get(gas_web)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,xpath_numero_cliente)))
            cliente_in = driver.find_element(By.XPATH, xpath_numero_cliente)
            cliente_in.send_keys(cliente)
            time.sleep(1)
            xpath_buscar = '/html/body/main/div/form/div[3]/div[3]/span/button'
            buscar = driver.find_element(By.XPATH, xpath_buscar)
            buscar.click()
            xpath_descarga = '/html/body/main/div/div[1]/div/span/a'
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,xpath_descarga)))
            descarga = driver.find_element(By.XPATH, xpath_descarga)
            descarga.click()
            time.sleep(5)
            carpeta_descargas = 'C:/Users/'+ usuario +'/Downloads'
            for file in os.listdir(carpeta_descargas):
                fact_cliente = str(cliente) + '_F'
                if file.startswith(fact_cliente):
                    largo = len(fact_cliente)
                    file_cortado = file[0 : largo]
                    if(fact_cliente == file_cortado):
                        filex = file
            source = carpeta_descargas + '/' + filex
            destination = ubicacion + '/' + str(folio) + '_' + str(cliente) + '.pdf'
            shutil.move(source,destination)
        except:
            pass
        porcentaje = round(contador/cont_i*100,2)
        print(str(contador) + '-' + str(cont_i) + ' ' + str(porcentaje) + '%')

def aplicacion2():
    CONTADOR = 0
    listado = []
    try:
        mkdir(carpeta_estampado)
    except:
        pass
    with open(carpeta_destino + '/' + 'la setubal.txt', 'r', encoding = 'utf-8') as f:
        line = [linea.split() for linea in f]
    for linea in line:
        listado.append(linea)   
    for servicio in listado:
        folio = servicio[0]
        cliente = servicio[1]
        watermarkHoja = servicio[2]
        inputfile = ubicacion + '/' +  folio + "_" + cliente + ".pdf"
        outputfile = carpeta_estampado + '/' +  folio + "_" + cliente + ".pdf"
        #print(inputfile)
        watermark = carpeta_destino + '/AUXILIAR/' + "watermark.pdf"
        #print(watermark)
        try:
            with open (inputfile, 'rb') as inputfile1:
                pdf = PyPDF2.PdfReader(inputfile1)
                with open(watermark, "rb") as watermarkfile:
                    watermarkpdf = PyPDF2.PdfReader(watermarkfile)
                    output = PdfWriter()
                    canpage = len(pdf.pages)
                    for numero in range(0, canpage):
                        p = pdf.pages[canpage - 1]  
                        w = watermarkpdf.pages[int(watermarkHoja)-1]
                        p.merge_page(w)
                        Text1 = p.extract_text()

                        
                        #print(Text1)
                        try:
                            deuda = Text1.index('DETALLE ')
                            datos_deuda = Text1[deuda + 41 : deuda + 73]
                            con_deuda = 'Con Deuda'
                        except:
                            con_deuda = ''
                        total_pagar = Text1.index('TOTAL A PAGAR')
                        pagar = Text1[total_pagar + 22 : total_pagar + 37]
                        venc = Text1.index('TOTAL A PAGAR')
                        pagar1 = pagar.index(',')
                        pagar3 = pagar.index('$')
                        pagar4 = pagar[pagar3 : pagar1 + 3]
                        vencimiento = Text1[venc + 15 : venc + 25]
                        medidor = Text1.index('KCAL/M3')
                        med = Text1[medidor + 8 : medidor + 15]
                        periodo = Text1.index('Bimestral')
                        per = Text1[periodo + 9 : periodo + 16]
                        liq = Text1[periodo + 18 : periodo + 36]
                        detalle ="\n"+ folio + " " + cliente + " " +  per + " " + liq + " " + med + ' ' + vencimiento + ' ' + pagar4 + ' ' + con_deuda
                        print(detalle)
                        with open(carpeta_destino +'/' +  "Detalle " + fecha +".txt", "a") as file:
                            file.write(detalle)
                        
                        output.add_page(p)
                        pdfwriter = PyPDF2.PdfWriter()
                        pdfwriter.add_page(p)

                        
                        with open(outputfile, "wb") as outputfilecontent:
                            pdfwriter.write(outputfilecontent)
                            outputfilecontent.close()
        except:
            print('ERROR')



def aplicacion3():
    print('ap3')
    

ventana_principal = tkinter.Tk()
ventana_principal.geometry('400x150')
ventana_principal.title('NOMBRE DE LA APLICACION')
rute_icon = rute + 'BASES Y CODIGOS/INTERFAS GRAFICA/'
ventana_principal.iconbitmap(rute_icon + 'ICON.ico')

#titulo y texto
label0 = tkinter.Label(ventana_principal,
text= ' Titulo',
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
text = 'lable1', 
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
text ='button1',
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


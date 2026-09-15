import tkinter
from tkinter import *
#IMPORT APP 1
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import json
import os
import sys
from datetime import datetime
from os import mkdir
#IMPORT APP 2


base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)
from bot import nombrebot



#rute = 'C:/PROGRAMAS/'
numero_bot = nombrebot()
#print(f"nombre_bot: {numero_bot}")
rute = '//10.10.10.171/Compartida/'
rute_txt = rute + "IMPUESTOS/TGI/TXT/"
rute_tgi = rute + "IMPUESTOS/TGI/"
logo = rute + "IMPUESTOS/TGI/AUXILIARES/logo.jpg"
#numero_bot = "Bot_01"
rute_tgi = rute + "IMPUESTOS/TGI/"

now = datetime.now()
fecha = str(now.year) + "-" + str(now.month) + "-" + str(now.day).zfill(2)
PATH = 'C:/PROGRAMAS/BASES Y CODIGOS/WEB DRIVER/' + "chromedriver.exe"

#----------------------------------------------------------------------------------------------------------------------------------

def aplicacion1():
    try:
        mkdir(rute_tgi + "DESCARGA")
    except:
        pass
    try:
        mkdir(rute_tgi + "TXT")
    except:
        pass 
    chrome_options = webdriver.ChromeOptions() 
    appState = {
    "recentDestinations": [
            {
                "id": "Save as PDF",
                "origin": "local",
                "account": ""
            }
        ],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }
    profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState),"download.default_directory": rute_tgi, "download.prompt_for_download": True, "plugins.always_open_pdf_externally": False}

    chrome_options.add_experimental_option("prefs", profile)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--start-maximized")            

    driver = webdriver.Chrome(options=chrome_options)
    tgi_web = "https://muniweb4.santafeciudad.gov.ar/sat/seg/Login.do?method=anonimo&url=/gde/AdministrarLiqDeuda.do?method=inicializarContr&id=14"

    directorio_descarga = rute_tgi + "DESCARGA"

    # armado de la lista a imprimir
    lista_armada_tgi = []
    contador = 0
    with open(rute_tgi + 'TXT/' + "lista_tgi_"+numero_bot+".txt", 'r') as f:
        lineas = [linea.split() for linea in f]

    for linea in lineas:
        lista_armada_tgi.append(linea)


    for TGI in lista_armada_tgi:
        todos_tgi = len(lista_armada_tgi)
        contador +=1
        folio = TGI[0]
        padron = TGI[1]
        clave = TGI[2]
        adm = TGI[3]
        id_casa = TGI[4]
        
        
        try:
            # entra a la web
            driver.get(tgi_web)
            WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "container"))
            )
            insert_padron = driver.find_element(By.NAME, "cuenta.numeroCuenta")
            insert_clave = driver.find_element(By.NAME, "cuenta.codGesPer")
            aceptar = driver.find_element(By.NAME, "btnAceptar")
            insert_padron.send_keys(TGI[1])
            time.sleep(1)
            insert_clave.send_keys(TGI[2])
            time.sleep(1)
            insert_clave.send_keys(Keys.RETURN)
            aceptar.click()
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "contenido"))
            )
            try:
                selectores = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[2]/table/tbody/tr[1]/th[1]/input")
            except:
                time.sleep(2)
                selectores = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[3]/table/tbody/tr[1]/th[1]/input")
            
            #//*[@id="filter"]/div[2]/table/tbody/tr[1]/th[1]/input
            #for selector in selectores:
            #    selector.click()  
            time.sleep(1)     
            selectores.click() 
            time.sleep(1)
            
            reimpresion = driver.find_element(By.NAME,"btnReimp")
            time.sleep(1)
            reimpresion.click()
            
            # ESPERAR HASTA QUE CONTENIDO ESTE CARGADO
            WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "btnImpRecibos"))
            )
            # selecciona imprimir
            imprimir_ultima = driver.find_element(By.ID,"btnImpRecibos")
            imprimir_ultima.click()
            WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "filter"))
            )


            time.sleep(30)

            pyautogui.press('tab', presses=39,interval=0.20)
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(9)

            
            for _ in range(3):
                pyautogui.hotkey('shift','tab')
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(5)
            
            #escribe nombre de archivo
            descargaEn = directorio_descarga+ "/" + folio + "_" + padron + ".pdf"
            print(descargaEn.replace("/", "\\"))
            pyautogui.write(descargaEn.replace("/", "\\"))


            #se mueve hasta la posicion de la direccion de descarga, la coloca y da enter.
            pyautogui.press("enter")

            # se mueve hasta la posicion de guardar y luego sobreescribe
            time.sleep(0.5)
            pyautogui.press("left")
            pyautogui.press("enter")

            time.sleep(2)
            
        

            
            print(str(contador) + ' / ' + str(todos_tgi) + " " + str(contador/todos_tgi*100) + "%")


            encontrado = folio+" "+padron+" "+clave+" "+adm + " " + id_casa+"\n"
            #with open(rute_tgi + 'tgi_estampar.txt', 'a') as file:
               # file.write(encontrado)
        
                
            
        except:
            try:
                montoXpath = "/html/body/div[1]/div[3]/form/div[2]/h3"
                textoCero = driver.find_element(By.XPATH,montoXpath)
                
                if textoCero.text == "Total: $ 0,00":
                    montosCeros= "\n"+folio+" "+padron+" "+clave+" "+adm + " " +  id_casa
                    with open(rute_tgi + 'Monto_0_tgi_'+ fecha + numero_bot +'.txt', 'a') as file:
                        file.write(montosCeros)
            except:


                no_encontrado="\n"+folio+" "+padron+" "+clave+" "+adm + " " +  id_casa
                with open(rute_tgi + 'no_encontrados_tgi_'+ fecha + numero_bot + '.txt', 'a') as file:
                    file.write(no_encontrado)
                print("Folio:"+ folio + " no encontrado")
                pass
            
 
    print("PROCESO TERMINADO")

    driver.close()
    #os.system('shutdown /p /f')



#----------------------------------------------------------------------------------------------------------------------------------


aplicacion1()
                                            
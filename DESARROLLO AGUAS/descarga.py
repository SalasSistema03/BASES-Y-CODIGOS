from asyncio import Handle
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from getpass import getuser
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager

usuario = getuser()
now = datetime.now()
rute = '//10.10.10.171/Compartida/'
ubicacion = rute + "IMPUESTOS/AGUA/"
pag_agua = 'https://www.aguassantafesinas.com.ar/portal'


def descarga(numero_bot):
    chrome_options = webdriver.ChromeOptions() 
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--start-maximized")            

    driver = webdriver.Chrome(options=chrome_options)
    
    contador = 0
    folio_no_encontrado = ""
    listado = []
    with open(ubicacion + 'TXT/agua_' + str(numero_bot) + '.txt', 'r') as f:
        line = [linea.split() for linea in f]
    for linea in line:
        listado.append(linea) 
    for servicio in listado:
        folio = servicio[0]
        partida = servicio[1]
        suministro = servicio[2]
        adm = servicio[3]
        idCasa = servicio[4]



        month = now.month+1
        if  month == 13:
            month_dir = 1
        else:
            month_dir = month
        validar = True
        while validar:
            try: 
                driver.quit()
                
                time.sleep(2)
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(pag_agua)
                xpath_ver_tu_factura = "/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]"
                WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,xpath_ver_tu_factura)))
                ver_tu_factura = driver.find_element(By.XPATH,xpath_ver_tu_factura)
                ver_tu_factura.click()
                xpath_punto_suministro = "/html/body/div[1]/div[1]/div/div/div[5]/div/div[2]/input"
                WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,xpath_punto_suministro)))
                punto_suministro = driver.find_element(By.XPATH,xpath_punto_suministro)
                punto_suministro.send_keys(suministro)
                xpath_descargar_factura = "/html/body/div[1]/div[1]/div/div/div[5]/div/button[1]"
                WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,xpath_descargar_factura)))
                descargar_factura = driver.find_element(By.XPATH,xpath_descargar_factura)
                descargar_factura.click()
                try:
                    time.sleep(4)
                    WebDriverWait(driver, 2).until_not(EC.presence_of_all_elements_located((By.XPATH,xpath_descargar_factura)))
                    aguas_reporte = folio + ' ' + partida + ' '  + suministro + ' '  + adm + ' ' + idCasa + '\n'
                    with open(ubicacion +  'Aguas con error' + str(numero_bot) + ".txt", "a") as file:
                        file.write(aguas_reporte)
                except:
                    pass
                try:
                    pyautogui.hotkey('ctrl', 's')
                    time.sleep(15)          
                    ubicacionDescargado = ubicacion + "DESCARGA/"
                    print(ubicacionDescargado)
                    pyautogui.typewrite(ubicacionDescargado.replace("/", "\\") + suministro)
                    time.sleep(3)
                    pyautogui.press('enter')
                    time.sleep(17)
                    pyautogui.press('enter')
                    time.sleep(2)
                    

                    
                    
                    aguas_reporte = folio + ' ' + partida + ' '  + suministro + ' '  + adm +  '\n'
                    with open(ubicacion +  'Aguas descargadas_' + str(numero_bot) + ".txt", "a") as file:
                        file.write(aguas_reporte)
                except:
                    aguas_reporte = folio + ' ' + partida + ' '  + suministro + ' '  + adm + ' ' + idCasa + '\n'
                    with open(ubicacion +  'Aguas con error' + str(numero_bot) + ".txt", "a") as file:
                        file.write(aguas_reporte)
                        print(aguas_reporte)
                time.sleep(1)
                validar = False
            except:
                pass
                
        contador_t = len(listado)
        contador += 1
        porcentaje = round(contador/contador_t*100,2)
        print(str(contador) + '/' + str(contador_t) + ' - ' + str(porcentaje) + '%')

        print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


descarga ("Bot_02")
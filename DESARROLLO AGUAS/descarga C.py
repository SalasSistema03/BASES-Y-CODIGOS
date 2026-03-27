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
pag_agua = 'https://www.aguassantafesinas.com.ar/gestiones/wwcuentaasociada.aspx'

#--------------------------------------------------------- logueos por cuenta

gmail_1 = 'adm.impuestos.1@gmail.com' #clave mail admin3108 #clave web salas3108
gmail_2 = 'adm.impuestos.2@gmail.com'
gmail_3 = 'adm.impuestos.3@gmail.com'
gmail_4 = 'adm.impuestos.4@gmail.com'
gmail_5 = 'adm.impuestos.005@gmail.com'
gmail_6 = 'adm.impuestos.6@gmail.com'
gmail_7 = 'adm.impuestos.7@gmail.com'

def cambio_cuenta (c_mail,driver):
    #log out 
    try:
        id_logout="SALIR_MPAGE"
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID,id_logout)))
        logout = driver.find_element(By.ID,id_logout)
        logout.click()
        time.sleep(2)
        driver.refresh()
    except:
        pass
    driver.get(pag_agua)
    xpath_mail_cuenta = '/html/body/form/div[1]/div/div[4]/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/input'
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,xpath_mail_cuenta)))
    insert_cuenta = driver.find_element(By. XPATH, xpath_mail_cuenta)
    time.sleep(1)
    insert_cuenta.send_keys(c_mail)
    time.sleep(1)
    insert_contraseña = driver.find_element(By.XPATH, '/html/body/form/div[1]/div/div[4]/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/div[1]/div/div/div/div/div[3]/div/div/input')
    insert_contraseña.send_keys("salas3108")
    time.sleep(1)
    ingresa = driver.find_element(By.XPATH, '/html/body/form/div[1]/div/div[4]/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/div[1]/div/div/div/div/div[4]/div[2]/div/div/input')
    ingresa.click()

#--------------------------------------------------------- termina logueos por cuenta

def descarga(numero_bot):
    variable_range = 0
    chrome_options = webdriver.ChromeOptions() 
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--start-maximized")            

    driver = webdriver.Chrome(options=chrome_options)
    
    contador = 0
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

    #--------------------------------------------------------- cambios de cuenta
        if variable_range == 0:
            print('Varialbe Range ' + str(variable_range))
            if int(folio) in range(1,500) or int(folio) in range(49000,51000):
                variable_range = 1
                cambio_cuenta(gmail_1,driver) 
            elif int(folio) in range(501,1000):
                variable_range = 2
                cambio_cuenta(gmail_2,driver) 
            elif int(folio) in range(1001,1500):
                variable_range = 3
                cambio_cuenta(gmail_3,driver)
            elif int(folio) in range(1501,2000):
                variable_range = 4
                cambio_cuenta(gmail_4,driver)
            elif int(folio) in range(2001,2500):
                variable_range = 5
                cambio_cuenta(gmail_5,driver)
            elif int(folio) in range(2501,3000):
                variable_range = 6
                cambio_cuenta(gmail_6,driver)
            elif int(folio) in range(3001,3500):
                variable_range = 7
                cambio_cuenta(gmail_7,driver)    
        elif  variable_range == 1:
            if int(folio) in range(0,500):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(501,1000):
                    variable_range = 2
                    cambio_cuenta(gmail_2,driver) 
                elif int(folio) in range(1001,1500):
                    variable_range = 3
                    cambio_cuenta(gmail_3,driver) 
                elif int(folio) in range(1501,2000):
                    variable_range = 4
                    cambio_cuenta(gmail_4,driver) 
                elif int(folio) in range(2001,2500):
                    variable_range = 5
                    cambio_cuenta(gmail_5,driver) 
                elif int(folio) in range(2501,3000):
                    variable_range = 6
                    cambio_cuenta(gmail_6,driver) 
                elif int(folio) in range(3001,3500):
                    variable_range = 7
                    cambio_cuenta(gmail_7,driver)  
        elif  variable_range == 2:
            if int(folio) in range(501,1000):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,500):
                    variable_range = 1
                    cambio_cuenta(gmail_1,driver) 
                elif int(folio) in range(1001,1500):
                    variable_range = 3
                    cambio_cuenta(gmail_3,driver) 
                elif int(folio) in range(1501,2000):
                    variable_range = 4
                    cambio_cuenta(gmail_4,driver) 
                elif int(folio) in range(2001,2500):
                    variable_range = 5
                    cambio_cuenta(gmail_5,driver) 
                elif int(folio) in range(2501,3000):
                    variable_range = 6
                    cambio_cuenta(gmail_6,driver) 
                elif int(folio) in range(3001,3500):
                    variable_range = 7
                    cambio_cuenta(gmail_7,driver)       
        elif  variable_range == 3:
            if int(folio) in range(1001,1500):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,500):
                    variable_range = 1
                    cambio_cuenta(gmail_1,driver) 
                elif int(folio) in range(501,1000):
                    variable_range = 2
                    cambio_cuenta(gmail_2,driver) 
                elif int(folio) in range(1501,2000):
                    variable_range = 4
                    cambio_cuenta(gmail_4,driver) 
                elif int(folio) in range(2001,2500):
                    variable_range = 5
                    cambio_cuenta(gmail_5,driver) 
                elif int(folio) in range(2501,3000):
                    variable_range = 6
                    cambio_cuenta(gmail_6,driver) 
                elif int(folio) in range(3001,3500):
                    variable_range = 7
                    cambio_cuenta(gmail_7,driver)  
        elif  variable_range == 4:
            if int(folio) in range(1501,2000):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,500):
                    variable_range = 1
                    cambio_cuenta(gmail_1,driver) 
                elif int(folio) in range(501,1000):
                    variable_range = 2
                    cambio_cuenta(gmail_2,driver) 
                elif int(folio) in range(1001,1500):
                    variable_range = 3
                    cambio_cuenta(gmail_3,driver) 
                elif int(folio) in range(2001,2500):
                    variable_range = 5
                    cambio_cuenta(gmail_5,driver) 
                elif int(folio) in range(2501,3000):
                    variable_range = 6
                    cambio_cuenta(gmail_6,driver) 
                elif int(folio) in range(3001,3500):
                    variable_range = 7
                    cambio_cuenta(gmail_7,driver)  
        elif  variable_range == 5:
            if int(folio) in range(2001,2500):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,500):
                    variable_range = 1
                    cambio_cuenta(gmail_1,driver) 
                elif int(folio) in range(501,1000):
                    variable_range = 2
                    cambio_cuenta(gmail_2,driver) 
                elif int(folio) in range(1001,1500):
                    variable_range = 3
                    cambio_cuenta(gmail_3,driver) 
                elif int(folio) in range(1501,2000):
                    variable_range = 4
                    cambio_cuenta(gmail_4,driver) 
            
                elif int(folio) in range(2501,3000):
                    variable_range = 6
                    cambio_cuenta(gmail_6,driver) 
                elif int(folio) in range(3001,3500):
                    variable_range = 7
                    cambio_cuenta(gmail_7,driver) 
        elif  variable_range == 6:
            if int(folio) in range(2501,3000):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,500):
                    variable_range = 1
                    cambio_cuenta(gmail_1,driver) 
                elif int(folio) in range(501,1000):
                    variable_range = 2
                    cambio_cuenta(gmail_2,driver) 
                elif int(folio) in range(1001,1500):
                    variable_range = 3
                    cambio_cuenta(gmail_3,driver) 
                elif int(folio) in range(1501,2000):
                    variable_range = 4
                    cambio_cuenta(gmail_4,driver) 
                elif int(folio) in range(2001,2500):
                    variable_range = 5
                    cambio_cuenta(gmail_5,driver) 
                elif int(folio) in range(3001,3500):
                    variable_range = 7
                    cambio_cuenta(gmail_7,driver)  
        elif  variable_range == 7:
            if int(folio) in range(3001,3500):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,500):
                    variable_range = 1
                    cambio_cuenta(gmail_1,driver) 
                elif int(folio) in range(501,1000):
                    variable_range = 2
                    cambio_cuenta(gmail_2,driver) 
                elif int(folio) in range(1001,1500):
                    variable_range = 3
                    cambio_cuenta(gmail_3,driver) 
                elif int(folio) in range(1501,2000):
                    variable_range = 4
                    cambio_cuenta(gmail_4,driver) 
                elif int(folio) in range(2001,2500):
                    variable_range = 5.1
                    cambio_cuenta(gmail_5,driver) 
                elif int(folio) in range(2501,3000):
                    variable_range = 6
                    cambio_cuenta(gmail_6,driver) 
    #--------------------------------------------------------- termina cambios de cuenta    
        month = now.month+1
        if  month == 13:
            month_dir = 1
        else:
            month_dir = month
        xpathConsultaPuntual = "/html/body/form/div[2]/div[2]/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/table/tbody/tr/td[2]/input"
        WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.XPATH, xpathConsultaPuntual)))
        consultaPuntual = driver.find_element(By.XPATH, xpathConsultaPuntual)
        consultaPuntual.click()
        id_frame = 'gxp0_ifrm'
        WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.ID,id_frame)))
        driver.switch_to.frame(driver.find_element(By.ID,id_frame))
        xpath_unidad_facturacion = '/html/body/form/div[2]/div[2]/div[1]/div/div/div/div[3]/div/div/div[2]/div/div/div/div/input'
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,xpath_unidad_facturacion)))
        unidad_facturacion = driver.find_element(By.XPATH,xpath_unidad_facturacion)
        unidad_facturacion.send_keys(suministro)
        
        try:
            xpathBotonConfirmar = '/html/body/form/div[2]/div[2]/div[1]/div/div/div/div[7]/div/input'
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,xpathBotonConfirmar)))
            botonConfirmar = driver.find_element(By.XPATH,xpathBotonConfirmar)
            botonConfirmar.click()
            xpathVerDetalle = '/html/body/form/div[2]/div[2]/div/div[4]/div/div/div/div/div/div/div/div/div[9]/div/input'
            driver.switch_to.default_content()
            """ WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,xpathVerDetalle)))
            time.sleep(3)
            verDetalle = driver.find_element(By.XPATH,xpathVerDetalle)
            verDetalle.send_keys(Keys.ENTER) """
            xpathComprobante = "/html/body/form/div[2]/div[2]/div/div[4]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/ul/li[2]/a/span/span/span"
            #xpathComprobante = '/html/body/form/div[2]/div[2]/div/div[4]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/ul/li[4]/a/span/span/span'
            WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.XPATH,xpathComprobante)))
            time.sleep(2)
            comprobante = driver.find_element(By.XPATH,xpathComprobante)
            comprobante.click()
            time.sleep(6)
            idFechaUno="span_W0024W0007vCOMPFECHAVTO_00010001"
            WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.ID,idFechaUno)))
            fechaUno = driver.find_element(By. ID, idFechaUno)
            fechaUnoText = fechaUno.text[3:5]
            idFechaDos="span_W0024W0007vCOMPFECHAVTO_00020001"
            WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.ID,idFechaDos)))
            fechaDos = driver.find_element(By. ID, idFechaDos)
            fechaDosText = fechaDos.text[3:5]
            idFechaTres="span_W0024W0007vCOMPFECHAVTO_00030001"
            WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.ID,idFechaTres)))
            fechaTres = driver.find_element(By. ID, idFechaTres)
            fechaTresText = fechaTres.text[3:5]

            if int(fechaUnoText) == month_dir:
                idDescarga = "W0024W0007vDESCARGAR_00010001"
            elif int(fechaDosText) == month_dir:
                idDescarga = "W0024W0007vDESCARGAR_00020001"
            elif int(fechaTresText) == month_dir:
                idDescarga = "W0024W0007vDESCARGAR_00030001"
            else:
                "posible error"
                if int(fechaUnoText) == month-1:
                    idDescarga = "W0024W0007vDESCARGAR_00010001"
                elif int(fechaDosText) == month-1:
                    idDescarga = "W0024W0007vDESCARGAR_00020001"
                elif int(fechaTresText) == month-1:
                    idDescarga = "W0024W0007vDESCARGAR_00030001"
                else:
                    print("error")
            
            WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.ID,idDescarga)))
            descargaPdf = driver.find_element(By.ID,idDescarga)
            time.sleep(4)
            descargaPdf.click()
            time.sleep(30)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(3)
            """ try:
                os.mkdir(ubicacion + str(now.year) + ' - ' + str(month_dir).zfill(2))
            except:
                pass """
            
            ubicacionDescargado = ubicacion + "DESCARGA/"
            print(ubicacionDescargado)
            pyautogui.typewrite(ubicacionDescargado.replace("/", "\\") + suministro)
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('esc')  
            time.sleep(1)
            pyautogui.press('left')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('esc')  
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'w')
            driver.switch_to.window(driver.window_handles[0])
            aguas_reporte = folio + ' ' + partida + ' '  + suministro + ' '  + adm +  '\n'
            with open(ubicacion +  'Aguas descargadas_' + str(numero_bot) + ".txt", "a") as file:
                file.write(aguas_reporte)

        except:
            aguas_reporte = folio + ' ' + partida + ' '  + suministro + ' '  + adm + ' ' + idCasa + ' ' + fechaUnoText + ' ' + fechaDosText + ' ' + fechaTresText +'\n'
            with open(ubicacion +  'Aguas con error' + str(numero_bot) + ".txt", "a") as file:
                file.write(aguas_reporte)
                print(aguas_reporte)
        time.sleep(1)
        driver.get(pag_agua)

        contador_t = len(listado)
        contador += 1
        porcentaje = round(contador/contador_t*100,2)
        print(str(contador) + '/' + str(contador_t) + ' - ' + str(porcentaje) + '%')

        print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


#descarga ()
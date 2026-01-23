from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from os import mkdir
import shutil
from os import remove

from getpass import getuser
rute = 'C:/PROGRAMAS/'
rute_txt = rute + "IMPUESTOS/GAS/TXT/"
now = datetime.now()
fecha = str(now.year) + "-" + str(now.month).zfill(2) + "-" + str(now.day).zfill(2)

def descarga(completable1):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)

    gas_web = "https://www.litoral-gas.com.ar/ov/login"
    
    padron_gas = rute_txt + "descarga_objetica.txt"
    contador = 0

    #--------------------------------------------------------- logueos por cuenta
    variable_range = 0
    gmail_1 = 'adm.impuestos.1@gmail.com' #clave mail admin3108 #clave web salas3108
    gmail_2 = 'adm.impuestos.2@gmail.com'
    gmail_3 = 'adm.impuestos.3@gmail.com'
    gmail_4 = 'adm.impuestos.4@gmail.com'
    gmail_5 = 'adm.impuestos.5@gmail.com'
    gmail_6 = 'adm.impuestos.6@gmail.com'
    gmail_7 = 'adm.impuestos.7@gmail.com'

    def cambio_cuenta (c_mail):
        
        try:
            
            inicio_xpath = '/html/body/app-root/div/sdl-menu/div/sdl-header/mat-toolbar/mat-toolbar-row/sdl-user/div/div/div[2]/div'
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,inicio_xpath)))
            inicio = driver.find_element(By.XPATH,inicio_xpath)
            inicio.click()
            time.sleep(5)

            xpath_logout = '/html/body/div[2]/div[2]/div/div/div/button[3]'
            WebDriverWait(driver, 17).until(EC.presence_of_element_located((By.XPATH,xpath_logout)))
            logout = driver.find_element(By.XPATH,xpath_logout)
            logout.click()
            time.sleep(2)

            driver.refresh()
            print('Cambia de CUENTA')

        except:
            pass
        

        driver.get(gas_web)
        """
        try:
            xpath_espera = '/html/body/app-root/div/app-login-page/div[2]/div[1]/div[1]/mat-card/form/mat-card-content/sdl-input/form/mat-form-field/div/div[1]/div[1]/input'
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath_espera)))
            time.sleep(10)
        except:
            print('Pasa por def')
            pass
        """

        #deteccion y estampado de usuario, contraseña y apreta un enter
        mail_cuenta = '/html/body/app-root/div/app-login-page/div[2]/div[1]/div[1]/mat-card/form/mat-card-content/sdl-input/form/mat-form-field/div/div[1]/div[1]/input'
        WebDriverWait(driver, 360).until(EC.presence_of_element_located((By.XPATH,mail_cuenta)))
        insert_cuenta = driver.find_element(By.XPATH,mail_cuenta)
        insert_cuenta.send_keys(c_mail)
        time.sleep(1)
        insert_contraseña = driver.find_element(By.XPATH,"//input[@id='mat-input-1']")
        insert_contraseña.send_keys("salas3108")
        time.sleep(1)
        insert_contraseña.send_keys(Keys.ENTER)
        variable_range = 0
    #--------------------------------------------------------- termina logueos por cuenta


    #ABRE Y ARMA LISTADO PARA BUSCAR POR NOMBRE EL PDF
    pad_g =[]
    with open (padron_gas,'r', encoding ='utf-8') as padron_g:
        line = [linea.split() for linea in padron_g]

    for linea in line:
        pad_g.append(linea)
        

    for p_g in pad_g:
        

        contador_total = len(pad_g)
        
        folio = str(p_g[0])
        cliente = str(p_g[1])
        persona = str(p_g[2])
        adm = str(p_g[3])



#--------------------------------------------------------- cambios de cuenta
        if variable_range == 0:
            
            if int(folio) in range(1,501):
                variable_range = 1
                cambio_cuenta(gmail_1) 
            elif int(folio) in range(501,1001):
                variable_range = 2
                cambio_cuenta(gmail_2)
            elif int(folio) in range(1001,1501):
                variable_range = 3
                cambio_cuenta(gmail_3)
            elif int(folio) in range(1501,2001):
                variable_range = 4
                cambio_cuenta(gmail_4)
            elif int(folio) in range(2001,2501):
                variable_range = 5
                cambio_cuenta(gmail_5)
            elif int(folio) in range(2501,3001):
                variable_range = 6
                cambio_cuenta(gmail_6)
            elif int(folio) in range(3001,3501):
                variable_range = 7
                cambio_cuenta(gmail_7)    

        elif  variable_range == 1:
            if int(folio) in range(0,501):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(501,1001):
                    variable_range = 2
                    cambio_cuenta(gmail_2)
                elif int(folio) in range(1001,1501):
                    variable_range = 3
                    cambio_cuenta(gmail_3)
                elif int(folio) in range(1501,2001):
                    variable_range = 4
                    cambio_cuenta(gmail_4)
                elif int(folio) in range(2001,2501):
                    variable_range = 5
                    cambio_cuenta(gmail_5)
                elif int(folio) in range(2501,3001):
                    variable_range = 6
                    cambio_cuenta(gmail_6)
                elif int(folio) in range(3001,3501):
                    variable_range = 7
                    cambio_cuenta(gmail_7) 

        elif  variable_range == 2:
            if int(folio) in range(501,1001):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,501):
                    variable_range = 1
                    cambio_cuenta(gmail_1) 
                elif int(folio) in range(1001,1501):
                    variable_range = 3
                    cambio_cuenta(gmail_3)
                elif int(folio) in range(1501,2001):
                    variable_range = 4
                    cambio_cuenta(gmail_4)
                elif int(folio) in range(2001,2501):
                    variable_range = 5
                    cambio_cuenta(gmail_5)
                elif int(folio) in range(2501,3001):
                    variable_range = 6
                    cambio_cuenta(gmail_6)
                elif int(folio) in range(3001,3501):
                    variable_range = 7
                    cambio_cuenta(gmail_7)      

        elif  variable_range == 3:
            if int(folio) in range(1001,1501):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,501):
                    variable_range = 1
                    cambio_cuenta(gmail_1) 
                elif int(folio) in range(501,1001):
                    variable_range = 2
                    cambio_cuenta(gmail_2)
                elif int(folio) in range(1501,2001):
                    variable_range = 4
                    cambio_cuenta(gmail_4)
                elif int(folio) in range(2001,2501):
                    variable_range = 5
                    cambio_cuenta(gmail_5)
                elif int(folio) in range(2501,3001):
                    variable_range = 6
                    cambio_cuenta(gmail_6)
                elif int(folio) in range(3001,3501):
                    variable_range = 7
                    cambio_cuenta(gmail_7) 

        elif  variable_range == 4:
            if int(folio) in range(1501,2001):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,501):
                    variable_range = 1
                    cambio_cuenta(gmail_1) 
                elif int(folio) in range(511,1001):
                    variable_range = 2
                    cambio_cuenta(gmail_2)
                elif int(folio) in range(1001,1501):
                    variable_range = 3
                    cambio_cuenta(gmail_3)
                elif int(folio) in range(2001,2501):
                    variable_range = 5
                    cambio_cuenta(gmail_5)
                elif int(folio) in range(2501,3001):
                    variable_range = 6
                    cambio_cuenta(gmail_6)
                elif int(folio) in range(3001,3501):
                    variable_range = 7
                    cambio_cuenta(gmail_7) 

        elif  variable_range == 5:
            if int(folio) in range(2001,2501):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,501):
                    variable_range = 1
                    cambio_cuenta(gmail_1) 
                elif int(folio) in range(501,1001):
                    variable_range = 2
                    cambio_cuenta(gmail_2)
                elif int(folio) in range(1001,1501):
                    variable_range = 3
                    cambio_cuenta(gmail_3)
                elif int(folio) in range(1501,2001):
                    variable_range = 4
                    cambio_cuenta(gmail_4)
                elif int(folio) in range(2501,3001):
                    variable_range = 6
                    cambio_cuenta(gmail_6)
                elif int(folio) in range(3001,3501):
                    variable_range = 7
                    cambio_cuenta(gmail_7) 

        elif  variable_range == 6:
            if int(folio) in range(2501,3001):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,501):
                    variable_range = 1
                    cambio_cuenta(gmail_1) 
                elif int(folio) in range(501,1001):
                    variable_range = 2
                    cambio_cuenta(gmail_2)
                elif int(folio) in range(1001,1501):
                    variable_range = 3
                    cambio_cuenta(gmail_3)
                elif int(folio) in range(1501,2001):
                    variable_range = 4
                    cambio_cuenta(gmail_4)
                elif int(folio) in range(2001,2501):
                    variable_range = 5
                    cambio_cuenta(gmail_5)
                elif int(folio) in range(3001,3501):
                    variable_range = 7
                    cambio_cuenta(gmail_7) 

        elif  variable_range == 7:
            if int(folio) in range(3001,3501):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,501):
                    variable_range = 1
                    cambio_cuenta(gmail_1) 
                elif int(folio) in range(501,1001):
                    variable_range = 2
                    cambio_cuenta(gmail_2)
                elif int(folio) in range(1001,1501):
                    variable_range = 3
                    cambio_cuenta(gmail_3)
                elif int(folio) in range(1501,2001):
                    variable_range = 4
                    cambio_cuenta(gmail_4)
                elif int(folio) in range(2001,2501):
                    variable_range = 5
                    cambio_cuenta(gmail_5)
                elif int(folio) in range(2501,3001):
                    variable_range = 6
                    cambio_cuenta(gmail_6)
#--------------------------------------------------------- termina cambios de cuenta    

        print('------------------------------------------------------------------------------------------------------------------------------------')
        print('Cliente ' + cliente)
        print('Persona ' + persona)

        try:
            #ATENCION CONTRATO CON DEUDA apreta SI
            xpath_deuda_si = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-sdl-dialog/mat-dialog-content/div[2]/div/div/button"
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_deuda_si)))
            deuda_si = driver.find_element(By.XPATH,xpath_deuda_si)
            deuda_si.click()
            xpath_deuda_x = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-sdl-dialog-deuda/div/a"
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath_deuda_x)))
            deuda_x = driver.find_element_by_xpath (xpath_deuda_x)
            deuda_x.click()
        except:
            pass

        try:
            carga_datos = "/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-home-page/div/div[2]/div[1]/mat-card/mat-card-content/div/div[2]/div"
            WebDriverWait(driver, 380).until(EC.presence_of_element_located((By.XPATH, carga_datos)))
            print("paso la carga")
        except:
            pass    

        xpath_casita = '/html/body/app-root/div/sdl-menu/div/sdl-header/mat-toolbar/mat-toolbar-row/sdl-contratos/div/div[1]/div[2]/div'
        xpath_casita2 = '/html/body/app-root/div/sdl-menu/div/sdl-header/mat-toolbar/mat-toolbar-row/sdl-contratos/div/div[1]/div[2]'
        WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, xpath_casita2)))
        seleccion_casita = driver.find_element(By.XPATH,xpath_casita)
        time.sleep(4)
        seleccion_casita.click()

        xpath_num_cliente = '/html/body/app-root/div/sdl-menu/div/sdl-header/mat-toolbar/mat-toolbar-row/sdl-contratos/div/div[2]/div/input'
        WebDriverWait(driver, 380).until(EC.presence_of_element_located((By.XPATH, xpath_num_cliente)))
        inserta_cliente = driver.find_element(By.XPATH,xpath_num_cliente)
        
        numero_cliente_contrato = cliente
        len(numero_cliente_contrato)
        numero_final_cliente = numero_cliente_contrato [0 : len(numero_cliente_contrato)-2]
        inserta_cliente.send_keys(numero_final_cliente)



        try:
            xpath_contrato = '/html/body/app-root/div/sdl-menu/div/sdl-header/mat-toolbar/mat-toolbar-row/sdl-contratos/div/div[2]/ul/li[1]/div/div/div[1]/div'
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_contrato)))
            seleccion_contrato = driver.find_element(By.XPATH,xpath_contrato)
            seleccion_contrato.click()
            
            try:
                #ATENCION CONTRATO CON DEUDA apreta SI
                xpath_deuda_si = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-sdl-dialog/mat-dialog-content/div[2]/div/div/button"
                WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, xpath_deuda_si)))
                deuda_si = driver.find_element(By.XPATH,xpath_deuda_si)
                deuda_si.click()

                xpath_deuda_x = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-sdl-dialog-deuda/div/a"
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath_deuda_x)))
                deuda_x = driver.find_element_by_xpath (xpath_deuda_x)
                deuda_x.click()

            except:
                pass


            xpath_reimprecion_f = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav/div/sdl-sidebar/div/mat-nav-list[1]/mat-expansion-panel/div/div/div/div[1]/a/div/span'
            WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.XPATH, xpath_reimprecion_f)))
            reimprecion_f = driver.find_element(By.XPATH,xpath_reimprecion_f)
            reimprecion_f.click()

            xpath_ultima_factura = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-reprint/div/div[2]/div[2]/mat-card/mat-card-content/sdl-table/table/tbody/tr[1]/td[7]/mdt-table-cell/ld-options-cell/div/sdl-button-loadding/button/span/img'
            WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.XPATH, xpath_ultima_factura)))
            numero_factura_xpath = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-reprint/div/div[2]/div[2]/mat-card/mat-card-content/sdl-table/table/tbody/tr[1]/td[2]/mdt-table-cell'
            numero_factura = driver.find_element(By.XPATH,numero_factura_xpath).text
            periodo_xpath ='/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-reprint/div/div[2]/div[2]/mat-card/mat-card-content/sdl-table/table/tbody/tr[1]/td[3]/mdt-table-cell'
            periodo = driver.find_element(By.XPATH,periodo_xpath).text
            print(periodo)
            importe_xpath ='/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-reprint/div/div[2]/div[2]/mat-card/mat-card-content/sdl-table/table/tbody/tr[1]/td[5]/mdt-table-cell'
            importe = driver.find_element(By.XPATH,importe_xpath).text
            #print(importe)
            len(periodo)
            numero_periodo = periodo [3 : len(periodo)-5].zfill(2)
            #print(numero_periodo)

            num_periodo = completable1
            print('periodo '+ str(num_periodo))

            if numero_periodo == num_periodo:
                ultima_factura = driver.find_element(By.XPATH,xpath_ultima_factura)
                time.sleep(7)
                ultima_factura.click()

                time.sleep(21)

                usuario = getuser()

                f_descargada = 'C:/Users/' + usuario + '/Downloads/'+ 'F' + numero_factura + '.pdf'
                print(f_descargada)
                carpeta_boletas = rute + 'IMPUESTOS/GAS/' + "GAS - "+ fecha
                try:
                    mkdir(carpeta_boletas)
                except:
                    #print('no crea carpeta')
                    pass
                outputfile = carpeta_boletas +'/' + cliente + "_" + persona + ".pdf"

                # Mover el archivo y cambiar el nombre
                shutil.move(f_descargada, outputfile)
                
            
                importes_lista = folio + " " + cliente  + " " + persona + ' ' + importe + ' ' + periodo + ' F' + numero_factura + ' ' + adm + "\n"
                print('IMPORTE ' + 'Folio ' + folio + ' Cliente ' + cliente + ' Persona ' + persona)
                with open(rute + 'IMPUESTOS/GAS/' + "IMPORTE " + fecha + ".txt", "a") as file:
                    file.write(importes_lista)
                    
                try:
                    remove(f_descargada)
                except:
                    print('no borro')
                
                time.sleep(10)
            else:
                folio_fuera_periodo = folio + " " + cliente  + " " + persona + " " + adm + ' ' + periodo + "\n"
                print('fuera de periodo ' + 'Folio ' + folio + ' Cliente ' + cliente + ' Persona ' + persona)
                with open(rute + 'IMPUESTOS/GAS/' + "FUERA DE PERIODO " + fecha + ".txt", "a") as file:
                    file.write(folio_fuera_periodo)
        except:
            folio_no_encontrado = folio + " " + cliente  + " " + persona + " " + adm + "\n"
            print('no se encontro ' + 'Folio ' + folio + ' Cliente ' + cliente + ' Persona ' + persona)
            with open(rute + 'IMPUESTOS/GAS/' + "NO ENCONTRADOS " + fecha + ".txt", "a") as file:
                file.write(folio_no_encontrado)
        
        contador += 1
        print('Procesados ' + str(contador) + '/' + str(contador_total) + ' - Folio ' + str(folio))
        
        driver.get('https://www.litoral-gas.com.ar/ov/site/home')

    print('DONE')
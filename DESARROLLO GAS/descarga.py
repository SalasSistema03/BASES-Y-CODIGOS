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

#rute = 'C:/PROGRAMAS/'
rute = '//10.10.10.171/Compartida/'
rute_txt = rute + "IMPUESTOS/GAS/TXT/"
now = datetime.now()
fecha = str(now.year) + "-" + str(now.month).zfill(2) + "-" + str(now.day).zfill(2)

def descarga(completable1, numero_bot):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(options=options)

 

    #driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
    gas_web = "https://www.litoral-gas.com.ar/ov/login"
    gas_web_r = "https://www.litoralgas.com.ar/ov/site/reprint"
    #gas_principal = "https://www.litoralgas.com.ar/site/noticias/comunicaciones/oficina-virtual/"
    gas_principal = "https://www.litoralgas.com.ar/ov/login"
    padron_gas = rute_txt + "descarga_" + numero_bot + ".txt"
    contador = 0
    #--------------------------------------------------------- logueos por cuenta
    gmail_1 = 'adm.impuestos.1@gmail.com' #clave mail admin3108 #clave web salas3108
    gmail_2 = 'adm.impuestos.2@gmail.com'
    gmail_3 = 'adm.impuestos.3@gmail.com'
    gmail_4 = 'adm.impuestos.4@gmail.com'
    gmail_5 = 'adm.impuestos.5@gmail.com'
    gmail_6 = 'adm.impuestos.6@gmail.com'
    gmail_7 = 'adm.impuestos.7@gmail.com'
    variable_range = 0
    def cambio_cuenta (c_mail):
        try: 
            driver.get(gas_principal)
            xpath_oficina = "/html/body/div[3]/div/section/div/div/div[1]/div/div/div/p[1]/a/img"
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,xpath_oficina)))   
            oficina = driver.find_element(By.XPATH,xpath_oficina)
            oficina.click()
            handles = driver.window_handles
            # Cierra la primera ventana (si hay más de una ventana abierta)
            if len(handles) > 1:
                driver.switch_to.window(handles[0])  # Cambia el foco a la primera ventana
                driver.close()  # Cierra la primera ventana
            driver.switch_to.window(handles[-1])
        except:
            pass
        try:
            #deteccion y estampado de usuario, contraseña y apreta un enter
            mail_cuenta = '/html/body/app-root/div/app-login-page/div[2]/div[1]/div[1]/mat-card/form/mat-card-content/sdl-input/form/mat-form-field/div/div[1]/div[1]/input'
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,mail_cuenta)))
            insert_cuenta = driver.find_element(By.XPATH,mail_cuenta)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//input[@id='mat-input-1']")))
            insert_cuenta.send_keys(c_mail)
            time.sleep(1)
            insert_contraseña = driver.find_element(By.XPATH,"//input[@id='mat-input-1']")
            insert_contraseña.send_keys("salas3108")
            time.sleep(3)
            insert_contraseña.send_keys(Keys.ENTER)
            time.sleep(2)
            driver.refresh()
            """ print("pasa aca")
            time.sleep(10) """
        except:
            try:
                driver.refresh()
                #deteccion y estampado de usuario, contraseña y apreta un enter
                mail_cuenta = '/html/body/app-root/div/app-login-page/div[2]/div[1]/div[1]/mat-card/form/mat-card-content/sdl-input/form/mat-form-field/div/div[1]/div[1]/input'
                WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH,mail_cuenta)))
                insert_cuenta = driver.find_element(By.XPATH,mail_cuenta)
                mail = "/html/body/app-root/div/app-login-page/div[2]/div[1]/div[1]/mat-card/form/mat-card-content/sdl-input/form/mat-form-field/div/div[1]/div"
                #WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//input[@id='mat-input-1']")))
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,mail)))
                insert_cuenta.send_keys(c_mail)
                time.sleep(1)
                contrasenia = "/html/body/app-root/div/app-login-page/div[2]/div[1]/div[1]/mat-card/form/mat-card-content/sdl-password-input/form/mat-form-field/div/div[1]/div[1]"
                insert_contraseña = driver.find_element(By.XPATH,contrasenia)
                #insert_contraseña = driver.find_element(By.XPATH,"//input[@id='mat-input-1']")
                insert_contraseña.send_keys("salas3108")
                time.sleep(3)
                insert_contraseña.send_keys(Keys.ENTER)
                time.sleep(2)
                #driver.refresh()
                """ print("pasa aca")
                time.sleep(10) """
            except:
                pass
            pass
            #
        

    def cambioCuenta (folio, variable_range, gmail_1, gmail_2, gmail_3, gmail_4, gmail_5, gmail_6, gmail_7):
        #print(variable_range)
        if int(folio) in range(1,501):
            if variable_range != 1:
                variable_range = 1
                cambio_cuenta(gmail_1) 
        elif int(folio) in range(501,1001):
            if variable_range != 2:
                variable_range = 2
                cambio_cuenta(gmail_2)
        elif int(folio) in range(1001,1501):
            if variable_range != 3:
                variable_range = 3
                cambio_cuenta(gmail_3)
        elif int(folio) in range(1501,2001):
            if variable_range != 4:
                variable_range = 4
                cambio_cuenta(gmail_4)
        elif int(folio) in range(2001,2501):
            if variable_range != 5:
                variable_range = 5
                cambio_cuenta(gmail_5)
        elif int(folio) in range(2501,3001):
            if variable_range != 6:
                variable_range = 6
                cambio_cuenta(gmail_6)
        elif int(folio) in range(3001,3501):
            if variable_range != 7:
                variable_range = 7
                cambio_cuenta(gmail_7)
        return (variable_range)
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
        empresa = str(p_g[4])
        idCasa = str(p_g[5])
        
        #--------------------------------------------------------- cambios de cuenta
        print('------------------------------------------------------------------------------------------------------------------------------------')
        variable_range = cambioCuenta (folio, variable_range, gmail_1, gmail_2, gmail_3, gmail_4, gmail_5, gmail_6, gmail_7)
        #driver.refresh()
        print(variable_range)
        #--------------------------------------------------------- termina cambios de cuenta        
        print('Cliente ' + cliente)
        print('Persona ' + persona)
        logo_xpath="/html/body/app-root/div/sdl-menu/div/sdl-header/mat-toolbar/mat-toolbar-row/a/img"
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,logo_xpath)))
        time.sleep(8)
        

        xpath_misfacturas = "/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav/div/sdl-sidebar/div/mat-nav-list[1]/mat-expansion-panel/div/div/div/div[1]/a/div"
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,xpath_misfacturas)))
        misfacturas = driver.find_element(By.XPATH,xpath_misfacturas)
        misfacturas.click()
    
        """ text_reimprecion = "Reimpresión de comprobantes"
        WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.LINK_TEXT,text_reimprecion)))
        reimprecion = driver.find_element(By.LINK_TEXT,text_reimprecion)
        reimprecion.click() """

        #driver.get(gas_web_r)
        xpath_ultima_factura = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-mis-facturas/div/div[2]/div[2]/mat-card/mat-card-content/div/div[1]/div/mat-radio-group/mat-radio-button[1]/label/div[2]'
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, xpath_ultima_factura)))
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
        time.sleep(5)
        inserta_cliente.send_keys(int(numero_final_cliente))
        contrato_vigente="-"
        try:
            xpath_contrato = "/html/body/app-root/div/sdl-menu/div/sdl-header/mat-toolbar/mat-toolbar-row/sdl-contratos/div/div[2]/ul/li[1]/div/div"
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_contrato)))
            seleccion_contrato = driver.find_element(By.XPATH,xpath_contrato)
            texto_contrato = driver.find_element(By.XPATH,xpath_contrato).text
            inicioContrato = texto_contrato.index(": ")
            finalContrato = texto_contrato.index("/")
            barracontrato =texto_contrato[finalContrato+1: finalContrato+3]
            verificaContrato = texto_contrato[inicioContrato+2:finalContrato]+barracontrato
            if str(int(cliente)) == verificaContrato:
                seleccion_contrato.click()
                time.sleep(5)
                xpath_misfacturas_pendientes = "/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav/div/sdl-sidebar/div/mat-nav-list[1]/mat-expansion-panel/div/div/div/div[2]/a/div/span"
                WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,xpath_misfacturas_pendientes)))
                misfacturas_pendientes = driver.find_element(By.XPATH,xpath_misfacturas_pendientes)
                misfacturas_pendientes.click()
                WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,xpath_misfacturas)))
                misfacturas.click()
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_ultima_factura)))
                try:
                    contrato_vigente_xpath = "/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-mis-facturas/div/div[2]/div[2]/mat-card/mat-card-header/div/mat-card-subtitle/span"
                    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, contrato_vigente_xpath)))
                    contrato_vigenteS = driver.find_element(By.XPATH,contrato_vigente_xpath).text.replace(" ", "_")
                    try:
                        contrato_vigente = contrato_vigenteS [contrato_vigenteS.index("NO_VIGENTE"):]
                    except:
                        contrato_vigente = contrato_vigenteS [contrato_vigenteS.index("-_VIGENTE")+2:]
                except:
                    pass
                xpath_mostrartodo = "/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-mis-facturas/div/div[2]/div[2]/mat-card/mat-card-content/div/div[1]/div/mat-radio-group/mat-radio-button[2]/label/div[2]"
                WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,xpath_mostrartodo)))
                mostrartodo = driver.find_element(By.XPATH,xpath_mostrartodo)
                time.sleep(3)
                mostrartodo.click()
                numero_factura_xpath = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-mis-facturas/div/div[2]/div[2]/mat-card/mat-card-content/div/sdl-table/table/tbody/tr[1]/td[2]/mdt-table-cell/mdt-text-cell/span'
                WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,numero_factura_xpath)))
                numero_factura = driver.find_element(By.XPATH,numero_factura_xpath).text
                periodo_xpath ='/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-mis-facturas/div/div[2]/div[2]/mat-card/mat-card-content/div/sdl-table/table/tbody/tr[1]/td[3]'
                periodo = driver.find_element(By.XPATH,periodo_xpath).text
                print(periodo)
                importe_xpath ='/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-mis-facturas/div/div[2]/div[2]/mat-card/mat-card-content/div/sdl-table/table/tbody/tr[1]/td[4]/mdt-table-cell/mdt-text-cell/span'
                importe = driver.find_element(By.XPATH,importe_xpath).text
                #print(importe)
                len(periodo)
                numero_periodo = periodo [3 : len(periodo)-5].zfill(2)
                #print(numero_periodo)
                num_periodo = completable1
                print('periodo '+ str(num_periodo))
                if numero_periodo == num_periodo:
                    credito_xpath = "/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-mis-facturas/div/div[2]/div[2]/mat-card/mat-card-content/div/sdl-table/table/tbody/tr[1]/td[7]/mdt-table-cell/mdt-text-cell/span"
                    credito = driver.find_element(By.XPATH,credito_xpath).text
                    if credito !="CREDITO":
                        xpath_descargaFactura = "/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-mis-facturas/div/div[2]/div[2]/mat-card/mat-card-content/div/sdl-table/table/tbody/tr[1]/td[9]/mdt-table-cell/ld-options-cell/div/sdl-button-loadding/button/span/img"
                        descargaFactura = driver.find_element(By.XPATH,xpath_descargaFactura)
                        time.sleep(2)
                        descargaFactura.click()
                        time.sleep(21)      
                        usuario = getuser()
                        f_descargada = 'C:/Users/' + usuario + '/Downloads/'+ 'F' + numero_factura + '.pdf'
                        d_descargada = 'C:/Users/' + usuario + '/Downloads/'+ 'D' + numero_factura + '.pdf'
                        print(f_descargada)
                        print(d_descargada)
                        carpeta_boletas = rute + 'IMPUESTOS/GAS/' + "GAS - "+ fecha
                        carpeta_boletas_p = rute + 'IMPUESTOS/GAS/' + "GAS - "+ fecha + " - PLAN DE PAGOS"
                        try:
                            mkdir(carpeta_boletas)
                        except:
                            #print('no crea carpeta')
                            pass
                        try:
                            mkdir(carpeta_boletas_p)
                        except:
                            #print('no crea carpeta')
                            pass
                        outputfile = carpeta_boletas +'/' + cliente + "_" + persona + ".pdf"
                        outputfilep = carpeta_boletas_p +'/' + folio + "_" + cliente + "_" + persona + ".pdf"
                        # Mover el archivo y cambiar el nombre
                        try:
                            shutil.move(f_descargada, outputfile)
                            importes_lista = folio + " " + cliente  + " " + persona + ' ' + importe + ' ' + periodo + ' F' + numero_factura + ' ' + adm + " " + contrato_vigente + " " + empresa + " " + idCasa +"\n"
                            print('IMPORTE ' + 'Folio ' + folio + ' Cliente ' + cliente + ' Persona ' + persona)
                            with open(rute + 'IMPUESTOS/GAS/' + "IMPORTE " + fecha + "_" + str(numero_bot) + ".txt", "a") as file:
                                file.write(importes_lista)
                        except:
                            shutil.move(d_descargada, outputfilep)
                            importes_lista = folio + " " + cliente  + " " + persona + ' ' + importe + ' ' + periodo + ' F' + numero_factura + ' ' + adm + " " + contrato_vigente + " " + empresa + " " + idCasa +"\n"
                            print('IMPORTE PLAN DE PAGO ' + 'Folio ' + folio + ' Cliente ' + cliente + ' Persona ' + persona)
                            with open(rute + 'IMPUESTOS/GAS/' + "IMPORTE " + fecha + "_" + str(numero_bot) + ".txt", "a") as file:
                                file.write(importes_lista) 
                        try:
                            remove(f_descargada)
                        except:
                            try:
                                remove(d_descargada)
                            except:
                                print('no borro')
                        time.sleep(10)
                    else:
                        importes_lista = folio + " " + cliente  + " " + persona + ' ' + importe + ' ' + periodo + ' F' + numero_factura + ' ' + adm + " " + contrato_vigente + " " + empresa + " " + idCasa +"\n"
                        print('IMPORTE ' + 'Folio ' + folio + ' Cliente ' + cliente + ' Persona ' + persona)
                        with open(rute + 'IMPUESTOS/GAS/' + "IMPORTE a FAVOR" + fecha + "_" + str(numero_bot) + ".txt", "a") as file:
                            file.write(importes_lista)
                else:
                    folio_fuera_periodo = folio + " " + cliente  + " " + persona + " " + adm + " " + empresa + " " + idCasa  + ' ' + periodo + " " + contrato_vigente +"\n"
                    print('fuera de periodo ' + 'Folio ' + folio + ' Cliente ' + cliente + ' Persona ' + persona)
                    with open(rute + 'IMPUESTOS/GAS/' + "FUERA DE PERIODO " + fecha + "_" + numero_bot +  ".txt", "a") as file:
                        file.write(folio_fuera_periodo)
            else:
                credito = driver.find_element(By.XPATH,credito_xpath).text
        except:
            folio_no_encontrado = folio + " " + cliente  + " " + persona + " " + adm + " " + empresa + " " + idCasa + " " + contrato_vigente + "\n"
            print('no se encontro ' + 'Folio ' + folio + ' Cliente ' + cliente + ' Persona ' + persona)
            with open(rute + 'IMPUESTOS/GAS/' + "NO ENCONTRADOS " + fecha + "_" + numero_bot + ".txt", "a") as file:
                file.write(folio_no_encontrado)
        contador += 1
        print('Procesados ' + str(contador) + '/' + str(contador_total) + ' - Folio ' + str(folio))
        driver.get('https://www.litoralgas.com.ar/ov/site/home')
    print('DONE')

""" descarga("01") """
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager

#rute = 'C:/PROGRAMAS/'
rute = '//10.10.10.171/Compartida/'
rute_txt = rute + "IMPUESTOS/GAS/TXT/"
now = datetime.now()
fecha = str(now.year) + "-" + str(now.month).zfill(2) + "-" + str(now.day).zfill(2)

def carga():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(options=options)
         
    gas_web = "https://www.litoral-gas.com.ar/ov/login"

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
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,inicio_xpath)))
            inicio = driver.find_element(By.XPATH,inicio_xpath)
            inicio.click()

            xpath_logout = '/html/body/div[2]/div[2]/div/div/div/button[3]'
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,xpath_logout)))
            logout = driver.find_element(By.XPATH,xpath_logout)
            logout.click()
            time.sleep(2)

            driver.refresh()

        except:
            try: 
                driver.get("https://www.litoral-gas.com.ar/site/noticias/comunicaciones/oficina-virtual/")
                xpath_oficina = "/html/body/div[3]/div/section/div/div/div[1]/div/div/div/p[1]/a/img"
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath_oficina)))   
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
        

        driver.get(gas_web)
        time.sleep (2)
 
        #deteccion y estampado de usuario, contraseña y apreta un enter
        mail_cuenta = '/html/body/app-root/div/app-login-page/div[2]/div[1]/div[1]/mat-card/form/mat-card-content/sdl-input/form/mat-form-field/div/div[1]/div[1]/input'
        WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.XPATH,mail_cuenta)))
        insert_cuenta = driver.find_element(By.XPATH,mail_cuenta)
        insert_cuenta.send_keys(c_mail)
        time.sleep(1)
        insert_contraseña = driver.find_element(By.XPATH,"//input[@id='mat-input-1']")
        insert_contraseña.send_keys("salas3108")
        time.sleep(1)
        insert_contraseña.send_keys(Keys.ENTER)
        variable_range = 0
#--------------------------------------------------------- termina logueos por cuenta

    listado_gas = []

    with open(rute_txt + "listado_carga.txt", "r") as a:
        lista = [linea.split() for linea in a]
    for linea in lista:
        listado_gas.append(linea)
    for GAS in listado_gas:
        folio = GAS[0]
        cliente = GAS[1]
        persona = GAS[2]
        #adm = GAS[3]

#--------------------------------------------------------- cambios de cuenta
        if variable_range == 0:
            
            #print('llega aca')
            if int(folio) in range(1,500):
                #print('aca otro')
                variable_range = 1
                cambio_cuenta(gmail_1) 
            elif int(folio) in range(501,1000):
                variable_range = 2
                cambio_cuenta(gmail_2)
            elif int(folio) in range(1001,1500):
                variable_range = 3
                cambio_cuenta(gmail_3)
            elif int(folio) in range(1501,2000):
                variable_range = 4
                cambio_cuenta(gmail_4)
            elif int(folio) in range(2001,2500):
                variable_range = 5
                cambio_cuenta(gmail_5)
            elif int(folio) in range(2501,3000):
                print('toma este valor')
                variable_range = 6
                cambio_cuenta(gmail_6)
            elif int(folio) in range(3001,3500):
                variable_range = 7
                cambio_cuenta(gmail_7)    

        elif  variable_range == 1:
            if int(folio) in range(0,500):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(501,1000):
                    variable_range = 2
                    cambio_cuenta(gmail_2)
                elif int(folio) in range(1001,1500):
                    variable_range = 3
                    cambio_cuenta(gmail_3)
                elif int(folio) in range(1501,2000):
                    variable_range = 4
                    cambio_cuenta(gmail_4)
                elif int(folio) in range(2001,2500):
                    variable_range = 5
                    cambio_cuenta(gmail_5)
                elif int(folio) in range(2501,3000):
                    variable_range = 6
                    cambio_cuenta(gmail_6)
                elif int(folio) in range(3001,3500):
                    variable_range = 7
                    cambio_cuenta(gmail_7) 

        elif  variable_range == 2:
            if int(folio) in range(501,1000):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,500):
                    variable_range = 1
                    cambio_cuenta(gmail_1) 
                elif int(folio) in range(1001,1500):
                    variable_range = 3
                    cambio_cuenta(gmail_3)
                elif int(folio) in range(1501,2000):
                    variable_range = 4
                    cambio_cuenta(gmail_4)
                elif int(folio) in range(2001,2500):
                    variable_range = 5
                    cambio_cuenta(gmail_5)
                elif int(folio) in range(2501,3000):
                    variable_range = 6
                    cambio_cuenta(gmail_6)
                elif int(folio) in range(3001,3500):
                    variable_range = 7
                    cambio_cuenta(gmail_7)      

        elif  variable_range == 3:
            if int(folio) in range(1001,1500):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,500):
                    variable_range = 1
                    cambio_cuenta(gmail_1) 
                elif int(folio) in range(501,1000):
                    variable_range = 2
                    cambio_cuenta(gmail_2)
                elif int(folio) in range(1501,2000):
                    variable_range = 4
                    cambio_cuenta(gmail_4)
                elif int(folio) in range(2001,2500):
                    variable_range = 5
                    cambio_cuenta(gmail_5)
                elif int(folio) in range(2501,3000):
                    variable_range = 6
                    cambio_cuenta(gmail_6)
                elif int(folio) in range(3001,3500):
                    variable_range = 7
                    cambio_cuenta(gmail_7) 

        elif  variable_range == 4:
            if int(folio) in range(1501,2000):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,500):
                    variable_range = 1
                    cambio_cuenta(gmail_1) 
                elif int(folio) in range(501,1000):
                    variable_range = 2
                    cambio_cuenta(gmail_2)
                elif int(folio) in range(1001,1500):
                    variable_range = 3
                    cambio_cuenta(gmail_3)
                elif int(folio) in range(2001,2500):
                    variable_range = 5
                    cambio_cuenta(gmail_5)
                elif int(folio) in range(2501,3000):
                    variable_range = 6
                    cambio_cuenta(gmail_6)
                elif int(folio) in range(3001,3500):
                    variable_range = 7
                    cambio_cuenta(gmail_7) 

        elif  variable_range == 5:
            if int(folio) in range(2001,2500):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,500):
                    variable_range = 1
                    cambio_cuenta(gmail_1) 
                elif int(folio) in range(501,1000):
                    variable_range = 2
                    cambio_cuenta(gmail_2)
                elif int(folio) in range(1001,1500):
                    variable_range = 3
                    cambio_cuenta(gmail_3)
                elif int(folio) in range(1501,2000):
                    variable_range = 4
                    cambio_cuenta(gmail_4)
                elif int(folio) in range(2501,3000):
                    variable_range = 6
                    cambio_cuenta(gmail_6)
                elif int(folio) in range(3001,3500):
                    variable_range = 7
                    cambio_cuenta(gmail_7) 

        elif  variable_range == 6:
            if int(folio) in range(2501,3000):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,500):
                    variable_range = 1
                    cambio_cuenta(gmail_1) 
                elif int(folio) in range(501,1000):
                    variable_range = 2
                    cambio_cuenta(gmail_2)
                elif int(folio) in range(1001,1500):
                    variable_range = 3
                    cambio_cuenta(gmail_3)
                elif int(folio) in range(1501,2000):
                    variable_range = 4
                    cambio_cuenta(gmail_4)
                elif int(folio) in range(2001,2500):
                    variable_range = 5
                    cambio_cuenta(gmail_5)
                elif int(folio) in range(3001,3500):
                    variable_range = 7
                    cambio_cuenta(gmail_7) 

        elif  variable_range == 7:
            if int(folio) in range(3001,3500):
                print('Varialbe Range ' + str(variable_range))
            else:
                if int(folio) in range(1,500):
                    variable_range = 1
                    cambio_cuenta(gmail_1) 
                elif int(folio) in range(501,1000):
                    variable_range = 2
                    cambio_cuenta(gmail_2)
                elif int(folio) in range(1001,1500):
                    variable_range = 3
                    cambio_cuenta(gmail_3)
                elif int(folio) in range(1501,2000):
                    variable_range = 4
                    cambio_cuenta(gmail_4)
                elif int(folio) in range(2001,2500):
                    variable_range = 5
                    cambio_cuenta(gmail_5)
                elif int(folio) in range(2501,3000):
                    variable_range = 6
                    cambio_cuenta(gmail_6)
#--------------------------------------------------------- termina cambios de cuenta    
    

                          
        
        try:
                #ATENCION CONTRATO CON DEUDA apreta SI
                xpath_deuda_si = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-sdl-dialog/mat-dialog-content/div[2]/div/div/button"
                WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, xpath_deuda_si)))
                deuda_si = driver.find_element(By.XPATH,xpath_deuda_si)
                deuda_si.click()

                xpath_deuda_x = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-sdl-dialog-deuda/div/a"
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath_deuda_x)))
                deuda_x = driver.find_element_by_xpath (xpath_deuda_x)
                deuda_x.click()

        except:
            pass

        try:
            #busca para agregar a nuevas voletas
            #PRECIONA "VINCULAR SUMINISTRO/CONTACTO"
            #vincular_gas = driver.find_element(By.XPATH,'//*[@id="cdk-accordion-child-0"]/div/div/div[2]/a/div/span')
            #vincular_gas.click()
            #xpath_v_s = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav/div/sdl-sidebar/div/mat-nav-list[3]/mat-expansion-panel/div/div/div/div[4]/a/div/span'
            xpath_v_s = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav/div/sdl-sidebar/div/mat-nav-list[2]/mat-expansion-panel/div/div/div/div[6]/a/div/span'
            WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH,xpath_v_s)))
            vincular_suministro = driver.find_element(By.XPATH,xpath_v_s)
            vincular_suministro.click()
            time.sleep(1)

            xpath_a_d = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-matriculados/div/div[2]/div[2]/mat-card/mat-card-content/div/div/sdl-table/div[1]/div[2]/button'
            WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,xpath_a_d)))
            agregar_datos = driver.find_element(By.XPATH,xpath_a_d)
            agregar_datos.click()
            time.sleep(1)
            xpath_n_a = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-matriculados/div/div[2]/div[2]/mat-card/mat-card-content/div/div/form/div[1]/div[1]/div/div/mat-radio-group/mat-radio-button[2]'
            WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,xpath_n_a)))
            no_administra = driver.find_element(By.XPATH,xpath_n_a)
            no_administra.click()
            time.sleep(1)
            xpath_r_t = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-matriculados/div/div[2]/div[2]/mat-card/mat-card-content/div/div/form/div[1]/div[2]/div/div/sdl-select/div/form/mat-form-field/div/div[1]/div[1]/input'
            WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,xpath_r_t)))
            relacion_titular = driver.find_element(By.XPATH,xpath_r_t)
            time.sleep(2)
            relacion_titular.send_keys('Administrador')
            time.sleep(1)
            xpath_num_client = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-matriculados/div/div[2]/div[2]/mat-card/mat-card-content/div/div/form/div[2]/div[1]/sdl-input/form/mat-form-field/div/div[1]/div[1]/input'
            WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,xpath_num_client)))
            numero_c = driver.find_element(By.XPATH,xpath_num_client)
            numero_c.send_keys(cliente)
            time.sleep(1)
            xpath_num_pers = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-matriculados/div/div[2]/div[2]/mat-card/mat-card-content/div/div/form/div[2]/div[2]/sdl-input/form/mat-form-field/div/div[1]/div[1]/input'
            WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,xpath_num_pers)))
            numero_p = driver.find_element(By.XPATH,xpath_num_pers)
            numero_p.send_keys(persona)
            time.sleep(1)
            xpath_terminos = '/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-matriculados/div/div[2]/div[2]/mat-card/mat-card-content/div/div/form/div[4]/div/mat-checkbox/label/div'
            WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,xpath_terminos)))
            terminos = driver.find_element(By.XPATH,xpath_terminos)
            terminos.click()
            time.sleep(1)
            xpath_vinc ='/html/body/app-root/div/sdl-menu/div/mat-sidenav-container/mat-sidenav-content/div/div[1]/app-matriculados/div/div[2]/div[2]/mat-card/div/div[2]/button/span'
            WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,xpath_vinc)))
            vincular = driver.find_element(By.XPATH,xpath_vinc)
            vincular.click()
            time.sleep(1)
            
            element_to_find = '/html/body/div[2]/div/div/snack-bar-container/sdl-alert/div/span[2]'
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,element_to_find)))
            except:
                pass
            
            try:
                time.sleep(7)
                if driver.find_element(By.XPATH,element_to_find):
                    
                    text_element = driver.find_element(By.XPATH,element_to_find)
                    text_find = text_element.text
                    #print(text_find)
                    no_encontrados = "\n" + folio + ";" + cliente + ";" + persona + ";" + text_find
                    with open(rute + 'IMPUESTOS/GAS/CARGA/' + "Detalle_carga_" + "_" + fecha + ".txt", "a") as file:
                        file.write(no_encontrados)
                        print ('Folio ' + folio + " " + text_find)
                        
            except:
                
                no_encontrados = "\n" + folio + ";" + cliente + ";" + persona + ";" + "ERROR"
                with open(rute + 'IMPUESTOS/GAS/CARGA/' + "Detalle_carga_" + "_" + fecha + ".txt", "a") as file:
                    file.write(no_encontrados)
                    print ('Folio ' + folio + " " + "ERROR")

            driver.get(gas_web)
            
            try:
                xpath_close_deuda = "/html/body/div[2]/div[2]/div/mat-dialog-container/app-sdl-dialog-deuda/div/a/i"
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_close_deuda)))
                print("paso la close deuda")
                close_deuda = driver.find_element(By.XPATH,xpath_close_deuda)
                close_deuda.click()
                print("click")
            except:
                pass

            print('------------------------------------------------')
            time.sleep(3)
            pass

        finally:
            time.sleep(1)
    print ("TERMINADO")
    driver.close()
#carga()
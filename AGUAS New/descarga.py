from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pyautogui
bot = "Bot_01"
cuenta = 0
cuenta_actual = 0
order = []
#ruta_descarga = "C:\\Users\\santi\\Desktop\\AGUAS\\DESCARGAS"
#ruta_descarga = "C:/PROGRAMAS/IMPUESTOS/GAS/TXT/"
ruta_descarga = "\\\\10.10.10.171\\Compartida\\IMPUESTOS\\AGUA\\TXT"
# Configuración del navegador
options = webdriver.ChromeOptions()
# options.add_argument('--headless') # Descomenta si no quieres ver la ventana
driver = webdriver.Chrome(options=options)
driver.maximize_window()
#analiza numero de folio para camviar de vuenta
""" def cambio_cuenta (folio, cuenta, cuenta_actual):
    folio = int(folio)
    #si el folio es menor a 500 entonces es uno, si el folio es mayor de 500 pero menor de 1000 entonces 2 sino 3
    if 1 <= folio <= 500:
        cuenta = 1
    elif 501 <= folio <= 1000:
        cuenta = 2
    elif 1001 <= folio <= 1500:
        cuenta = 3
    elif 1501 <= folio <= 2000:
        cuenta = 4
    elif 2001 <= folio <= 2500:
        cuenta = 5
    elif 2501 <= folio <= 3000:
        cuenta = 6
    else:
        cuenta = None
    return cuenta """

with open ("agua_"+bot+".txt", "r") as n_list:
    lines = [line.split() for line in n_list]
for line in lines:
    order.append(line)
total_procesos = len(lines)
contador = 0
for orden in order:
    contador = contador + 1
    folio = orden[0]
    partida = orden[1]
    punto = orden[2]
    admin = orden[3]
    id_casa = orden[4]
    print(folio)
    if int(folio) > 50000:
        fol = str(folio)
        folio = int(folio)-50000
    else:
        fol = folio
    """ cuenta = cambio_cuenta(folio, cuenta, cuenta_actual) """
    

    fecha_mas_grande_obj = None
    posicionFactura = None
    if cuenta != cuenta_actual:
        cuenta_actual = cuenta
        print ("cambio de cuenta")
        try:
            driver.quit()
            driver = webdriver.Chrome(options=options)
            driver.maximize_window()
            # 1. Entrar a la web
            url = "https://ov.aguassantafesinas.com.ar/oficina-virtual/login"
            driver.get(url)
            # 2. Esperar a que aparezcan los XPATHs y loggearse
            # Reemplaza los XPATH con los reales de tu sitio
            id_user = "email"
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, id_user)))
            driver.find_element(By.ID, id_user).send_keys("adm.impuestos."+str(cuenta)+"@gmail.com")
            id_pass = "password"
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, id_pass)))
            driver.find_element(By.ID, id_pass).send_keys("salas3108")
            xpath_login = "/html/body/div[1]/div[3]/div/div/div[2]/div/div[3]/form/div[3]/button"
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_login)))
            driver.find_element(By.XPATH, xpath_login).click()
            #ya ingreso
            xpath_mis_facturas = "/html/body/div[1]/div[1]/div/nav/ul/li[3]/button/span"
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_mis_facturas)))
            driver.find_element(By.XPATH, xpath_mis_facturas).click()
            xpath_descarga_tus_comprobantes = "/html/body/div[1]/div[4]/main/div/div/div[3]/div/div[6]"
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_descarga_tus_comprobantes)))
            driver.find_element(By.XPATH, xpath_descarga_tus_comprobantes).click()
        except:
            pass
    #abre listado
    xpath_listado = "/html/body/div[1]/div[4]/main/div/div/div[3]/div[1]/div[1]/button"
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_listado)))
    time.sleep(5)
    try:
        driver.find_element(By.XPATH, xpath_listado).click()
    except:
        pyautogui.press("esc")
        time.sleep(5)
        driver.find_element(By.XPATH, xpath_listado).click()
    dropdown_element = driver.find_element(By.XPATH, xpath_listado)
    texto_a_buscar = "Cargar"
    xpath_opcion = f"//*[contains(text(), '{texto_a_buscar}')]"
    #repetir esto 40 veces
    try:
        for i in range(40):
            opcion = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath_opcion)))
            opcion.click()
            #time.sleep(1)
            #print(f"Click {i+1}")
    except:
        pass
    punto_a_buscar = str(int(punto))
    print(str(punto_a_buscar))
    xpath_opcion = f"//*[contains(text(), '{punto_a_buscar}')]"
    try:
        opcion = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath_opcion)))
        opcion.click()
        time.sleep(5)
        print("punto encontrado")
        xpath_factura_descargar = ""
        try:
            for i in range(3):
                xpath_factura = "/html/body/div[1]/div[4]/main/div/div/div[3]/div[2]/div[1]/div[1]/table/tbody/tr[" + str(i+1) + "]/td[3]"
                factura = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_factura)))
                fecha_actual_texto = factura.text
                print("selecciona la factura" + str(i+1))
                anio = fecha_actual_texto.split("-")[1]
                mes = fecha_actual_texto.split("-")[0]
                fechafactura = anio + mes
                # 3. Comparamos con la que ya teníamos guardada
                if fecha_mas_grande_obj is None or fechafactura > fecha_mas_grande_obj:
                    fecha_mas_grande_obj = fechafactura
                    posicionFactura = i+1
                    xpath_factura_descargar = "/html/body/div[1]/div[4]/main/div/div/div[3]/div[2]/div[1]/div[1]/table/tbody/tr[" + str(posicionFactura) + "]/td[6]/div/button"
        except:
            print("hay menos de 3 facturas")
        print("descarga_factura")
        time.sleep(2)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, xpath_factura_descargar)))
        driver.find_element(By.XPATH, xpath_factura_descargar).click()
        time.sleep(8)
        #apretar 17 veces tab
        #pyautogui.press('tab', presses=15, interval=0.1)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(9)
        ruta_a_descargar = ruta_descarga + "\\" + punto + ".pdf"
        pyautogui.write(ruta_a_descargar)
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(4)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.press("esc")
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'w')
        with open("agua_"+bot+"_encontrados.txt", "a") as n_list:
            n_list.write(fol + " " + partida + " " + punto + " " + admin + " " + id_casa + " " + "cuenta_"+str(cuenta) + "\n")
    except:
        with open("agua_"+bot+"_no_encontrados.txt", "a") as n_list:
            n_list.write(fol + " " + partida + " " + punto + " " + admin + " " + id_casa + " " + "cuenta_"+str(cuenta) + "\n")
    porcentual = (contador / total_procesos) * 100
    print(str(contador) + "/" + str(total_procesos) + " - " + str(porcentual) + "%")
print("fin")
# Mantener el navegador abierto un momento o cerrarlo
driver.quit()
pass
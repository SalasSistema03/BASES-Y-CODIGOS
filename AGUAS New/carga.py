from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pyautogui
bot = "Bot_04"
cuenta = 0
cuenta_actual = 0
order = []
adm.impuestos.1@gmail.com
SALAS3108
ruta_descarga = "C:\\Users\\santi\\Desktop\\AGUAS\\DESCARGAS"

# Configuración del navegador
options = webdriver.ChromeOptions()
# options.add_argument('--headless') # Descomenta si no quieres ver la ventana
driver = webdriver.Chrome(options=options)
driver.maximize_window()

#analiza numero de folio para camviar de vuenta
def cambio_cuenta (folio, cuenta, cuenta_actual):
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
    return cuenta

with open ("agua_"+bot+".txt", "r") as n_list:
    lines = [line.split() for line in n_list]
for line in lines:
    order.append(line)
for orden in order:
        folio = orden[0]
        fol = folio
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
            
        cuenta = cambio_cuenta(folio, cuenta, cuenta_actual)
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
            except:
                pass
        
        #abre listado
        time.sleep(3)
        xpath_gestionar_suministro = "/html/body/div[1]/div[1]/div/nav/ul/li[2]/button/span"
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_gestionar_suministro)))
        driver.find_element(By.XPATH, xpath_gestionar_suministro).click()
        time.sleep(3)
        xpath_input_punto = "/html/body/div[1]/div[4]/main/div/div/div[2]/div[1]/div[2]/div[2]/div/div/input"
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_input_punto)))
        time.sleep(3)
        driver.find_element(By.XPATH, xpath_input_punto).send_keys(punto)
        xpath_buscar = "/html/body/div[1]/div[4]/main/div/div/div[2]/div[1]/div[2]/div[2]/div/div/button"
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_buscar)))
        driver.find_element(By.XPATH, xpath_buscar).click()
        xpath_agregar = "/html/body/div[4]/div[2]/div/div/div[2]/button"
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_agregar)))
        driver.find_element(By.XPATH, xpath_agregar).click()
        xpath_mesnaje = "/html/body/div[2]/ol/li"
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_mesnaje)))
        mensaje = driver.find_element(By.XPATH, xpath_mesnaje).text
        print(mensaje)
        lineas = mensaje.strip().splitlines()
        if len(lineas) >= 2:
            titulo = lineas[0].strip()   # "Suministro asociado"
            mensaje = lineas[1].strip()  # "Suministro 729218 asociado correctamente"

            mensaje = titulo + " " + mensaje
        try:
            xpath_cerrar_modal = "/html/body/div[4]/button/svg"
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_cerrar_modal)))
            driver.find_element(By.XPATH, xpath_cerrar_modal).click()
        except:
            pass
        with open("agua_"+bot+"_cargados.txt", "a") as n_list:
            n_list.write(fol + ";" + partida + ";" + punto + ";" + admin + ";" + id_casa + ";" + mensaje + "\n")
        driver.get("https://ov.aguassantafesinas.com.ar/oficina-virtual/oficina")

print("fin")
# Mantener el navegador abierto un momento o cerrarlo
driver.quit()
pass
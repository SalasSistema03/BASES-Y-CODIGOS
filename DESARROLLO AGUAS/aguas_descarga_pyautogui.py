import pyautogui
import time
import pyperclip
numero_bot = "01"
""" fecha de hoy mes """
factura_mes = ""
mes_actual = time.strftime("%m")
anio_actual = time.strftime("%Y")
if int(mes_actual) % 2 == 0:
    factura_mes = int(int(mes_actual)/2)
else:
    factura_mes = int((int(mes_actual) + 1)/2)

# Esperar 5 segundos para que puedas posicionar el cursor donde necesites
time.sleep(3)
""" \\10.10.10.171\Compartida\IMPUESTOS\AGUA """
ruta_descarga = "\\\\10.10.10.171\\Compartida\\IMPUESTOS\\AGUA\\DESCARGA"
ruta_txt = "\\\\10.10.10.171\\Compartida\\IMPUESTOS\\AGUA\\TXT\\agua_Bot_" + numero_bot + ".txt"
ruta_txt_info = "\\\\10.10.10.171\\Compartida\\IMPUESTOS\\AGUA"


def obtener_texto_pagina():
    # 1. Seleccionar todo el texto de la página (Ctrl + A)
    pyautogui.hotkey('ctrl', 'a')  # Usa 'command' en Mac
    time.sleep(3)
    # 2. Copiar al portapapeles (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    # 3. Guardar el texto en una variable de Python
    texto_pagina = pyperclip.paste()
    time.sleep(2)
    pyautogui.press('right')
    return texto_pagina

def espera_hasta(texto):
    while True:
        print("texto =", texto)
        texto_pagina = obtener_texto_pagina()
        if texto in texto_pagina:
            
            break
        time.sleep(1)


suministros_asociados = 1
gestionar_suministro = "ov.aguassantafesinas.com.ar/oficina-virtual/oficina/gestionar-suministros"
oficina = "ov.aguassantafesinas.com.ar/oficina-virtual/oficina"
facturas = "ov.aguassantafesinas.com.ar/oficina-virtual/oficina/facturas"
#comprobantes = "ov.aguassantafesinas.com.ar/oficina-virtual/oficina/facturas/comprobantes"
with open(ruta_txt, 'r') as f:
    line = [linea.split() for linea in f]   
listado = []
for linea in line:
    listado.append(linea) 
for servicio in listado:
    folio = servicio[0]
    partida = servicio[1]
    sum = int(servicio[2])
    #sum = int("756351")
    suministro = str(sum)
    adm = servicio[3]
    idCasa = servicio[4]
    
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write(gestionar_suministro)
    texto = "Suministros Asociados ("
    pyautogui.press('enter')
    espera_hasta(texto)
    

    while int(suministros_asociados) != 100:
        texto_pagina = obtener_texto_pagina()
        indice_suministros_asociados = texto_pagina.find("Suministros Asociados")
        time.sleep(1)
        suministros_asociados = texto_pagina[indice_suministros_asociados+23:indice_suministros_asociados+24]
        print(suministros_asociados)
        if int(suministros_asociados) == 0:
            break
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.write('Suministros Asociados')
        time.sleep(2)
        pyautogui.press('esc')
        time.sleep(2)
        pyautogui.press('tab')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('tab')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write(gestionar_suministro)
        pyautogui.press('delete')
        texto = "Suministros Asociados ("
        pyautogui.press('enter')
        espera_hasta(texto)
        
        
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write(gestionar_suministro)
    texto = "Suministros Asociados ("
    pyautogui.press('enter')
    espera_hasta(texto)
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('por calle y altura')
    time.sleep(2)
    pyautogui.press('esc')
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(suministro)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write(facturas)
    texto = "Periodo - Cuota"
    pyautogui.press('enter')
    espera_hasta(texto)
    texto_pagina = obtener_texto_pagina()
    index = texto_pagina.find("Punto de Suministro:")
    finPunto = len(suministro)
    punto_de_suministro = texto_pagina[index + 22 : index + 22 + finPunto]
    time.sleep(0.5)
    if punto_de_suministro == suministro:
        """ ===================== ACAAAAAAAAAA ANTES SE DIRIJIA A COMPROBANTES ======================="""
        pyautogui.hotkey('ctrl','f')
        texto_pagar = "Ordenar por fecha"
        pyautogui.write(texto_pagar)
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('esc')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        #texto_pagar = "Pagar"
        pyautogui.hotkey('ctrl','f')
        pyautogui.write('Pagar')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
       # pyautogui.press('enter')
       # time.sleep(0.5)
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.hotkey('shift','tab')
        time.sleep(1)
        pyautogui.press('enter')

        #pyautogui.hotkey('ctrl', 'l')
        #pyautogui.write(comprobantes)
        """ texto = "Periodo - Cuota"
        pyautogui.press('enter')
        espera_hasta(texto)

        texto_pagina = obtener_texto_pagina()
        factura_buscar = str(factura_mes).zfill(2) + "-" + anio_actual
        index_factura = texto_pagina.find(factura_buscar)
        factura_encontrada = texto_pagina[index_factura:index_factura + len(factura_buscar)]
        if factura_encontrada == factura_buscar:
            pyautogui.hotkey('ctrl', 'f')
            pyautogui.write(factura_buscar)
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(1)
            pyautogui.press('tab')
            texto = "Mi Suministro"
            pyautogui.press('enter') """
            

        time.sleep(6)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(3)
        pyautogui.typewrite(ruta_descarga.replace("/", "\\") + "\\" + suministro)
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('esc')  
        time.sleep(2)
        pyautogui.press('left')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('esc')  
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(3)
        
        ruta_txt_info_limpia = ruta_txt_info.replace("/", "\\")
        with open(ruta_txt_info_limpia + "\Encontrados " + time.strftime("%d-%m-%Y") +numero_bot+ ".txt", "a") as f:
            f.write(folio + " " + partida + " " + suministro + " " + adm + "\n")


        """ else:
            #print("La factura no se encontró")
            ruta_txt_info_limpia = ruta_txt_info.replace("/", "\\")
            with open(ruta_txt_info_limpia + "\\NO_ENCONTRADOS_ENCONTRADOS " + time.strftime("%d-%m-%Y") + numero_bot+ ".txt", "a") as f:
                f.write(folio + " " + partida + " " + suministro + " " + adm + "\n") """
        
    else:
        #print("El punto de suministro no coincide con el esperado")
        ruta_txt_info_limpia = ruta_txt_info.replace("/", "\\")
        with open(ruta_txt_info_limpia + "\AGUAS_CON_ERROR " + time.strftime("%d-%m-%Y") + numero_bot+ ".txt", "a") as f:
            f.write(folio + " " + partida + " " + suministro + " " + adm + "\n")


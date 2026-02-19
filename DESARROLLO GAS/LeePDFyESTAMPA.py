import time
import PyPDF2
from PyPDF2 import PdfWriter
from datetime import datetime
from os import mkdir
from CREADOR import create_pdf
import os
import re


rute = '//10.10.10.171/Compartida/'
rute_txt = rute + "IMPUESTOS/GAS/TXT/"
rute_gas = rute + "IMPUESTOS/GAS/"
logo = rute + "IMPUESTOS/GAS/AUXILIARES/logo.jpg"

now = datetime.now()
date = str(now.year) + "-" + str(now.month).zfill(2) + "-" + str(now.day).zfill(2)
#fecha_txt = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
#print(fecha_txt)    
#VARIABLE DE DOCUMENTO TXT PARA INTRODUCIR LISTADO
#filename =  rute_txt + "padron_estampado.txt"




#BUSQUEDA DEL ARCHIVO
listado = []
def estampado(numero_bot):
    contador = 0
    filename = rute + "IMPUESTOS/GAS/IMPORTE " + date + "_" + str(numero_bot) + ".txt"
    with open(rute + "IMPUESTOS/GAS/IMPORTES - Lectura " + date + "_" + str(numero_bot) + ".txt", "a") as file:  
        valores_imp ="\n"+ "Folio" + ";" +  "Cliente" + ";" + "Persona" + ";" + "Administra" + ";" + "Estado Contrato"  + ";" + "Empresa" + ";" + "Id Casa" + ";" + "Numero de Liquidacion" +";"+ "Monto" + ";" + "Vencimiento"  + ";" + "Dias Liquidados" + ";" + "Periodo" + ";" + "Deuda" + ";" + "Descripcion"
        file.write(valores_imp)

    with open(filename, 'r') as f:
        line = [linea.split() for linea in f]
    for linea in line:
        listado.append(linea)
    #SE DECLARAN LAS VARIABLES QUE ESTAN DENTRO DE LA LISTA QUE SE OBTUVO DEL TXT     
    for servicio in listado:
        folio = servicio[0]
        cliente = servicio[1]
        persona = servicio[2]
        adm = servicio[7]
        vigente = servicio[8]
        empresa = servicio[9]
        id_casa = servicio[10]
        if empresa == "1":
            emp = ""
        elif empresa == "2":
            emp = "CAN_"
        elif empresa == "3":
            emp = "TRIB_"
        #id_casa = servicio[4]
        #SE DETERMINAN LAS VARIABLES PARA LA INTRODUCCION DEL CODIGO DE BARRAS
        inputfile = rute_gas + "GAS - " + date + "/" + cliente + "_" + persona + ".pdf"
        print(inputfile)
        print(folio)

        #ABRE LOS PDF Y ESTAMPA EL CODIGO DE BARRA SEGUN PAGINAS DEL ARCHIVO DE CODIGO DE BARRA
        try:
            with open (inputfile, "rb") as inputfile1:
                pdf = PyPDF2.PdfReader(inputfile1)
                output = PdfWriter()
                canpage = len(pdf.pages)
                for numero in range(0, 1):
                    p = pdf.pages[numero]
                    contenido = p.extract_text() 
                    #print(contenido)
                    vencidainicio = contenido.index("TOTAL A PAGAR hasta el ")
                    fechavencidas = contenido[ vencidainicio + 23 : vencidainicio + 33]
                    vencidasdia = contenido[ vencidainicio + 23 : vencidainicio + 25]
                    vencidasmes = contenido[ vencidainicio + 26 : vencidainicio + 28]
                    print(vencidasdia)
                    print(vencidasmes)
                    mesAhora = int(str(now.month).zfill(2))

                    if mesAhora == 12:
                        mesAhora = 1
                    if mesAhora <= int(vencidasmes):
                        diaAhora = int(str(mesAhora) + str(now.day).zfill(2))
                        diaVence = int(str(vencidasmes) + str(vencidasdia))
                        if diaAhora <= diaVence:
                            try:
                                indiceLiq = contenido.index('Bimestre')
                                liquidacion = contenido[indiceLiq -19 : indiceLiq + 16]
                                print(liquidacion)
                            except:
                                liquidacion = "Comercial "
                                print(liquidacion)
                            try:
                                indiceCodigoBarras = contenido.index('81408')
                                codigoBarras = contenido[indiceCodigoBarras : indiceCodigoBarras + 44]
                                print(codigoBarras)
                            except:
                                codigoBarras = "0".zfill(44)
                            monto = int(codigoBarras[14:26])
                            #print(monto)
                            dia = codigoBarras[26:28]
                            mes = codigoBarras[28:30]
                            anio = codigoBarras[30:34]
                            fechaFactura = dia + "/" + mes + "/" + anio
                            #print(fechaFactura)


                            diasLiquidacion = contenido.index('Y APLICADA')
                            diasLiq = contenido[diasLiquidacion +10 : diasLiquidacion + 14]
                            #print(diasLiq)
                            #print(contenido)
                            # Utilizamos una expresión regular para encontrar todas las ocurrencias de "R" en el texto
                            patron = r' R '

                            # Buscar todas las coincidencias en el texto
                            coincidencias = re.finditer(patron, contenido)

                            # Almacenar los índices de las ocurrencias de "R" en una lista
                            indices_r = [coincidencia.start() for coincidencia in coincidencias]

                            # Imprimir los índices de las ocurrencias de "R"
                            #print("Índices de 'R':", indices_r)
                            try:
                                inicioI = indices_r[0]
                                inicioF = indices_r[1]
                                indiceDesde = contenido[inicioI -10 : inicioI]
                                indiceHasta = contenido[inicioF - 10 : inicioF]
                            except:
                                try:
                                    inicioF = indices_r[0]
                                    iniciaEncontrarA = contenido[indices_r[0]-50 : inicioF+2]
                                    inicioA = iniciaEncontrarA.index(r' A ')-10
                                    indiceDesde = iniciaEncontrarA [inicioA:inicioA+10]
                                    indiceHasta = contenido[inicioF - 10 : inicioF]
                                except:
                                    inicioI = indices_r[0]
                                    iniciaEncontrarA = contenido[indices_r[0] : inicioF+50]
                                    inicioA = iniciaEncontrarA.index(r' A ')
                                    indiceHasta = iniciaEncontrarA [inicioA-10:inicioA]
                                    indiceDesde = contenido[inicioF - 10 : inicioF]

                            #print(indiceDesde)
                            #print(indiceHasta)

                            desdeHasta = indiceDesde + " al " + indiceHasta
                            print(desdeHasta)
                            




                            try:
                                indiceDeuda = contenido.index('Su Deuda')
                                deuda = contenido[indiceDeuda : indiceDeuda + 8]
                                print(deuda)

                                if deuda == 'Su Deuda':
                                    cuentaDeuda = "Tiene Deuda"
                                    folio_CON_DEUDA ="\n"+ folio + ";" +  cliente + ";" + persona + ";" + adm + ";" + ";" + vigente + ";" + empresa + ";" + id_casa
                                    with open(rute + "IMPUESTOS/GAS/" + "DEUDA - " + str(now.month).zfill(2)+ "_" + str(numero_bot)  + ".txt", "a") as file:
                                        file.write(folio_CON_DEUDA)

                                else:
                                    cuentaDeuda = "."
                            except:
                                cuentaDeuda = "."
                            
                            
            
                            create_pdf(logo, folio.zfill(6), cliente.zfill(11), str(monto).zfill(10), fechaFactura, indiceDesde, indiceHasta, adm, empresa)
                            carpeta_actual = os.getcwd()
                            watermark_pdf_filename = "watermarck.pdf"
                            time.sleep(3)

                            with open(watermark_pdf_filename, "rb") as watermarkfile:
                                watermarkpdf = PyPDF2.PdfReader(watermarkfile)
                                watermark_page = watermarkpdf.pages[0]
                                p.merge_page(watermark_page)

                                #CIERRA EL PDF PARA EL FINAL DEL ARMADO
                                output.add_page(p)
                                pdfwriter = PyPDF2.PdfWriter()
                                pdfwriter.add_page(p)

                                if adm == 'I':
                                    try:
                                        folder_inq = mkdir(rute + 'IMPUESTOS/GAS/' + "GAS Inquilino DESCARGADO " + date)
                                    except:
                                        #print("ERROR ARMADO CARPETA INQUILINO")
                                        pass
                                    fld_i = rute + 'IMPUESTOS/GAS/' + "GAS Inquilino DESCARGADO " + date+ "/"
                                    outputfile = fld_i + emp + folio + '_' + cliente + '_' + persona + '_' + adm + '.pdf'

                                elif adm == 'P':
                                    try:
                                        folder_prop = mkdir(rute + 'IMPUESTOS/GAS/' + "GAS Propietario DESCARGADO " + date)
                                    except:
                                        #print("ERROR ARMADO CARPETA PROPIETARIO")
                                        pass
                                    fld_p = rute + 'IMPUESTOS/GAS/' + "GAS Propietario DESCARGADO " + date+ "/"
                                    outputfile = fld_p + emp + folio + '_' + cliente + '_' + persona + '_' + adm  + '.pdf'

                                elif adm == 'L':
                                    try:
                                        folder_inm = mkdir(rute + 'IMPUESTOS/GAS/' + "GAS Inmobiliaria DESCARGADO " + date)
                                    except:
                                        #print("ERROR ARMADO CARPETA INMOBILIARIA")
                                        pass
                                    fld_l = rute + 'IMPUESTOS/GAS/' + "GAS Inmobiliaria DESCARGADO " + date+ "/"
                                    outputfile = fld_l + emp + folio + '_' + cliente + '_' + persona + '_' + adm + '.pdf'
                                
                                elif adm == 'S':
                                    try:
                                        folder_s = mkdir(rute + 'IMPUESTOS/GAS/' + "GAS SALAS DESCARGADO " + date)
                                    except:
                                        #print("ERROR ARMADO CARPETA INMOBILIARIA")
                                        pass
                                    fld_s = rute + 'IMPUESTOS/GAS/' + "GAS SALAS DESCARGADO " + date+ "/"
                                    outputfile = fld_s + emp + folio + '_' + cliente + '_' + persona + '_' + adm + '.pdf'

                    
                                with open(outputfile, "wb") as outputfilecontent:
                                    pdfwriter.write(outputfilecontent)
                                    outputfilecontent.close()
                                if liquidacion == "Comercial ":
                                    liq = liquidacion
                                    descripcion = "GASP " + desdeHasta
                                else:
                                    liq ="L" + liquidacion [liquidacion.index("de") -2 :  liquidacion.index("de")-1] + "/" + liquidacion [liquidacion.index("de") +3 :  liquidacion.index("de") + 4] 
                                    des = indiceDesde [:6] + indiceDesde [8:] 
                                    hast = indiceHasta [:6] + indiceHasta [8:] 
                                    descripcion = "GASP " + des + " a " + hast + " " + liq
                                    largo = len(descripcion)
                                if adm == "P":
                                    valores_propietarios ="\n"+ folio + ";" +  cliente + ";" + persona + ";" + adm + ";" + vigente + ";" + empresa + ";" + id_casa + ";" + liquidacion +";"+ str(monto/100) + ";" + fechaFactura  + ";" + diasLiq + ";" + desdeHasta + ";" + cuentaDeuda + ";" + descripcion
                                    print(valores_propietarios)
                                    with open(rute + "IMPUESTOS/GAS/valores propietarios " + anio + "-" + mes + "_" + str(numero_bot) + ".txt", "a") as file:  
                                        file.write(valores_propietarios)
                                else:
                                    pass

                                with open(rute + "IMPUESTOS/GAS/IMPORTES - Lectura " + date + "_" + str(numero_bot) + ".txt", "a") as file:  
                                    valores_imp ="\n"+ folio + ";" +  cliente + ";" + persona + ";" + adm + ";" + vigente + ";" + empresa + ";" + id_casa + ";" + liquidacion +";"+ str(monto/100) + ";" + fechaFactura  + ";" + diasLiq + ";" + desdeHasta + ";" + cuentaDeuda + ";" + descripcion
                                    file.write(valores_imp)
                        else:
                            vencidasf ="\n"+ folio + " " +  cliente + " " + persona + " " + adm + " " + vigente + " " + empresa + " " + id_casa + " " + fechavencidas
                            with open(rute + "IMPUESTOS/GAS/" + "Vencidas " + date + "_" + str(numero_bot) + ".txt", "a") as file:
                                file.write(vencidasf)
                                print("FOLIO "+folio+" NO ENCONTRADO")  
                    else:
                        vencidasf ="\n"+ folio + " " +  cliente + " " + persona + " " + adm + " " + vigente + " " + empresa + " " + id_casa + " " + fechavencidas
                        with open(rute + "IMPUESTOS/GAS/" + "Vencidas " + date + "_" + str(numero_bot) + ".txt", "a") as file:
                            file.write(vencidasf)
                            print("FOLIO "+folio+" NO ENCONTRADO")  

        #SI EL PDF INICIAL NO ES ENCONTRADO ARMA UN TXT CON EL LISTADO DE LOS PDF NO ENCONTRADOS CON LA FECHA DE HOY AL FINAL
        except:
            try:
                inputfile = rute_gas + "GAS - " + date + " - PLAN DE PAGOS" + "/" +folio + "_" + cliente + "_" + persona + ".pdf"
                with open (inputfile, "rb") as inputfile1:
                    pdf = PyPDF2.PdfReader(inputfile1)
                    output = PdfWriter()
                    canpage = len(pdf.pages)
                    for numero in range(0, 1):
                        p = pdf.pages[numero]
                        contenido = p.extract_text() 
                        #print(contenido)
                        try:
                                indiceLiq = contenido.index('Bimestre')
                                liquidacion = contenido[indiceLiq -19 : indiceLiq + 16]
                                print(liquidacion)
                        except:
                            liquidacion = "PLAN_DE_PAGOS"
                            print(liquidacion)

 
                        create_pdf(logo, folio.zfill(6), cliente.zfill(11), str(0).zfill(10), "00000000","-","-", adm, empresa)
                        carpeta_actual = os.getcwd()
                        watermark_pdf_filename = "watermarck.pdf"
                        time.sleep(3)

                        with open(watermark_pdf_filename, "rb") as watermarkfile:
                            watermarkpdf = PyPDF2.PdfReader(watermarkfile)
                            watermark_page = watermarkpdf.pages[0]
                            p.merge_page(watermark_page)

                            #CIERRA EL PDF PARA EL FINAL DEL ARMADO
                            output.add_page(p)
                            pdfwriter = PyPDF2.PdfWriter()
                            pdfwriter.add_page(p)

                            
                            try:
                                folder_inm = mkdir(rute + 'IMPUESTOS/GAS/' + "GAS plan de pagos DESCARGADO " + date)
                            except:

                                pass
                            fld_l = rute + 'IMPUESTOS/GAS/' + "GAS plan de pagos DESCARGADO " + date+ "/"
                            outputfile = fld_l + emp + folio + '_' + cliente + '_' + persona + '_' + adm + '.pdf'
                        

                            with open(outputfile, "wb") as outputfilecontent:
                                pdfwriter.write(outputfilecontent)
                                outputfilecontent.close()

                            folio_no_encontrado ="\n"+ folio + " " +  cliente + " " + persona + " " + adm + " " + vigente + " " + empresa + " " + id_casa + " " + liquidacion
                            with open(rute + "IMPUESTOS/GAS/" + "NO ENCONTRADOS - Estamapado " + date +   "_" + str(numero_bot) +".txt", "a") as file:
                                file.write(folio_no_encontrado)
                                print("FOLIO "+folio+" NO ENCONTRADO") 
            except:
                folio_no_encontrado ="\n"+ folio + " " +  cliente + " " + persona + " " + adm + " " + vigente + " " + empresa + " " + id_casa
                with open(rute + "IMPUESTOS/GAS/" + "NO ENCONTRADOS - Estamapado " + date +   "_" + str(numero_bot) + ".txt", "a") as file:
                    file.write(folio_no_encontrado)
                    print("FOLIO "+folio+" NO ENCONTRADO")  

        #SUMA DEL CONTADOR PARA VER LA CANTIDAD DE REGISTROS PROCESADOS  
        contador += 1
        print (str(contador) + "/" + str(len((listado))) + " " + str(folio))
        print(" - - - - - - - - - - - - - - - - - - - - - - ")

        #IGUALO LA CANTIDAD DE REGISTROS PASADOS CON LA CANTIDAD DE REGISTROS TOTALES PARA FINALIZAR EL PROCESO, SOLO IMPRIMO RESULTADO
        if ((contador)-len(listado) == 0):
            no_encontrados = "NO ENCONTRADOS " + date + "_" + str(numero_bot) + ".txt"
            lista_no =[]
            try:
                with open(rute + "GAS/" + no_encontrados, 'r', encoding = 'utf-8') as ll:
                    lin = [lina.split() for lina in ll]
                for lina in lin:
                    lista_no.append(lina)
                print("CANTIDAD DE PARTIDAS NO ENCONTRADAS = " + str(len(lista_no)-1))
            except:
                pass
            print("PROCESO TERMINADO")
        pass
numero_bot = "bot_03" 
estampado(numero_bot)  
import time
import PyPDF2
from PyPDF2 import PdfWriter
from datetime import datetime
from os import mkdir
from CREADOR import create_pdf
import os

#rute = 'C:/PROGRAMAS/'
rute = '//10.10.10.171/Compartida/'
rute_txt = rute + "IMPUESTOS/API/TXT/"
rute_api = rute + "IMPUESTOS/API/"
logo = rute + "IMPUESTOS/API/AUXILIARES/logo.jpg"

now = datetime.now()
fecha_txt = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
#print(fecha_txt)    
#VARIABLE DE DOCUMENTO TXT PARA INTRODUCIR LISTADO
filename =  rute_txt + "api.txt"



#BUSQUEDA DEL ARCHIVO
listado = []
def estampado ():
    contador = 0

    with open(filename, 'r') as f:
        line = [linea.split() for linea in f]
    for linea in line:
        listado.append(linea)
    #SE DECLARAN LAS VARIABLES QUE ESTAN DENTRO DE LA LISTA QUE SE OBTUVO DEL TXT     
    for servicio in listado:
        folio = servicio[0]
        partida = servicio[1]
        adm = servicio[2]
        id_casa = servicio[3]
        #SE DETERMINAN LAS VARIABLES PARA LA INTRODUCCION DEL CODIGO DE BARRAS
        inputfile = rute_api + "DESCARGA/" + partida + ".pdf"
        #print(inputfile)

        #ABRE LOS PDF Y ESTAMPA EL CODIGO DE BARRA SEGUN PAGINAS DEL ARCHIVO DE CODIGO DE BARRA
        try:
            with open (inputfile, "rb") as inputfile1:
                pdf = PyPDF2.PdfReader(inputfile1)
                output = PdfWriter()
                canpage = len(pdf.pages)
                for numero in range(0, canpage):
                    p = pdf.pages[numero-1]
                    Text1 = p.extract_text()
                    try:
                        cod1 = Text1.index('01102 ')
                    except:
                        cod1 = Text1.index('01103 ')
                    cod = Text1[cod1:cod1+59]
                    #print(cod)
                    partidaCodigo = cod [9:30].replace(" ","")
                    partida
                    if partida == partidaCodigo:   
                        dia = cod [44:46]
                        mes = cod [42:44]
                        año = cod [39:41]
                        fecha = dia+"/"+mes+"/"+año
                        #print(fecha)
                        monto = (f"{cod [46:47]}{cod [48:53]}{cod [54:58]}")
                        #print (monto)
                        total = int(monto)/100
                        #print(total)

                        create_pdf(logo, folio, partida, monto, fecha, adm)
                        carpeta_actual = os.getcwd()
                        watermark_pdf_filename = "watermarck.pdf"
                        time.sleep(3)

                        with open(watermark_pdf_filename, "rb") as watermarkfile:
                            watermarkpdf = PyPDF2.PdfReader(watermarkfile)
                            watermark_page = watermarkpdf.pages[0]
                            p.merge_page(watermark_page)

                            with open(rute_api + "IMPORTES " + fecha_txt +  ".txt", "a") as file:
                                valores_imp ="\n"+ folio + " " +  partida + " " + adm + " " + mes +" "+ str(total) + " " + id_casa
                                file.write(valores_imp)


                            #CIERRA EL PDF PARA EL FINAL DEL ARMADO
                            output.add_page(p)
                            pdfwriter = PyPDF2.PdfWriter()
                            pdfwriter.add_page(p)
                            

                            if adm == "I":
                                try:
                                    mkdir(rute + "IMPUESTOS/API/" + año + " - " + mes + " - Inquilino") 
                                except:
                                    pass
                                fld_i = rute + "IMPUESTOS/API/" + año + " - " + mes + " - " + "Inquilino/"
                                outputfile = fld_i + folio + "_" + partida + "_" + adm + "_" + "_Periodo_" + mes + "_" + dia + "-" + mes + "-" + año + ".pdf"
                            elif adm == "L":
                                try:
                                    mkdir(rute + "IMPUESTOS/API/" + año + " - " + mes + " - Inmbiliaria")
                                except:
                                    pass
                                fld = rute + "IMPUESTOS/API/" + año + " - " + mes + " - " + "Inmbiliaria/"
                                try:
                                    mkdir(fld + dia) 
                                except:
                                    pass
                                fld_l = fld + dia + "/"
                                outputfile = fld_l + folio + "_" + partida + "_" + adm + "_" + "_Periodo_" + mes + "_" + dia + "-" + mes + "-" + año + ".pdf"
                            elif adm == "P":
                                try:
                                    mkdir(rute + "IMPUESTOS/API/" + año + " - " + mes + " - Propietario")
                                except:
                                    pass
                                fld_p = rute + "IMPUESTOS/API/" + año + " - " + mes + " - " + "Propietario/"
                                outputfile = fld_p + folio + "_" + partida + "_" + adm + "_" + "_Periodo_" + mes + "_" + dia + "-" + mes + "-" + año + ".pdf"
                            elif adm == "S":
                                try:
                                    mkdir(rute + "IMPUESTOS/API/" + año + " - " + mes + " - Salas")
                                except:
                                    ""
                                fld_s = rute + "IMPUESTOS/API/" + año + " - " + mes + " - " + "Salas/"
                                #print(adm)
                                #print(folio)
                                outputfile = fld_s + folio + "_" + partida + "_" + adm + "_" + "_Periodo_" + mes + "_" + dia + "-" + mes + "-" + año + ".pdf"
                            with open(outputfile, "wb") as outputfilecontent:
                                pdfwriter.write(outputfilecontent)
                                outputfilecontent.close()
                    else:
                        errorPartida ="\n"+ folio + "_" +  partida + "_" + adm + "_" + " " + id_casa + "_Partida en boleta_"+ partidaCodigo
                        with open(rute + "IMPUESTOS/API/" + "Error Partida " + fecha_txt + ".txt", "a") as file:
                            file.write(errorPartida)
                            print("FOLIO "+folio+" Con Error")         
        #SI EL PDF INICIAL NO ES ENCONTRADO ARMA UN TXT CON EL LISTADO DE LOS PDF NO ENCONTRADOS CON LA FECHA DE HOY AL FINAL
        except:
            folio_no_encontrado ="\n"+ folio + " " +  partida + " " + adm + " " + " " + id_casa
            with open(rute + "IMPUESTOS/API/" + "NO ENCONTRADOS " + fecha_txt + ".txt", "a") as file:
                file.write(folio_no_encontrado)
                print("FOLIO "+folio+" NO ENCONTRADO")  
        #SUMA DEL CONTADOR PARA VER LA CANTIDAD DE REGISTROS PROCESADOS  
        contador += 1
        print (str(contador) + "/" + str(len((listado))) + " " + str(folio))
        #IGUALO LA CANTIDAD DE REGISTROS PASADOS CON LA CANTIDAD DE REGISTROS TOTALES PARA FINALIZAR EL PROCESO, SOLO IMPRIMO RESULTADO
        if ((contador)-len(listado) == 0):
            no_encontrados = "NO ENCONTRADOS " + fecha_txt + ".txt"
            lista_no =[]
            try:
                with open(rute + "API/" + no_encontrados, 'r', encoding = 'utf-8') as ll:
                    lin = [lina.split() for lina in ll]
                for lina in lin:
                    lista_no.append(lina)
                print("CANTIDAD DE PARTIDAS NO ENCONTRADAS = " + str(len(lista_no)-1))
            except:
                pass
            print("PROCESO TERMINADO")
        pass

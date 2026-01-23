import time
import PyPDF2
from PyPDF2 import PdfWriter
from datetime import datetime
from os import mkdir
from CREADOR import create_pdf
import os
from conexion import conectar

#rute = 'C:/PROGRAMAS/'
rute = '//10.10.10.171/Compartida/'
rute_txt = rute + "IMPUESTOS/TGI/TXT/"
rute_tgi = rute + "IMPUESTOS/TGI/"
logo = rute + "IMPUESTOS/TGI/AUXILIARES/logo.jpg"

now = datetime.now()
fecha_txt = str(now.day).zfill(2) + "-" + str(now.month).zfill(2) + "-" + str(now.year)
#print(fecha_txt)    
#VARIABLE DE DOCUMENTO TXT PARA INTRODUCIR LISTADO



#BUSQUEDA DEL ARCHIVO
listado = []
def estampado (numero_bot):
    filename =  rute_txt + "lista_tgi_"+ numero_bot +".txt"

    contador = 0
    resultados = conectar()
    with open(filename, 'r') as f:
        line = [linea.split() for linea in f]
    for linea in line:
        listado.append(linea)
    #SE DECLARAN LAS VARIABLES QUE ESTAN DENTRO DE LA LISTA QUE SE OBTUVO DEL TXT     
    for servicio in listado:
        folio = servicio[0]
        partida = servicio[1]
        clave = servicio[2]
        adm = servicio[3]
        id_casa = servicio[4]
        #SE DETERMINAN LAS VARIABLES PARA LA INTRODUCCION DEL CODIGO DE BARRAS
        inputfile = rute_tgi + "DESCARGA/" + folio + "_" + partida + ".pdf"
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
                    #print(Text1)
                    try:
                        codi = Text1.index('000394')
                        cod = Text1[codi: codi + 47]
                        print(cod)
                        verificador_deuda = cod [9:10]
                        #print(verificador_deuda)
                        dia = cod [29:31]
                        mes = cod [31:33]
                        año = cod [33:37]
                        fecha = dia+"-"+mes+"-"+año
                        #print(fecha)
                        monto = cod [38:47]
                    except:
                        codi = Text1.index('600394')
                        cod = Text1[codi: codi + 44]
                        print(cod)
                        verif_deuda = cod [8:9]
                        if verif_deuda == '1':
                            verificador_deuda = 0
                        else: 
                            verificador_deuda = 1

                        #print(verificador_deuda)
                        dia = cod [27:29]
                        mes = cod [25:27]
                        año = cod [21:25]
                        fecha = dia+"-"+mes+"-"+año
                        #print(fecha)
                        monto = cod [29:42]
                    
                    #print (monto)
                    total = int(monto)/100
                    #print(total)
                    
                    folios = []
                    for result in resultados:
                        #print(result)
                        try:
                            if int(partida) == int(result[1]):
                                folios.append(result[0])
                        except:
                            pass


                    create_pdf(logo, folios, partida, monto, fecha, adm)
                    carpeta_actual = os.getcwd()
                    watermark_pdf_filename = "watermarck.pdf"
                    time.sleep(3)

                    with open(watermark_pdf_filename, "rb") as watermarkfile:
                        watermarkpdf = PyPDF2.PdfReader(watermarkfile)
                        watermark_page = watermarkpdf.pages[0]
                        p.merge_page(watermark_page)

                        with open(rute_tgi + "IMPORTES " + fecha_txt + "_" + numero_bot + ".txt", "a") as file:
                            if int(verificador_deuda) == int(0):
                                valores_imp ="\n"+ folio + " " +  partida + " " + clave + " " + adm + " " + mes +" "+ str(total) + " " + id_casa
                                file.write(valores_imp)
                            else:
                                valores_imp ="\n"+ folio + " " +  partida + " " + clave + " " + adm + " " + "deuda" +" "+ str(total) + " " +id_casa
                                file.write(valores_imp)


                        #CIERRA EL PDF PARA EL FINAL DEL ARMADO
                        output.add_page(p)
                        pdfwriter = PyPDF2.PdfWriter()
                        pdfwriter.add_page(p)
                        
                        if int(verificador_deuda) == int(0):
                            if adm == "I":
                                try:
                                    mkdir(rute + "IMPUESTOS/TGI/" + año + " - " + mes + " - Inquilino") 
                                except:
                                    pass
                                fld_i = rute + "IMPUESTOS/TGI/" + año + " - " + mes + " - " + "Inquilino/"
                                outputfile = fld_i + folio + "_" + partida + "_" + adm + "_" + "_Periodo_" + mes + "_" + dia + "-" + mes + "-" + año + ".pdf"
                            elif adm == "L":
                                try:
                                    mkdir(rute + "IMPUESTOS/TGI/" + año + " - " + mes + " - Inmbiliaria")
                                except:
                                    pass
                                fld_l = rute + "IMPUESTOS/TGI/" + año + " - " + mes + " - " + "Inmbiliaria/"
                                outputfile = fld_l + folio + "_" + partida + "_" + adm + "_" + "_Periodo_" + mes + "_" + dia + "-" + mes + "-" + año + ".pdf"
                            elif adm == "P":
                                try:
                                    mkdir(rute + "IMPUESTOS/TGI/" + año + " - " + mes + " - Propietario")
                                except:
                                    pass
                                fld_p = rute + "IMPUESTOS/TGI/" + año + " - " + mes + " - " + "Propietario/"
                                outputfile = fld_p + folio + "_" + partida + "_" + adm + "_" + "_Periodo_" + mes + "_" + dia + "-" + mes + "-" + año + ".pdf"
                            elif adm == "S":
                                try:
                                    mkdir(rute + "IMPUESTOS/TGI/" + año + " - " + mes + " - Salas")
                                except:
                                    ""
                                fld_s = rute + "IMPUESTOS/TGI/" + año + " - " + mes + " - " + "Salas/"
                                #print(adm)
                                #print(folio)
                                outputfile = fld_s + folio + "_" + partida + "_" + adm + "_" + "_Periodo_" + mes + "_" + dia + "-" + mes + "-" + año + ".pdf"
                        else:
                            try:
                                    fld_deuda = mkdir(rute + "IMPUESTOS/TGI/" + año + " - " + mes + " - DEUDA")
                            except:
                                    pass
                            fld_deuda = rute + "IMPUESTOS/TGI/" + año + " - " + mes + " - DEUDA/"
                            outputfile = fld_deuda + folio + "_" + partida + "_" + adm + "_" + "DEUDA" + ".pdf"

                        with open(outputfile, "wb") as outputfilecontent:
                            pdfwriter.write(outputfilecontent)
                            outputfilecontent.close()

        #SI EL PDF INICIAL NO ES ENCONTRADO ARMA UN TXT CON EL LISTADO DE LOS PDF NO ENCONTRADOS CON LA FECHA DE HOY AL FINAL
        except:
            folio_no_encontrado ="\n"+ folio + " " +  partida + " " + clave + " " + adm + " " + " " + id_casa
            with open(rute + "IMPUESTOS/TGI/" + "NO ENCONTRADOS " + fecha_txt + "_" + numero_bot + ".txt", "a") as file:
                file.write(folio_no_encontrado)
                print("FOLIO "+folio+" NO ENCONTRADO")  

        #SUMA DEL CONTADOR PARA VER LA CANTIDAD DE REGISTROS PROCESADOS  
        contador += 1
        print (str(contador) + "/" + str(len((listado))) + " " + str(folio))

        #IGUALO LA CANTIDAD DE REGISTROS PASADOS CON LA CANTIDAD DE REGISTROS TOTALES PARA FINALIZAR EL PROCESO, SOLO IMPRIMO RESULTADO
        if ((contador)-len(listado) == 0):
            no_encontrados = "NO ENCONTRADOS " + fecha_txt + "_" + numero_bot + ".txt"
            lista_no =[]
            try:
                with open(rute + "TGI/" + no_encontrados, 'r', encoding = 'utf-8') as ll:
                    lin = [lina.split() for lina in ll]
                for lina in lin:
                    lista_no.append(lina)
                print("CANTIDAD DE PARTIDAS NO ENCONTRADAS = " + str(len(lista_no)-1))
            except:
                pass
            print("PROCESO TERMINADO")
        pass

""" numero_bot = "Bot_01"
estampado (numero_bot) """
import PyPDF2
from PyPDF2 import PdfWriter
from datetime import datetime
from os import mkdir
from CREADOR import create_pdf
import os

#rute = 'C:/PROGRAMAS/'
rute = '//10.10.10.171/Compartida/'
rute_txt = rute + "IMPUESTOS/AGUA/TXT/"
rute_agua = rute + "IMPUESTOS/AGUA/"
logo = rute + "IMPUESTOS/AGUA/AUXILIARES/logo.jpg"

now = datetime.now()
fecha_txt = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
#print(fecha_txt)    
#VARIABLE DE DOCUMENTO TXT PARA INTRODUCIR LISTADO
from conexion import conectar

#PONEMOS UN CONTADOR EN 0 PARA IR SUMANDO LOS REGISTROS PROCESADOS EN COMPARATIVA, AL FINAL FIGURA LA SUMA DE CONTADOR

def medidors (dato_medido, rute_agua, fecha, folio, punto, total, adm,Text1, volumenFacturado):
    if dato_medido == 'NO MEDIDO':
        con_medidor = ''
        c_medidor = ''
        with open(rute_agua + "IMPORTES_SIN_MEDIDOR " + fecha + ".txt", "a") as file:
                valoresSinMedidor ="\n"+ folio + " " + punto + " " +  str(0) + " " + str(total).replace('.',',') + " " + adm  + '.'
                file.write(valoresSinMedidor)
    elif dato_medido == 'MEDIDO - ':
        
        cantMedidor = Text1.index("Ajuste        Consumo R/E  Medidor ")
        inicio_medidor1 =cantMedidor + 104 + 22
        cantMedidor_1 = Text1[inicio_medidor1 : inicio_medidor1 + 12].replace(' ','')
        #print(cantMedidor_1)
        consumo_1 = float(Text1[inicio_medidor1 + 75 : inicio_medidor1 + 82]) + 0
        #print(int(consumo_1))
        
        try:
            inicio_medidor2 =cantMedidor + 192 + 22
            cantMedidor_2 = Text1[inicio_medidor2 : inicio_medidor2 + 12].replace(' ','')
            #print(cantMedidor_2)
            consumo_2 = float(Text1[inicio_medidor2 + 75 : inicio_medidor2 + 82]) + 0
            #print(int(consumo_2))
        except:
            cantMedidor_2 = "-"
            consumo_2 = 0
            pass
        try:
            inicio_medidor3 =cantMedidor + 290 + 22
            cantMedidor_3 = Text1[inicio_medidor3 : inicio_medidor3 + 12].replace(' ','')
            #print(cantMedidor_3)
            consumo_3 = float(Text1[inicio_medidor3 + 75 : inicio_medidor3 + 82]) + 0
            #print(int(consumo_3))
        except:
            cantMedidor_3 = "-"
            consumo_3 = 0
            pass
        try:
            inicio_medidor4 =cantMedidor + 378 + 22
            cantMedidor_4 = Text1[inicio_medidor4 : inicio_medidor4 + 12].replace(' ','')
            #print(cantMedidor_4)
            consumo_4 = float(Text1[inicio_medidor4 + 75 : inicio_medidor4 + 82]) + 0
            #print(int(consumo_4))
        except:
            cantMedidor_4 = "-"
            consumo_4 = 0
            pass
        try:
            inicio_medidor5 =cantMedidor + 476 + 22
            cantMedidor_5 = Text1[inicio_medidor5 : inicio_medidor5 + 12].replace(' ','')
            #print(cantMedidor_5)
            #print(Text1[inicio_medidor5 + 75 : inicio_medidor5 + 82])
            consumo_5 = float(Text1[inicio_medidor5 + 75 : inicio_medidor5 + 82]) + 0
            #print(int(consumo_5))
        except:
            cantMedidor_5 = "-"
            consumo_5 = 0
            pass
        try:
            inicio_medidor6 =cantMedidor + 564 + 22
            cantMedidor_6 = Text1[inicio_medidor6 : inicio_medidor6 + 12].replace(' ','')
            #print(cantMedidor_6)
            consumo_6 = float(Text1[inicio_medidor6 + 75 : inicio_medidor6 + 82]) + 0
            #print(int(consumo_6))
        except:
            cantMedidor_6 = "-"
            consumo_6 = 0
            pass

        suma_medidores = float(consumo_1+consumo_2+consumo_3+consumo_4+consumo_5+consumo_6)
        #print( str(suma_medidores) == str(volumenFacturado))
        volFact = float(volumenFacturado)
        if volFact == 0.00:
            volFact = 1
        porUnidad = total / volFact
        medidor1 = consumo_1 * porUnidad
        medidor2 = consumo_2 * porUnidad
        medidor3 = consumo_3 * porUnidad
        medidor4 = consumo_4 * porUnidad
        medidor5 = consumo_5 * porUnidad
        medidor6 = consumo_6 * porUnidad


        total_medidores = round(medidor1,2)+round(medidor2,2)+round(medidor3,2)+round(medidor4,2)+round(medidor5,2)+round(medidor6,2)
        dif = total - total_medidores
        medidor1 = medidor1+dif


        con_medidor = ('CON_MEDIDOR_' + str(volumenFacturado) + "m3" + ' ' + 
        "Medidor-" + cantMedidor_1 + " " + str(consumo_1) + "m3" + " " + str(round(medidor1,2)) + " / " + 
        "Medidor-" + cantMedidor_3 + " " + str(consumo_3) + "m3" + " " + str(round(medidor3,2)) + " / " + 
        "Medidor-" + cantMedidor_5 + " " + str(consumo_5) + "m3" + " " + str(round(medidor5,2)) + " / " + 
        "Medidor-" + cantMedidor_2 + " " + str(consumo_2) + "m3" + " " + str(round(medidor2,2)) + " / " + 
        "Medidor-" + cantMedidor_4 + " " + str(consumo_4) + "m3" + " " + str(round(medidor4,2)) + " / " + 
        "Medidor-" + cantMedidor_6 + " " + str(consumo_6) + "m3" + " " + str(round(medidor6,2)))
        c_medidor = 'CON_MEDIDOR'

        if  consumo_1 != 0:
            with open(rute_agua + "IMPORTES_MEDIDOS " + fecha + "_" + str(numero_bot) + ".txt", "a") as file:
                valores_1 ="\n"+ folio + " " + punto + " " +  cantMedidor_1 + " " + str(round(medidor1,2)).replace('.',',') + " " + adm
                file.write(valores_1)
        if  consumo_3 != 0:
            with open(rute_agua + "IMPORTES_MEDIDOS " + fecha + "_" + str(numero_bot) + ".txt", "a") as file:
                valores_3 ="\n"+ folio + " " + punto + " " +  cantMedidor_3 + " " + str(round(medidor3,2)).replace('.',',') + " " + adm
                file.write(valores_3)
        if  consumo_5 != 0:
            with open(rute_agua + "IMPORTES_MEDIDOS " + fecha + "_" + str(numero_bot) + ".txt", "a") as file:
                valores_5 ="\n"+ folio + " " + punto + " " +  cantMedidor_5 + " " + str(round(medidor5,2)).replace('.',',') + " " + adm
                file.write(valores_5)
        if  consumo_2 != 0:
            with open(rute_agua + "IMPORTES_MEDIDOS " + fecha + "_" + str(numero_bot) + ".txt", "a") as file:
                valores_2 ="\n"+ folio + " " + punto + " " +  cantMedidor_2 + " " + str(round(medidor2,2)).replace('.',',') + " " + adm
                file.write(valores_2)
        if  consumo_4 != 0:
            with open(rute_agua + "IMPORTES_MEDIDOS " + fecha + "_" + str(numero_bot) + ".txt", "a") as file:
                valores_4 ="\n"+ folio + " " + punto + " " +  cantMedidor_4 + " " + str(round(medidor4,2)).replace('.',',') + " " + adm
                file.write(valores_4)
        if  consumo_6 != 0:
            with open(rute_agua + "IMPORTES_MEDIDOS " + fecha + "_" + str(numero_bot) + ".txt", "a") as file:
                valores_6 ="\n"+ folio + " " + punto + " " +  cantMedidor_6 + " " + str(round(medidor6,2)).replace('.',',') + " " + adm
                file.write(valores_6)
    else:
        con_medidor = 'ERROR_LECTURA_DE_MEDIDOR'
        c_medidor = 'ERROR_LECTURA_DE_MEDIDOR'
    return(c_medidor, con_medidor)


#BUSQUEDA DEL ARCHIVO
listado = []
def estampado (numero_bot):
    resultados = conectar()
    filename =  rute_txt + "agua_" + str(numero_bot) + ".txt"
    contador = 0

    with open(rute_agua + "IMPORTES " + fecha_txt + "_" + str(numero_bot) + ".txt", "a") as file:
        valores_imp = "Folio" + " " +  "Partida"  + " " + "Punto" + " " + "Adm" + " "  + "Mes" + " Deuda " + "Total_factura" + " " + "Cuota"  + " " + "Total_cuota" + " " + "id_casa" + " " + "medidores"
        file.write(valores_imp)                      
    
    with open(filename, 'r') as f:
        line = [linea.split() for linea in f]
    for linea in line:
        listado.append(linea)
    #SE DECLARAN LAS VARIABLES QUE ESTAN DENTRO DE LA LISTA QUE SE OBTUVO DEL TXT     
    for servicio in listado:
        folio = servicio[0]
        partida = servicio[1]
        punto = servicio[2]
        adm = servicio[3]
        id_casa = servicio[4]
        #SE DETERMINAN LAS VARIABLES PARA LA INTRODUCCION DEL CODIGO DE BARRAS
        inputfile = rute_agua + "DESCARGA/" + punto + ".pdf"
        #print(inputfile)

        #ABRE LOS PDF Y ESTAMPA EL CODIGO DE BARRA SEGUN PAGINAS DEL ARCHIVO DE CODIGO DE BARRA
        try:
            with open (inputfile, "rb") as inputfile1:
                pdf = PyPDF2.PdfReader(inputfile1)
                output = PdfWriter()
                canpage = len(pdf.pages)
                for numero in range(0, canpage):
                    total_factura = 0
                    p = pdf.pages[numero-1]
                    Text1 = p.extract_text() 
                    #print(Text1)
                    codi = Text1.index('53-0')
                    cod = Text1[codi: codi + 60]
                    dia = cod [19:21]
                    mes = cod [21:23]
                    año = cod [23:25]
                    fecha = dia+"-"+mes+"-"+año
                    monto = cod [26:36]
                    total = int(monto)
                    mont = str(total).zfill(10)
                    if int(mes) == 12:
                        #print ("es Enero")
                        codi2 = Text1.index("01"+str(int(año)+1)+"-")
                        cod2 = Text1[codi2 -21: codi2 + 39]
                        dia2 = cod2 [19:21]
                        mes2 = cod2 [21:23]
                        año2 = cod2 [23:25]
                        fecha2 = dia2+"-"+mes2+"-"+año2
                        monto2 = cod2 [26:36]
                        total2 = int(monto)
                        mont2 = str(monto2).zfill(10)
                        #print("toma el valor mas")
                        t_factura = total + total2
                        total_factura = str(t_factura).zfill(10)
                    else:
                        try:
                            codi2 = Text1.index(dia+str(int(mes)+1).zfill(2)+año+"-")
                            cod2 = Text1[codi2 -19: codi2 + 34]
                            dia2 = cod2 [19:21]
                            mes2 = cod2 [21:23]
                            año2 = cod2 [23:25]
                            fecha2 = dia2+"-"+mes2+"-"+año2
                            monto2 = cod2 [26:36]
                            total2 = int(monto2)
                            mont2 = str(monto2).zfill(10)
                        except:
                            codi2 = Text1.index(dia+str(int(mes)+1).zfill(2)+año+"-")
                            cod2 = Text1[codi2 -19: codi2 + 39]
                            dia2 = cod2 [22:24]
                            mes2 = cod2 [24:26]
                            año2 = cod2 [26:28]
                            fecha2 = dia2+"-"+mes2+"-"+año2
                            monto2 = cod2 [29:39]
                            total2 = int(monto2)
                            mont2 = str(monto2).zfill(10)

                        #print("toma el valor mas")
                        t_factura = total+ total2
                        total_factura = str(t_factura).zfill(10)
                    print(folio)
                    folios = []
                    for result in resultados:
                        #print(result)
                        try:
                            if int(punto) == int(result[2]):
                                folios.append(result[0])
                        except:
                            pass
                    create_pdf(logo, folios, punto, total_factura, fecha, fecha2, adm, mont, mont2)
                    carpeta_actual = os.getcwd()
                    watermark_pdf_filename = "watermarck.pdf"

                    indiceVolI = Text1.index("VOL.FACTURADO")
                    indiceVolF = Text1.index("m3")
                    volumenFacturado = Text1[indiceVolI + 14: indiceVolF].replace(',','.') 
                    medidor = Text1.index('- TARIFA')
                    dato_medido = Text1[medidor + 9 : medidor + 18]

                    deuda = Text1.index('Importe Deuda')
                    verificador_deuda = Text1[deuda + 13: deuda + 29]
                    #print(verificador_deuda)
                    total_f = float(mont)/100
                    total_f2 = float(mont2)/100
                    total_final = float(total_factura)/100

                    medido = medidors (dato_medido, rute_agua, fecha, folio, punto, total_f, adm,Text1, volumenFacturado)
                    medido2 = medidors (dato_medido, rute_agua, fecha2, folio, punto, total_f2, adm,Text1, volumenFacturado)
                    print(medido)
                    print(medido2)

                    with open(watermark_pdf_filename, "rb") as watermarkfile:
                        watermarkpdf = PyPDF2.PdfReader(watermarkfile)
                        watermark_page = watermarkpdf.pages[0]
                        p.merge_page(watermark_page)
                        with open(rute_agua + "IMPORTES " + fecha_txt + "_" + str(numero_bot) + ".txt", "a") as file:
                            if verificador_deuda == str('            0,00'):
                                valores_imp ="\n"+ folio + " " +  partida  + " " + punto + " " + adm + " "  + mes + " - " + str(total_final) + " " + "Cuota_1"  + " " + str(total/100) + " " + id_casa + " " + medido[1]
                                file.write(valores_imp)
                                valores_imp2 ="\n"+ folio + " " +  partida + " " + punto + " " + adm + " "  + mes2 + " - " + str(total_final) + " " + "Cuota_2"  + " " + str(total2/100) + " " + id_casa + " " + medido2[1]
                                file.write(valores_imp2)
                            else:
                                valores_imp ="\n"+ folio + " " +  partida + " " + punto + " " + adm + " "  + mes + " Deuda " + str(total_final) + " " + "Cuota_1"  + " " + str(total/100) + " " + id_casa + " " + medido[1]
                                file.write(valores_imp)
                                valores_imp2 ="\n"+ folio + " " +  partida + " " + punto + " " + adm + " " + mes2 + " Deuda " + str(total_final) + " " + "Cuota_2"  + " " + str(total2/100) + " " + id_casa + " " + medido2[1]
                                file.write(valores_imp2)
                                
                                
                        #CIERRA EL PDF PARA EL FINAL DEL ARMADO
                        output.add_page(p)
                        pdfwriter = PyPDF2.PdfWriter()
                        pdfwriter.add_page(p)

                        
                    
                        if adm == "I":
                            try:
                                mkdir(rute + "IMPUESTOS/AGUA/" + año + " - " + mes + " - Inquilino") 
                            except:
                                pass
                            fld_i = rute + "IMPUESTOS/AGUA/" + año + " - " + mes + " - " + "Inquilino/"
                            outputfile = fld_i + folio + "_" + punto + "_" + adm + "_" + "_Periodo_" + mes + "_" + dia + "-" + mes + "-" + año + ".pdf"
                        elif adm == "L":
                            try:
                                mkdir(rute + "IMPUESTOS/AGUA/" + año + " - " + mes + " - Inmbiliaria")
                            except:
                                pass
                            fld_l = rute + "IMPUESTOS/AGUA/" + año + " - " + mes + " - " + "Inmbiliaria/"
                            outputfile = fld_l + folio + "_" + punto + "_" + adm + "_" + "_Periodo_" + mes + "_" + dia + "-" + mes + "-" + año + ".pdf"
                        elif adm == "P":
                            try:
                                mkdir(rute + "IMPUESTOS/AGUA/" + año + " - " + mes + " - Propietario")
                            except:
                                pass
                            fld_p = rute + "IMPUESTOS/AGUA/" + año + " - " + mes + " - " + "Propietario/"
                            outputfile = fld_p + folio + "_" + punto + "_" + adm + "_" + "_Periodo_" + mes + "_" + dia + "-" + mes + "-" + año + ".pdf"
                        elif adm == "S":
                            try:
                                mkdir(rute + "IMPUESTOS/AGUA/" + año + " - " + mes + " - Salas")
                            except:
                                pass
                            fld_s = rute + "IMPUESTOS/AGUA/" + año + " - " + mes + " - " + "Salas/"
                            outputfile = fld_s + folio + "_" + punto + "_" + adm + "_" + "_Periodo_" + mes + "_" + dia + "-" + mes + "-" + año + ".pdf"


                        with open(outputfile, "wb") as outputfilecontent:
                            pdfwriter.write(outputfilecontent)
                            outputfilecontent.close()

        #SI EL PDF INICIAL NO ES ENCONTRADO ARMA UN TXT CON EL LISTADO DE LOS PDF NO ENCONTRADOS CON LA FECHA DE HOY AL FINAL
        except:
            folio_no_encontrado ="\n"+ folio + " " +  partida + " " + punto + " " + adm + " " + " " + id_casa
            with open(rute + "IMPUESTOS/AGUA/" + "NO ENCONTRADOS " + fecha_txt + "_" + str(numero_bot) + ".txt", "a") as file:
                file.write(folio_no_encontrado)
                print("FOLIO "+folio+" NO ENCONTRADO")   

        #SUMA DEL CONTADOR PARA VER LA CANTIDAD DE REGISTROS PROCESADOS  
        contador += 1
        print (str(contador) + "/" + str(len((listado))))

        #IGUALO LA CANTIDAD DE REGISTROS PASADOS CON LA CANTIDAD DE REGISTROS TOTALES PARA FINALIZAR EL PROCESO, SOLO IMPRIMO RESULTADO
        if ((contador)-len(listado) == 0):
            no_encontrados = "NO ENCONTRADOS " + fecha_txt + "_" + str(numero_bot) + ".txt"
            lista_no =[]
            try:
                with open(rute + "AGUA/" + no_encontrados, 'r', encoding = 'utf-8') as ll:
                    lin = [lina.split() for lina in ll]
                for lina in lin:
                    lista_no.append(lina)
                print("CANTIDAD DE PARTIDAS NO ENCONTRADAS = " + str(len(lista_no)-1))
            except:
                pass
            print("PROCESO TERMINADO")
        pass
numero_bot = "Bot_01"
estampado(numero_bot)

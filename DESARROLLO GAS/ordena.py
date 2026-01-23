
from datetime import datetime
from os import mkdir
import shutil

#rute = 'C:/PROGRAMAS/'
rute = '//10.10.10.171/Compartida/'
rute_txt = rute + "IMPUESTOS/GAS/TXT/"
now = datetime.now()
fecha = str(now.year) + "-" + str(now.month).zfill(2) + "-" + str(now.day).zfill(2)

def ordenar(numero_bot):  
    print('NOT YET')
    #armado de lista con la de importes
    dia_gas = rute + 'IMPUESTOS/GAS/' + 'IMPORTE ' + fecha + "_" + str(numero_bot) + '.txt'
    #print(dia_gas)
    list_importe = []
    with open (dia_gas, 'r', encoding = 'utf-8') as dia_gass:
        gas_split = [linea.split() for linea in dia_gass]

    for linea in gas_split:
        list_importe.append(linea)

    for dia_lista_gas in gas_split:
        folio = str(dia_lista_gas[0])
        #print(folio)
        cliente = str(dia_lista_gas[1])
        persona = str(dia_lista_gas[2])
        simbolo = str(dia_lista_gas[3])
        importe_ex = str(dia_lista_gas[4])
        fecha_factura = str(dia_lista_gas[5]).zfill(10)
        #fecha_factura1 = str(dia_lista_gas[9])
        dia_f = fecha_factura[:2].zfill(2)
        mes_f = fecha_factura[3:5].zfill(2)
        anio_f = fecha_factura[6:10].zfill(4)
        fec_fact = dia_f +'-'+ mes_f +'-'+ anio_f
        print(fec_fact)
        num_factura = str(dia_lista_gas[6])
        adm = "L"

        
        ubicacion_fecha = rute + 'IMPUESTOS/GAS/GAS Inmobiliaria DESCARGADO ' + fecha + '/' + 'Facturas del ' + str(fec_fact)
        print(ubicacion_fecha)
        try:
            mkdir(ubicacion_fecha)
        except:
            pass
        
        try:     
            archivo = rute + 'IMPUESTOS/GAS/GAS Inmobiliaria DESCARGADO ' + fecha + '/' + folio + '_' + cliente + '_' + persona + '_' + adm + '.pdf'
            print(archivo)
            destino = rute + 'IMPUESTOS/GAS/GAS Inmobiliaria DESCARGADO ' + fecha + '/' + 'Facturas del ' + str(fec_fact) + '/' + folio + '_' + cliente + '_' + persona + '_' + adm + '.pdf'
            shutil.move(archivo, destino)
        except:
            pass
    print('DONE')

#ordenar()
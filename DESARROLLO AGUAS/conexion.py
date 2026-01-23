import pymysql

ip_con ="10.10.10.190"
pasw_con = "aopen"
select = """SELECT 
       p.carpeta as "FOLIO",
       pi.partida,
       pi.clave_internet,
       e.id_empresa
        FROM desarrollo.propiedades_impuestos pi
        INNER JOIN desarrollo.tipos_impuestos ti ON pi.id_tipo_impuesto = ti.id_tipo_impuesto
        INNER JOIN desarrollo.propiedades p ON p.id_casa = pi.id_casa
        INNER JOIN desarrollo.nomenclador n ON n.Id_Nomenclador = p.id_nomenclador
        LEFT JOIN desarrollo.impuestos i ON pi.id_casa = i.id_casa
        INNER JOIN desarrollo.contratos_cabecera cc ON cc.id_casa = p.id_casa
        INNER JOIN desarrollo.empresa e ON cc.id_empresa = e.id_empresa 
        WHERE  ti.id_tipo_impuesto = 2 -- COLOCAR 1 PARA TGI, 2 PARA AGUA O 3 PARA API --
        GROUP BY pi.id_propiedad_impuesto -- PARA PADRON AGRUPAR POR ESTA ID, PARA DESCARGA AGRUPAR POR partida, O clave_internet .--
        ORDER BY id_empresa , folio;"""

def conectar():
    miConection =pymysql.connect(
        host= ip_con,
        user="root",
        passwd= pasw_con,
        db= "desarrollo",
        charset='utf8',  # Usamos 'utf8' en lugar de 'utf8mb4'
        use_unicode=True
    )
    cur =miConection.cursor()
    cur.execute(select)
    resultados = cur.fetchall()  # Obtenemos los resultados con fetchall()
    miConection.close()  # Cerramos la conexión
    
    # Mostrar los resultados
    for fila in resultados:
        print(fila) 
    
    return(resultados)

# Capturamos y mostramos los resultados
""" resultados = conectar()
print(f"\nTotal de registros encontrados: {len(resultados)}") """

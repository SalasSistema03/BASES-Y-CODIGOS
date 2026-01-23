import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from PIL import Image
from barcode import Code39
from barcode.writer import ImageWriter
import os
import shutil
import qrcode

def generate_barcode(filename, folio, partida, importe, fecha, indiceDesde, indiceHasta, adm):
    # Convert code to string
    code_str = str(folio.replace("_", "") + partida + importe.replace(".", "") + fecha.replace("/", "")+ indiceDesde.replace("/", "") + indiceHasta.replace("/", "") + adm)
    # Generate barcode image
    #barcode = Code39(code_str, writer=ImageWriter(), add_checksum=False)
    #barcode_image = barcode.save(filename + ".png")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(code_str)
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color="#0055B9", back_color="white")


    # Guarda el código QR resultante con la imagen superpuesta
    img_qr.save(filename + ".png")
    

def create_pdf(logo, folio, partida, monto, fecha, indiceDesde, indiceHasta, adm, empresa):
    carpetaTemporal = "temp"
    try:
        shutil.rmtree(carpetaTemporal)
    except:
        pass
    time.sleep(5)
    os.makedirs(carpetaTemporal)
    # Create PDF with A4 size
    pdf_filename = "watermarck.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    # Define styles
    styles = getSampleStyleSheet()
    style_down = ParagraphStyle('Center', parent=styles['Normal'], alignment=2, spaceAfter=5, fontSize=9) 
    style_up = ParagraphStyle('Center', parent=styles['Normal'], alignment=2, spaceAfter=5, fontSize=18) 
    # Draw logo
    logo_width = 2.7 * cm
    logo_height = 1.5 * cm
    # Draw barcodes and list numbers

    c.drawImage(logo, cm, A4[1] - 1.8 * cm, width=logo_width, height=logo_height)
    # Generate barcode
    barcode_filename = f"temp/barcode"
    generate_barcode(barcode_filename, folio, partida, monto, fecha, indiceDesde, indiceHasta, adm)
    # Draw barcode
    barcode_width = 2.5 * cm
    barcode_height = 2.5 * cm
    with Image.open(barcode_filename + ".png") as img:
        #UBICACION CODIGO DE BARRAS PRIMERO ANCHO Y LUEGO ALTO
        c.drawInlineImage(img, A4[0] - 0.1 * cm - barcode_width, A4[1] - 3 * cm, width=barcode_width, height=barcode_height)
    # Draw list number in the center at the top with a 0.5 cm margin
    if empresa == "1":
        emp = ""
    elif empresa == "2":
        emp = "CAN "
    elif empresa == "3":
        emp = "TRIB "
    text = f"F: {emp} <b>{folio}</b> Adm: <b>{adm}</b>"
    p = Paragraph(text, style_up)
    p.wrapOn(c, A4[0] - 12 * cm, cm) # LARGO
    p.drawOn(c, cm, A4[1] - 0.5 * cm) # ALTO
    p = Paragraph(text, style_down)
    p.wrapOn(c, A4[0] - 2 * cm, cm)
    p.drawOn(c, cm, 3.2 * cm)  # Cambia la coordenada Y para mover el texto hacia la parte inferior
    # Agregar un salto de página
    c.showPage()
    c.save()
    shutil.rmtree(carpetaTemporal)


#rute = 'C:/PROGRAMAS/'
#logo = rute + "IMPUESTOS/TGI/AUXILIARES/logo.jpg"
#folio = 2
#padron = 0
#importe = 100
#fecha = ""
#adm = "P"

#create_pdf(logo, folio, importe, fecha, adm)

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

def generate_barcode(code, filename):
    # Generate barcode image
    barcode = Code39(code, writer=ImageWriter(), add_checksum=False)
    barcode_image = barcode.save(filename + ".png")
def create_pdf(lista):
    carpetaTemporal = "temp"
    try:
        shutil.rmtree(carpetaTemporal)
    except:
        pass
    os.makedirs(carpetaTemporal)
    # Create PDF with A4 size
    pdf_filename = "watermarck.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    # Define styles
    styles = getSampleStyleSheet()
    style_center = ParagraphStyle('Center', parent=styles['Normal'], alignment=2, spaceAfter=5)
    # Draw logo
    logo_width = 2 * cm
    logo_height = 1 * cm
    # Draw barcodes and list numbers
    for i, code in enumerate(lista):
        folio = code[0]
        padron = code[1]
        dato2 = code[2]
        adm = code[3]
        dato4 = code[4]
        c.drawImage(logo, cm, A4[1] - 1.5 * cm, width=logo_width, height=logo_height)
        # Generate barcode
        barcode_filename = f"temp/barcode_{i}"
        generate_barcode(padron, barcode_filename)
        # Draw barcode
        barcode_width = 4 * cm
        barcode_height = 1 * cm
        with Image.open(barcode_filename + ".png" + ".png") as img:
            c.drawInlineImage(img, A4[0] - 1.5 * cm - barcode_width, A4[1] - 1.5 * cm, width=barcode_width, height=barcode_height)
        # Draw list number in the center at the top with a 0.5 cm margin
        text = f"F: <b>{folio}</b> Adm: <b>{adm}</b>"
        p = Paragraph(text, style_center)
        p.wrapOn(c, A4[0] - 11 * cm, cm)
        p.drawOn(c, cm, A4[1] - 0.8 * cm)
        p = Paragraph(text, style_center)
        p.wrapOn(c, A4[0] - 2 * cm, cm)
        p.drawOn(c, cm, 0.5 * cm)  # Cambia la coordenada Y para mover el texto hacia la parte inferior
        # Agregar un salto de página
        c.showPage()
    c.save()
    shutil.rmtree(carpetaTemporal)
def creador(rute_txt , logo):
    lista = []
    with open(rute_txt, 'r') as file:
        # Lee las líneas del archivo y quita los espacios en blanco
        lines = [line.strip() for line in file]
    for line in lines:
        # Divide cada línea en campos usando espacios como delimitador
        fields = line.split()
        # Ahora, 'fields' es una lista que contiene los campos de la línea
        lista.append(fields)
    create_pdf(lista)

rute = 'C:/PROGRAMAS/'
rute_txt = rute + "IMPUESTOS/TGI/TXT//lista_tgi.txt"
rute_tgi = rute + "IMPUESTOS/TGI/"
logo = rute + "IMPUESTOS/TGI/AUXILIARES/logo.jpg"
creador(rute_txt, logo)

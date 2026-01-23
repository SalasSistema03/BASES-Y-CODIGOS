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

def generate_barcode(filename, folio, partida, importe, fecha, fecha2, adm, mont, mont2):
    print(mont)
    print(mont2)
    print(fecha2)
    # Convert code to string
    #code_str = str(folio.zfill(5) + partida.zfill(8) + importe + fecha.replace("-", "") + mont + fecha2.replace("-", "") + mont2 + adm)
    code_str = str(partida.zfill(8) + fecha.replace("-", "") + mont + fecha2.replace("-", "") + mont2 + adm)
    
    #print(code_str)
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

    # Abre la imagen que deseas superponer en el centro
    #img_imagen = Image.open("SALAS.png")

    # Asegúrate de que la imagen tenga un canal alfa (canal de transparencia)
    """ if img_imagen.mode != "RGBA":
        img_imagen = img_imagen.convert("RGBA") """

    # Calcula el tamaño para que la imagen ocupe el 10% x 10% del código QR
    #ancho_qr, alto_qr = img_qr.size
    #ancho_imagen = int(ancho_qr * 0.15)
    #alto_imagen = int(alto_qr * 0.1)

    # Redimensiona la imagen a las dimensiones calculadas
    #img_imagen = img_imagen.resize((ancho_imagen, alto_imagen))

    # Calcula la posición para centrar la imagen en el código QR
    #x_pos = int((ancho_qr - ancho_imagen) / 2)
    #y_pos = int((alto_qr - alto_imagen) / 2)

    # Superpone la imagen en el centro del código QR
    #img_qr.paste(img_imagen, (x_pos, y_pos), img_imagen)

    # Guarda el código QR resultante con la imagen superpuesta
    img_qr.save(filename + ".png")

def create_pdf(logo, folio, partida, monto, fecha, fecha2, adm, mont, mont2):
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
    style_down = ParagraphStyle('Center', parent=styles['Normal'], alignment=2, spaceAfter=5, fontSize=11) 
    style_up = ParagraphStyle('Center', parent=styles['Normal'], alignment=2, spaceAfter=5, fontSize=17) 
    # Draw logo
    logo_width = 1.8 * cm
    logo_height = 1 * cm
    # Draw barcodes and list numbers
    for i, code in enumerate([1]):
        c.drawImage(logo, 0.5 *  cm, A4[1] - 2.9 * cm, width=logo_width, height=logo_height)
        # Generate barcode
        barcode_filename = f"temp/barcode_{i}"
        fol = str(folio[0])
        generate_barcode(barcode_filename, fol, partida, monto, fecha, fecha2, adm, mont, mont2)
        # Draw barcode
        barcode_width = 2.5 * cm
        barcode_height = 2.5 * cm
        with Image.open(barcode_filename + ".png") as img:
            #UBICACION CODIGO DE BARRAS PRIMERO ANCHO Y LUEGO ALTO
            c.drawInlineImage(img, A4[0] - 0.3 * cm - barcode_width, A4[1] - 2.35 * cm, width=barcode_width, height=barcode_height)
        # Draw list number in the center at the top with a 0.5 cm margin
        foli = str(folio).replace("[", "").replace("]", "")
        text = f"F: <b>{foli}</b> Adm: <b>{adm}</b>"
        p = Paragraph(text, style_up)
        p.wrapOn(c, A4[0] - 6 * cm, cm)
        #arriba abajo
        p.drawOn(c, cm, A4[1] - 2.2 * cm)
        p = Paragraph(text, style_down)
        p.wrapOn(c, A4[0] - 2 * cm, cm)
        p.drawOn(c, cm, 0.3 * cm)  # Cambia la coordenada Y para mover el texto hacia la parte inferior
        # Agregar un salto de página
        c.showPage()
    c.save()
    shutil.rmtree(carpetaTemporal)



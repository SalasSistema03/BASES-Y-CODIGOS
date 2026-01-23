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


def create_pdf(logo, folio, partida, monto, fecha, adm):
    time.sleep(1)
    # Create PDF with A4 size
    pdf_filename = "watermarck.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    # Define styles
    styles = getSampleStyleSheet()
    style_down = ParagraphStyle('Center', parent=styles['Normal'], alignment=2, spaceAfter=5, fontSize=20) 
    style_up = ParagraphStyle('Center', parent=styles['Normal'], alignment=2, spaceAfter=5, fontSize=15) 
    # Draw logo
    logo_width = 1.8 * cm
    logo_height = 1 * cm
    # Draw barcodes and list numbers
    c.drawImage(logo, cm, A4[1] - 29 * cm, width=logo_width, height=logo_height)
    text = f"F: <b>{folio}</b> Adm: <b>{adm}</b> {partida}"
    textd = f"F: <b>{folio}</b> Adm: <b>{adm}</b>"
    p = Paragraph(text, style_up)
    p.wrapOn(c, A4[0] - 10 * cm,  cm)
    p.drawOn(c, 8 * cm, A4[1] - 0.5 * cm)
    p = Paragraph(textd, style_down)
    p.wrapOn(c, A4[0] - 1 * cm, cm)
    p.drawOn(c, -1 * cm, 1 * cm)  # Cambia la coordenada Y para mover el texto hacia la parte inferior
    # Agregar un salto de página
    c.showPage()
    c.save()

import qrcode
from PIL import Image


def generar_qr_con_imagen_10porciento(texto, nombre_archivo_qr, nombre_archivo_imagen):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color="#0055B9", back_color="white")

    # Abre la imagen que deseas superponer en el centro
    img_imagen = Image.open(nombre_archivo_imagen)

    # Asegúrate de que la imagen tenga un canal alfa (canal de transparencia)
    if img_imagen.mode != "RGBA":
        img_imagen = img_imagen.convert("RGBA")

    # Calcula el tamaño para que la imagen ocupe el 10% x 10% del código QR
    ancho_qr, alto_qr = img_qr.size
    ancho_imagen = int(ancho_qr * 0.15)
    alto_imagen = int(alto_qr * 0.1)

    # Redimensiona la imagen a las dimensiones calculadas
    img_imagen = img_imagen.resize((ancho_imagen, alto_imagen))

    # Calcula la posición para centrar la imagen en el código QR
    x_pos = int((ancho_qr - ancho_imagen) / 2)
    y_pos = int((alto_qr - alto_imagen) / 2)

    # Superpone la imagen en el centro del código QR
    img_qr.paste(img_imagen, (x_pos, y_pos), img_imagen)

    # Guarda el código QR resultante con la imagen superpuesta
    img_qr.save(nombre_archivo_qr)

if __name__ == "__main__":
    # Texto que quieres codificar en el QR
    texto_para_qr = "1234567890123456789012345678901234567890"
    # Nombre del archivo de imagen del código QR que se generará
    nombre_archivo_qr = "verificadorQR.png"

    # Nombre del archivo de la imagen que deseas superponer
    nombre_archivo_imagen = "SALAS.png"


    generar_qr_con_imagen_10porciento(texto_para_qr, nombre_archivo_qr, nombre_archivo_imagen)
    print(f"Se ha generado el código QR en el archivo: {nombre_archivo_qr}")
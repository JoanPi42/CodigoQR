"""
Generador de QRs en color blanco con fondo transparente

Requisitos:
    pip install qrcode[pil] pillow
"""

import qrcode
from PIL import Image

def generar_qr_blanco_transparente(
    datos,
    ruta_salida = "qr_blanco_transparente.png",
    tamano = (400, 400),
    correccion_error=qrcode.constants.ERROR_CORRECT_H,
):
    """
    Genera un codigo QR blanco sobre fondo transparente

    Parametros:
    ----------
    datos : str
        Texto o URL que se codificara en el QR

    ruta_salida : str
        Ruta donde se guardara la imagen PNG resultante

    tamano
        Tamaño final del QR en pixeles (ancho, alto)

    correccion_error :
        Nivel de corrección de error del QR
        Opciones: ERROR_CORRECT_L, M, Q, H (H = más robusto)
    """

    # Crear objeto QR con configuracion base
    qr = qrcode.QRCode(
        version=2,  # Controla el tamaño del QR (1 = pequeño)
        error_correction=correccion_error,
        box_size=15,
        border=5,  # Margen alrededor del QR
    )

    # Agregar datos a codificar
    qr.add_data(datos)
    qr.make(fit=True)

    ancho, alto = tamano

    # Generar QR en escala de grises
    qr_imagen_gris = (
        qr.make_image(fill_color="white", back_color="black")
        .resize((ancho, alto))
        .convert("L")
    )

    # Crear imagen RGBA transparente
    qr_transparente = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))

    # Convertir pixeles negros a blanco opaco y el resto a transparente
    for y in range(alto):
        for x in range(ancho):
            pixel = qr_imagen_gris.getpixel((x, y))

            if pixel == 0:  # Negro → modulo del QR
                qr_transparente.putpixel((x, y), (0, 0, 0, 0))
            else:
                qr_transparente.putpixel((x, y), (255, 255,255, 255))

    # Guardar resultado
    qr_transparente.save(ruta_salida)

    print(f"Codigo QR generado correctamente")


# ======================
# EJEMPLO DE USO
# ======================

if __name__ == "__main__":
        url= input("¿Qué URL quieres convertir a QR?")

        url_sitio = "https://www.google.com/?hl=es_419"

        generar_qr_blanco_transparente(
            datos=url,
            ruta_salida="CodigoQR.png",
            tamano=(400, 400),
    )
# Generador de Códigos QR en Blanco con Fondo Transparente

Este repositorio contiene scripts en Python para generar códigos QR blancos sobre fondo transparente. Los QR pueden contener URLs o cualquier texto, y están pensados para ser fáciles de usar y personalizar.

## Requisitos

Instala las librerías necesarias antes de ejecutar los scripts:

```bash
pip install qrcode[pil] pillow
```

## Uso del script interactivo (CodigoQR_input.py)

Este script solicita al usuario que ingrese la URL o texto directamente en la ejecución del programa.

```bash
$ python qr_input.py
Ingresa la URL: https://example.com
Codigo QR generado correctamente
```

- Ideal para uso rápido

- No requiere argumentos adicionales

- Fácil de probar para principiantes

## Uso del script con argumentos de terminal (CodigoQR_sys.py)

Este script permite pasar la URL o texto directamente desde la terminal usando sys.argv.

```bash
$ python qr_argv.py https://example.com  #esto es desde la terminal en si
Codigo QR generado correctamente
```
- Ideal para automatización

- Permite integrarse en otros scripts

- Más eficiente para generar múltiples QR

## Configuración del QR

- Color del QR: blanco (`fill_color="white"`)

- Fondo: transparente (mediante RGBA)

- Tamaño: ajustable con el parámetro `tamano=(ancho, alto)`

- Corrección de error: ajustable con `qrcode.constants.ERROR_CORRECT_L, M, Q o H (H = más robusto)`

- Versión del QR: controla el tamaño general del QR (1 = pequeño, valores mayores = QR más grande)

## Ejemplos de QR generados

Dentro de la carpeta outputs/ puedes ver ejemplos generados con ambos scripts.

Tip: Cambia los nombres de las imágenes según los archivos que generes en tu carpeta outputs/.

# Generador de Códigos QR en Blanco con Fondo Transparente

Este repositorio contiene scripts en Python para generar códigos QR blancos sobre fondo transparente. Los QR pueden contener URLs o cualquier texto, y están pensados para ser fáciles de usar y personalizar.

## Requisitos

Instala las librerías necesarias antes de ejecutar los scripts:

```bash
pip install qrcode[pil] pillow
```

## Uso del script interactivo (qr_input.py)

Este script solicita al usuario que ingrese la URL o texto directamente en la ejecución del programa.

```bash
$ python qr_input.py
Ingresa la URL: https://example.com
Codigo QR generado correctamente en CodigoQR.png
```

- Ideal para uso rápido

- No requiere argumentos adicionales

- Fácil de probar para principiantes

## Uso del script con argumentos de terminal (qr_argv.py)

Este script permite pasar la URL o texto directamente desde la terminal usando sys.argv.

```bash
$ python qr_argv.py https://example.com
Codigo QR generado correctamente en CodigoQR.png
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

Dentro de la carpeta outputs/ puedes incluir ejemplos generados con ambos scripts. Por ejemplo:

QR generado con qr_input.py

QR generado con qr_argv.py

Tip: Cambia los nombres de las imágenes según los archivos que generes en tu carpeta outputs/.

##Estructura recomendada del repositorio

```bash

QR-Generator/
├─ qr_input.py         # script interactivo
├─ qr_argv.py          # script con argumentos de terminal
├─ outputs/            # ejemplos de QR generados
│   ├─ qr_input_example.png
│   └─ qr_argv_example.png
└─ README.md           # este archivo
```

import sys
from pathlib import Path

PALABRAS_SOSPECHOSAS = ["api_key", "apikey", "secret", "password", "token"]
ficheros = ["ventas.json"]

encontrado = False
for fichero in ficheros:
    contenido = Path(fichero).read_text().lower()
    for palabra in PALABRAS_SOSPECHOSAS:
        if palabra in contenido:
            print(f" Posible clave expuesta en {fichero}: '{palabra}'")
            encontrado = True

if encontrado:
    sys.exit(1)

print("Escaneo completado: no se han encontrado claves expuestas.")
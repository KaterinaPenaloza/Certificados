from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Lectura del archivo, lo pasamos a lista
datos = pd.read_csv("./nombres.csv", sep=",", header=None, names=['Nombres'])["Nombres"].to_list()

i = 0
for nombre in datos:
    # Plantilla del certificado
    certificado = Image.open("cert.jpg")

    # Estilo del certificado
    new = ImageDraw.Draw(certificado)
    coordenadas = (604,750) 
    color_texto = (37,233,27)
    tipo_letra = ImageFont.truetype("retro_computer.ttf", 50) 

    # Generacion certificado
    new.text(coordenadas, datos[i], fill=color_texto, font=tipo_letra)

    # Salida
    print(datos[i])
    certificado.save(datos[i]+".pdf")

    i = i + 1

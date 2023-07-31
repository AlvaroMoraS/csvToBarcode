"""
Este programa busca generar imágenes en formato .png en base a datos de entrada entregados
por el usuario mediante un archivo example.csv, 
el cual tiene 2 campos: nombre del producto y número del código de barra
Importante 1: el archivo .csv tiene ambos campos separados por ";".
Importante 2: aquí se usará el modelo EAN, que utiliza 12 dígitos para la generación de código de barra. Ejemplo: "123456789123" 

Es requisito además, tener una carpeta dentro del proyecto llamada "generatedBarcodes", ya que aquí
se generarán las imágenes de los códigos de barra.
"""

#Librerías necesarias:
from barcode import EAN13
from barcode.writer import ImageWriter
import csv


# Función que genera el código de barra como imagen .png
def generatorBarcodes(numero,nombreProducto,directorio):
  generatedBarcode = EAN13(numero, writer=ImageWriter())
  generatedBarcode.save(directorio+"/"+nombreProducto+"_"+numero)



if __name__ == '__main__':
   # Directorio donde serán guardados los códigos de barra:   
   directorio = r'./generatedBarcodes'

   # Archivo .csv que tiene el nombre y el número del código de barra que se requiere
   archivo = 'example.csv'

   # Lee el archivo example.csv, línea por línea, y entrega los valores a la función para que genere la imagen de los códigos de barra
   with open(archivo, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        generatorBarcodes((row[1]),row[0],directorio)
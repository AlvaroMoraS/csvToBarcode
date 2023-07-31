# English
## CSV to Barcode Image (.png), with Python
This program aims to generate images in .png format based on input data provided by the user through an **example.csv** file, which contains 2 fields: product name and barcode number. 

Important Note 1: The .csv file has both fields separated by ";". 
Important Note 2: The EAN model will be used here, which uses 12 digits for barcode generation. For example: "123456789123".

It is also a requirement to have a folder named "generatedBarcodes" within the project, as this is where the barcode images will be generated.

## How to make it work?
```sh
git clone
cd csvToBarcode
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```


# Español
## CSV a imagen de código de barra (.png), con Python
Este programa busca generar imágenes en formato .png en base a datos de entrada entregados por el usuario mediante un archivo **example.csv**, el cual tiene 2 campos: nombre del producto y número del código de barra.
Importante 1: el archivo .csv tiene ambos campos separados por ";".
Importante 2: aquí se usará el modelo EAN, que utiliza 12 dígitos para la generación de código de barra. Ejemplo: "123456789123"

Es requisito además, tener una carpeta dentro del proyecto llamada "generatedBarcodes", ya que aquí se generarán las imágenes de los códigos de barra.

## ¿Cómo hacerlo funcionar?
```sh
git clone
cd csvToBarcode
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```
import requests
from io import StringIO #parsea
import csv


url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSBw_ZhGrR2wJ4HVlaiy2I2YjGvrVAH_YFtTjnsm20BOuEMp-iNZ5IeYvLQ9tT22rpo_z0ZuDGeyN74/pub?output=csv'

respuesta = requests.get(url)
contenido = respuesta.text
file = StringIO(contenido)
objeto_csv = csv.reader(file)

with open('pelis_google.csv','w') as pelis:
    for linea in objeto_csv:
        fila = ','.join([linea[0],linea[1],linea[3]])
        pelis.write(fila + '\n')
        
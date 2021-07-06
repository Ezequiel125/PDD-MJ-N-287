import requests
import json
from pprint import pprint
import csv

claves = open ('E:/Curso/claves.txt')
log = open('log_error.txt','w')
listas_claves = [clave.strip('/n') for clave in claves]
key = listas_claves[0]


archivo = open('sucursales_sol_360.csv')
archivo_csv =csv.reader(archivo,delimiter=';')
ciudades = [linea[0] for linea in archivo_csv]

for ciudad in ciudades:
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + ciudad +',AR&units=metric&lang=es&appid=' + key
    objeto = json.loads(requests.get(url).text)
    try:
        print('El clima en', ciudad, 'es:', str(objeto['weather'][0]['description']))
        print ('La temp es',objeto['main']['temp'],'°C')
        print('La humedad del',objeto['main']['humidity'],'%\n')
    except:
        log.write(ciudad + '- No se encontro\n')
    
log.close()
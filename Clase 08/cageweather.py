import requests
import json
from pprint import pprint
import csv

claves = open ('E:/Curso/claves.txt')
log = open('log_error.txt','w')
listas_claves = [clave.strip('\n') for clave in claves]
key_open_weather = listas_claves[0]
key_open_cage = listas_claves[1]

archivo = open('sucursales_sol_360.csv')
archivo_csv =csv.reader(archivo,delimiter=';')
ciudades = [linea[0] for linea in archivo_csv]

for ciudad in ciudades:
    ciudad_cod = requests.utils.quote(ciudad)
    url = 'https://api.opencagedata.com/geocode/v1/json?q=' + ciudad_cod + ',Argentina&key=' + key_open_cage
    objeto = json.loads(requests.get(url).text)
    lat = objeto['results'][0]['geometry']['lat']
    long = objeto['results'][0]['geometry']['lng']
    #print(lat,long)
    
    #pprint(objeto)
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(long) +'&units=metric&lang=es&appid=' + key_open_weather
    objeto = json.loads(requests.get(url).text)
    try:
        print('El clima en', ciudad, 'es:', str(objeto['weather'][0]['description']))
        print ('La temp es',objeto['main']['temp'],'°C')
        print('La humedad del',objeto['main']['humidity'],'%\n')
    except:
        log.write(ciudad + '- No se encontro\n')
    
log.close()
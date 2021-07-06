import requests
import json
from pprint import pprint
import csv

claves = open ('E:/Curso/claves.txt')
listas_claves = [clave.strip('/n') for clave in claves]
key = listas_claves[0]

ciudad = 'San Juan, Argentina'
ciudad_cod = requests.utils.quote(ciudad) #codifico ciudad

url = 'https://api.openweathermap.org/data/2.5/weather?q=' + ciudad_cod +'&units=metric' + '&lang=es' +'&appid=' + key

objeto = json.loads(requests.get(url).text)
#pprint(objeto)
print('El clima en', ciudad, 'es:', objeto['weather'][0]['description'])


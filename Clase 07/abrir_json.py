import json
from pprint import pprint

with open('amo.json') as archivo:
    objeto = json.load(archivo)
    
pprint(objeto['amo']['mascota'][0]['le_gusta'][0])
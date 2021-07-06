from pprint import pprint
import json
import requests
from io import StringIO #otro metodo para parsear txt a json
import csv

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson'

contenido = requests.get(url).text #no me sirve lo trae como texto
objeto = json.loads(contenido) #agrego S a load



objetos = objeto['features']

with open('hospitales.csv','w',newline="",encoding='utf-8') as archivo_out:
    salida = csv.writer(archivo_out)
    salida.writerow(['Nombre','Direccion','Telefono','Especialidad', 'Web'])
    for objeto in objetos:
        nombre = objeto['properties'].get('NOMBRE','N/A')
        dire = objeto['properties'].get('DOM_NORMA','N/A')
        telefono = objeto['properties'].get('TELEFONO','N/A')
        especialidad = objeto['properties'].get('TIPO_ESPEC','N/A')
        pag_web = objeto['properties'].get('WEB','N/A')
        print([nombre,dire,telefono,especialidad,pag_web])
        salida.writerow([nombre , dire , telefono , especialidad, pag_web])

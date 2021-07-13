from pymongo import MongoClient

import requests

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/vicejefatura-de-gobierno/estaciones-saludables/estaciones-saludables.geojson'

req = requests.get(url)

data = req.json()

client2 = MongoClient(host='mongodb://localhost:27017')

db = client2['salud']

collection = db['estaciones_saludables']

collection.insert_many(data['features'])
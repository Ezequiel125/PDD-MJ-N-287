import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint


url = 'https://helena.anmat.gob.ar/Boletin/'
respuesta = requests.get(url)
respuesta.encoding = 'utf-8'
html = respuesta.text
dom = BS(html, features='html.parser')

tablas = dom.find_all('a')
titulos = dom.find('tr',class_='info' )
print(tablas.get('href','nono'))




        
    
    
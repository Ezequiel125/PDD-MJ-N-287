import mysql.connector as sql
from bs4 import BeautifulSoup as BS
import requests

# Scrapeo
url = 'https://www.cuspide.com/cienmasvendidos'
respuesta = requests.get(url)
respuesta.encoding = 'utf-8'
html = respuesta.text

dom = BS(html, features='html.parser')

articulos = dom.find_all('article')

tabla = []
for articulo in articulos:
    titulo = articulo.figure.div.a.get('title','no encontrado')
    ref = articulo.figure.div.a.get('href','no encontrado')
    url_ref='https://www.cuspide.com' + ref
    respuesta = requests.get(url_ref)
    respuesta.encoding = 'utf-8'
    html = respuesta.text
    dom1 = BS(html, features='html.parser')
    precios = dom1.find('meta',itemprop = 'price')
    price = precios['content']
    lista = [titulo , price]
    tabla.append(lista)
    
print(tabla)
# BASE DE DATOS
conexion = sql.connect(host = 'cloud.eant.tech',
                       database = 'pdp_base008',
                       user = 'pdp_usuario008',
                       password = 'eantpass')

cursor = conexion.cursor()

query_create=( ''' CREATE TABLE IF NOT EXISTS pdp_base008.libros 
              ( id INT NOT NULL AUTO_INCREMENT , 
               titulo VARCHAR(100) NULL , 
               precio VARCHAR(100) NULL ,                 
               PRIMARY KEY (id))''')

cursor.execute(query_create)
conexion.commit()

query_insert = '''INSERT INTO libros(titulo,precio)
                      Values(%s,%s)'''
cursor.executemany(query_insert,tuple(tabla))
conexion.commit()
    

cursor.close()
conexion.close()
    
    

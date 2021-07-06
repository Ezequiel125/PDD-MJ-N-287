import csv
import psycopg2  as sql

conexion = sql.connect(host = 'localhost',
                       port = '5433',
                       database = 'prueba',
                       user = 'postgres',
                       password = '123')

cursor = conexion.cursor()

query_create=( ''' CREATE TABLE IF NOT EXISTS public.ofertas 
              ( id INT NOT NULL , 
               nombre VARCHAR(100) NULL , 
               direccion VARCHAR(100) NULL , 
               comuna VARCHAR(100) NULL , 
               PRIMARY KEY (id))''')

cursor.execute(query_create)
conexion.commit()

with open('oferta_gastronomica.csv',encoding='utf-8') as archivo_in:
    entrada=csv.reader(archivo_in)
    next(entrada)
    
    for lineas in entrada:
        id = lineas[2]
        nombre = lineas[3]
        direccion = lineas[13]
        comuna = lineas[15]
        
        query_insert = '''INSERT INTO ofertas(id,nombre,direccion,comuna)
           Values(%s,%s,%s,%s)'''
        cursor.execute(query_insert,(id,nombre,direccion,comuna))
        conexion.commit()
    



cursor.close()
conexion.close()


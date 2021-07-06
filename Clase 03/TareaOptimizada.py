import csv
import mysql.connector as sql

conexion = sql.connect(host = 'cloud.eant.tech',
                       database = 'pdp_base008',
                       user = 'pdp_usuario008',
                       password = 'eantpass')

cursor = conexion.cursor()

query_create=( ''' CREATE TABLE IF NOT EXISTS pdp_base008.ofertas 
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
    values = [tuple([lineas[2],lineas[3],lineas[13],lineas[15]]) for lineas in entrada] ##Listcomprehesion!!
    
        
        
query_insert = '''INSERT INTO ofertas(id,nombre,direccion,comuna)
                      Values(%s,%s,%s,%s)'''
cursor.executemany(query_insert,tuple(values)) ##Executemany!!!!
conexion.commit()
    

cursor.close()
conexion.close()
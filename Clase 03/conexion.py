import mysql.connector as sql

conexion = sql.connect(host = 'cloud.eant.tech',
                       database = 'pdp_base008',
                       user = 'pdp_usuario008',
                       password = 'eantpass')

cursor = conexion.cursor()

query = '''SELECT id,nombre,apellido,dni 
           FROM alumnos
           WHERE nombre IN ('Cristian','Leonardo')'''
cursor.execute(query)

for alumno in cursor:
    print(alumno)



cursor.close()
conexion.close()
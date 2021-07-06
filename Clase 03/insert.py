import mysql.connector as sql

conexion = sql.connect(host = 'cloud.eant.tech',
                       database = 'pdp_base008',
                       user = 'pdp_usuario008',
                       password = 'eantpass')

cursor = conexion.cursor()

#query = '''INSERT INTO alumnos(nombre,apellido,dni,email,fecha_nac)
           #VALUES("Angel","Nadie","3654123","angel@nada","1999-03-12")'''
nombre = 'Tigre'
apellido = 'Blanco'
dni = '34343234'
email = 'tigra@nada.com'
fecha_nac = '2001-12-12'
           
query = '''INSERT INTO alumnos(nombre,apellido,dni,email,fecha_nac)
           Values(%s,%s,%s,%s,%s)'''
           
cursor.execute(query,(nombre,apellido,dni,email,fecha_nac))
conexion.commit()


cursor.close()
conexion.close()
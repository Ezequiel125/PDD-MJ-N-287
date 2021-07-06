import mysql.connector as sql

conexion = sql.connect(host = 'cloud.eant.tech',
                       database = 'pdp_base008',
                       user = 'pdp_usuario008',
                       password = 'eantpass')

cursor = conexion.cursor()
cursor.execute("SELECT dni FROM alumnos")
lista_dnis = [dni[0] for dni in cursor]



c = 'SI'
while c == 'SI':
    dni=input('Tu dni?: ')
    if int(dni) in lista_dnis: print('Este DNI ya fue ingresado')
    else:
        lista_dnis.append(int(dni))
        nombre= input('Cual es tu nombre?: ')
        apellido= input('Tu apellido?: ')
        email=input('Tu email?: ')
        fecha_nac=input('Fecha de Nacimiento?:(formato AAAA-MM-DD) ')
        query = '''INSERT INTO alumnos(nombre,apellido,dni,email,fecha_nac)
               Values(%s,%s,%s,%s,%s)'''
        cursor.execute(query,(nombre,apellido,dni,email,fecha_nac))
    c=input('Desea continuar SI o NO: ')

conexion.commit()
cursor.close()
conexion.close()

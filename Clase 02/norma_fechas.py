from datetime import datetime

#fecha salida =  '13-02-2019'

fecha = '13/2/2019'
objeto_fecha = datetime.strptime(fecha, '%d/%m/%Y') #indico como entra
fecha_normalizada = datetime.strftime(objeto_fecha,'%d-%m-%Y' ) 
print(fecha,objeto_fecha,fecha_normalizada)
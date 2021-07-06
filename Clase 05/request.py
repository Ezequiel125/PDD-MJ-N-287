import requests

url = 'https://eant.tech/cursos/recursos/frutas.txt'
respuesta = requests.get(url)

print('Codigo de rta:', respuesta.status_code) #codigo 200 ok, codigo 404 not found
print('URl de origen', respuesta.url)
print('Contenido:',respuesta.content)
print('Contenido Txt',respuesta.text)
print('Codificacion',respuesta.encoding)
respuesta.encoding = 'utf-8'
print('Contenido Txt',respuesta.text)

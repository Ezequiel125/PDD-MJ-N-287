from pprint import pprint
import json
#Variable
x = 0
#Lista
lista = []
#Tupla
tupla = ()
#Diccionario
diccionario = {}

perro = {'nombre':'Rocco',
         'tipo' : 'perro',
         'raza' : 'Labrador'
         }
edad = 5
le_gusta = ['comer','correr a las palomas','ladrar de noche']

#Combinacion
perro.update({'edad' : edad})
perro.update({'le_gusta': le_gusta})

#pprint(perro)

#Nuevo objeto amo
amo = {'nombre' : 'Robert',
       'tiro' : 'Humano',
       'le_gusta' : ['Una buena conver','Animales','Futbol'],
       'edad' : 45,
       'mascota' : perro
       }

#pprint(amo)

gato = {'nombre' : 'Cuqui',
        'tipo' : 'gato',
        'raza' : 'siames',
        'edad' : 6,
        'le_gusta' : ['comer','dormir']
        }


pez = { 'nombre' : 'nemo',
        'tipo' : 'pez',
        'raza' : 'payaso',
        'edad' : 1,
        'le_gusta' : ['comer','madar']
       }

mascotas =[pez,gato,perro]

amo.update({'mascota': mascotas})
#pprint(amo)
objeto = {'amo' : amo}
with open('amo.json','w',encoding = 'utf-8') as archivo_json:
    json.dump(objeto, archivo_json,indent = 3,ensure_ascii=False)
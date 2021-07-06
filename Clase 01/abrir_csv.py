archivo = open('subtes.csv',encoding='utf-8')

for subtes in archivo:
    subtes = subtes.strip('\n')
    lista = subtes.split(',')
    print(lista[2])
archivo_in = open('subtes.csv',encoding='utf-8')
archivo_out = open('subtes_salidas.csv','w',encoding='utf-8')

for linea in archivo_in :
    linea = linea.strip('\n')
    lista = linea.split(',')
    print(lista[2],lista[1],lista[0])
    archivo_out.write(lista[2] + ',' +  lista[1] + ',' + lista[0] + '\n')



archivo_in.close()
archivo_out.close()
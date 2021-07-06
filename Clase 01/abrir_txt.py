archivo = open('frutas.txt','r', encoding='utf-8') #newline='\r' saco ultimo caracter#
for lineas in archivo :
    #lineas = lineas[:-1]
    #lineas = lineas.strip('\n')
    lineas = lineas.replace('\n', '')
    print(lineas)
    
archivo.close()
    


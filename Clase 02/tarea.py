import funciones_norma as fn
import csv

with open('reclamos.csv',encoding='ansi') as archivo_in , open('reclamos2.csv','w', newline='',encoding='ansi') as archivo_out:
    entrada = csv.reader(archivo_in,delimiter=';')
    salida = csv.writer(archivo_out, delimiter=';')
    
    for lineas in entrada:
        try:    
           lineas[3] = fn.normalizadorFechas(lineas[3],'%d-%m-%Y')
        except:
            try:
               lineas[3] = fn.normalizadorFechas(lineas[3], '%Y-%m-%d')
            except:
                try:
                  lineas[3] =  fn.normalizadorFechas(lineas[3], '%d/%m/%y')
                except:
                    try:
                      lineas[3] =  fn.normalizadorFechas(lineas[3], '%d/%m/%Y')
                    except:
                        try:
                          lineas[3] =  fn.normalizadorFechas(lineas[3],'%Y-%d-%m')
                        except:
                            try:
                                lineas[3] = fn.normalizadorFechas(fn.traductorFecha2(lineas[3]),'%d %m %Y')
                            except:
                                try:
                                  lineas[3] =  fn.normalizadorFechas(lineas[3], '%y-%m-%d')
                                except:
                                     try:
                                       lineas[3] =  fn.normalizadorFechas(lineas[3], '%y-%d-%m')
                                     except:
                                         print('a')
                                        
        salida.writerow([lineas[0],lineas[1],lineas[2],lineas[3]])
                                         
                                        
                                           
  
import funciones_norma as fn

fecha = "13 days after February 2019"

try:
    fn.normalizadorFechas( fecha, '%d days after %B %Y')
    print('metodo 1')
except:
    try:
        fn.normalizadorFechas(fecha, '%d days %B %Y')
        print('metodo 2')
    except:
        print('No funciono')
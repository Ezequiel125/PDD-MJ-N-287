import funciones_norma as fn
    

fn.normalizadorFechas("02/19",'%m/%y' )

fn.normalizadorFechas("20191302", '%Y%d%m')

fn.normalizadorFechas("2019-13-02 14:23:33", '%Y-%d-%m %H:%M:%S')

fn.normalizadorFechas('13/Feb/2019','%d/%b/%Y' )

fn.normalizadorFechas("13/February/2019", '%d/%B/%Y')
fn.normalizadorFechas( "13 days after February 2019", '%d days after %B %Y')


fecha = "13/Febrero/2019"
fn.normalizadorFechas(fn.traductorFecha(fecha),'%d%m%Y')
from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import sleep

#Primero despliego todo el DOM
driver = webdriver.Chrome('E:/Curso/chromedriver.exe')

driver.get('https://www.lanacion.com.ar/')

script_js = """
let fin_de_pantalla = document.body.scrollHeight
window.scrollTo(0,fin_de_pantalla)
return fin_de_pantalla
"""
sleep(3)

pos_actual = 0
pos_siguiente = driver.execute_script(script_js)
sleep(3)

while pos_actual != pos_siguiente:
    pos_siguiente = pos_actual
    pos_actual = driver.execute_script(script_js)
    sleep(3)
    print(pos_actual)
print('final')


html = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()


dom = BS(html, features='html.parser')
titulares = dom.find_all('h2')#(class_="com-title --xs" or "com-title --xl")
print('Titulares:' , len(titulares))
for titulos in titulares:
    titulo = titulos.text
    vinculo = titulos.a['href']
    print(titulo, '-', vinculo)

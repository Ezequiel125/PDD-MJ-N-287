from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import sleep
from pprint import pprint
import requests

options = webdriver.ChromeOptions()
#options.add_argument("headless") para que no abra el navegador
options.add_argument("--incognito")
driver = webdriver.Chrome('E:/Curso/chromedriver.exe', options=options)

url = 'https://supermercado.carrefour.com.ar/cerveza?_q=cerveza&map=ft'
driver.get(url)
sleep(10)
script_boton = """
let boton = document.querySelector('[class="vtex-button__label flex items-center justify-center h-100 ph5 "]')
if (boton){
        boton.click()
        }
else{
    return "No exsiste"
          }
     
"""
script_scroll = """fondoDePantalla = document.body.scrollHeight
    for (let i = 0; i < fondoDePantalla; i += 50){
          setInterval(function(){window.scrollTo(0, i)}, 1000)
          };
          """

driver.execute_script(script_scroll)
sleep(5)
while driver.execute_script(script_boton) != "No exsiste":
   sleep(4)
   driver.execute_script(script_scroll)
   sleep(4)


html = driver.execute_script("return document.documentElement.outerHTML")

###############################################

dom = BS(html, features='html.parser')

links = dom.find_all('div',class_='lyracons-search-result-1-x-galleryItem lyracons-search-result-1-x-galleryItem--normal pa4')
url1 = 'https://www.carrefour.com.ar/'
urlf_list = []
promolist = []
preciolist = []
for link in links:
    #print(link.section.a['href'])
    href= link.section.a['href'].strip('/n')
    #print(href)
    #href_list.append(href)
    url_ref= url1 + href
    urlf_list.append(url_ref)
    driver.get(url_ref)
    sleep(20)
    html2 = driver.execute_script("return document.documentElement.outerHTML")
    #respuesta = requests.get(url_ref)
    #respuesta.encoding = 'utf-8'
   #html = respuesta.text
    dom2 = BS(html2, features='html.parser')
    descripcion = link.h1.span.text
    marca= dom2.find(class_= 'vtex-store-components-3-x-productBrandName' ).text
    precio_int = dom2.find(class_='lyracons-carrefourarg-product-price-1-x-currencyInteger').string
    precio_dec = dom2.find(class_='lyracons-carrefourarg-product-price-1-x-currencyFraction').string
    precio = float(precio_int + '.' + precio_dec)
    try:
        promo = dom2.find_all(class_='lyracons-carrefourarg-product-highlights-1-x-productHighlightText').text
    except: 
        promo = 'No tiene promo'
    promolist.append(promo)
    preciolist.append(precio)
    
    
    
    
    

   



    

    

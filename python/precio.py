from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe")
el = driver.find_element_by_tag_name('body')
str1 = el.text

paginas = ("https://www.coolmod.com/msi-geforce-rtx-3060-ti-ventus-3x-oc-8gb-gddr6-tarjeta-grafica-precio", "https://www.pccomponentes.com/amd-ryzen-5-3600-36ghz-box")

for i in paginas:
    driver.get(i)
    x = str1.find("Comprar")

    if(x != -1):
        print("Disponible")
    else: 
        print("No disponible")

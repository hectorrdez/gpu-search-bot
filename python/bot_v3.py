from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)


import datetime
import time

x = datetime.datetime.now()

driver = webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe")

p = 0
m = 0
n = 0

pagina = ["Coolmod","Pccomponentes","Amazon.es"]
nvidia_modelo = ["RTX 3060","RTX 3060 TI","RTX 3070","RTX 3080","RTX 3090"]
modelo_marca = ["MSI","Gigabyte","ASUS"]
nombre_modelo = ["Ventus x3"]
links = ["https://www.pccomponentes.com/amd-ryzen-5-3600-36ghz-box"]
for pag in pagina:
    p = p + 1
    c_pag = pagina[p-1]
    n = 0
    for modelo in nvidia_modelo:
        n = n+1
        n_modelo = nvidia_modelo[n - 1]
        m = 0
        for marca in modelo_marca:
            m = m + 1
            n_marca = modelo_marca[m-1]
            z = 0
            for link in links:
                driver.get(link)
                el = driver.find_element_by_tag_name('body')
                str1 = el.text
                z = z+1
                nombre1_modelo = nombre_modelo[z-1]
                if(str1.find("Comprar")!=-1):
                    print("["+x.strftime("%X")+"]"+Fore.CYAN+"["+c_pag+"]"+Style.RESET_ALL+"["+n_modelo+"]["+n_marca+"]["+nombre1_modelo+"]:"+Fore.GREEN+"IN STOCK")
                else:
                    print("["+x.strftime("%X")+"]"+Fore.CYAN+"["+c_pag+"]"+Style.RESET_ALL+"["+n_modelo+"]["+n_marca+"]["+nombre1_modelo+"]:"+Fore.RED+"OUT OF STOCK")

                time.sleep(1)
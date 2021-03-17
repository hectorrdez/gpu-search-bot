from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from playsound import playsound
import datetime
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

x = datetime.datetime.now()
rev = 0
p = 0
NOMBRE = "salida.mp3"
pagina = ''

driver = webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe")

#RTX3060#

paginas_coolmod_nombre_gpu_3060 = ["https://www.coolmod.com/msi-geforce-rtx-3060-gaming-x-12gb-gddr6-tarjeta-grafica-precio","https://www.coolmod.com/msi-geforce-rtx-3060-gaming-x-trio-12gb-gddr6-tarjeta-grafica-precio","https://www.coolmod.com/msi-geforce-rtx-3060-ventus-3x-oc-12gb-gddr6-tarjeta-grafica-precio","https://www.coolmod.com/msi-geforce-rtx-3060-ventus-2x-oc-12gb-gddr6-tarjeta-grafica-precio","https://www.coolmod.com/msi-geforce-rtx-3060-ventus-2x-12gb-gddr6-tarjeta-grafica-precio","https://www.coolmod.com/pny-geforce-rtx-3060-xlr8-gaming-revel-epic-x-rgb-single-fan-12gb-gddr6-tarjeta-grafica-precio","https://www.coolmod.com/zotac-geforce-rtx-3060-twin-edge-12gb-gddr6-tarjeta-grafica-precio","https://www.coolmod.com/asus-tuf-gaming-geforce-rtx-3060-12gb-gddr6-tarjeta-grafica-precio"]
paginas_coolmod_nombre_gpu_3060 = ["MSI GeForce® RTX 3060 GAMING X 12GB GDDR6","MSI GeForce® RTX 3060 GAMING X TRIO 12GB GDDR6","MSI GeForce® RTX 3060 VENTUS 3X OC 12GB GDDR6","MSI GeForce® RTX 3060 VENTUS 2X OC 12GB GDDR6","MSI GeForce® RTX 3060 VENTUS 2X 12GB GDDR6","PNY GeForce® RTX 3060 XLR8 Gaming REVEL EPIC-X RGB Single Fan 12GB GDDR6","Zotac GeForce® RTX 3060 Twin Edge 12GB GDDR6","Asus TUF Gaming GeForce® RTX 3060 12GB GDDR6"]
for pag in paginas_coolmod_nombre_gpu_3060:
    driver.get(pag)
    el = driver.find_element_by_tag_name('body')
    str1 = el.text
    p = p + 1
    pagina = paginas_coolmod_nombre_gpu_3060[p-1]

    if(str1.find("Comprar")!=-1):
        print("["+ x.strftime("%X") +"]"+"[Coolmod][Rtx 3060]:"+ bcolors.OKGREEN+''.join(pagina))
        playsound(NOMBRE)

    else:
       rev = rev + 1


if(p == rev):
    print("["+ x.strftime("%X") +"]"+ "[Coolmod][Rtx 3060]:"+Fore.RED+"OUT OF STOCK")


rev = 0
p = 0

#RTX3070#
paginas_coolmod_nombre_gpu_3070 = ["https://www.coolmod.com/gigabyte-geforce-rtx-3060-eagle-oc-12gb-gddr6-tarjeta-grafica-precio"]
paginas_coolmod_nombre_gpu_3070 = ["Gygabyte RTX 3060 EAGLE OC 12GB"]
for pag in paginas_coolmod_nombre_gpu_3070:
    driver.get(pag)
    el = driver.find_element_by_tag_name('body')
    str1 = el.text
    p = p + 1
    pagina = paginas_coolmod_nombre_gpu_3070[p-1]

    if(str1.find("Comprar")!=-1):
        print("["+ x.strftime("%X") +"]"+"[Coolmod][Rtx 3070]:"+ bcolors.OKGREEN+''.join(pagina))
        playsound(NOMBRE)

    else:
       rev = rev + 1


if(p == rev):
    print("["+ x.strftime("%X") +"]"+ "[Coolmod][Rtx 3070]:"+Fore.RED+"OUT OF STOCK")

#RTX 3080#
rev = 0
p = 0

paginas_coolmod_nombre_gpu_3080 = ["https://www.coolmod.com/zotac-gaming-geforce-rtx-3080-trinity-oc-10gb-gddr6x-tarjeta-grafica-precio","https://www.coolmod.com/msi-geforce-rtx-3080-suprim-x-10gb-gddr6x-tarjeta-grafica-precio","https://www.coolmod.com/evga-geforce-rtx-3080-ftw3-gaming-10gb-gddr6x-tarjeta-grafica-precio","https://www.coolmod.com/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6x-tarjeta-grafica-precio","https://www.coolmod.com/evga-geforce-rtx-3080-xc3-gaming-10gb-gddr6x-tarjeta-grafica-precio","https://www.coolmod.com/evga-geforce-rtx-3080-xc3-black-gaming-10gb-gddr6x-tarjeta-grafica-precio","https://www.coolmod.com/pny-geforce-rtx-3080-xlr8-gaming-epic-x-rgb-10gb-gddr6x-tarjeta-grafica-precio","https://www.coolmod.com/pny-geforce-rtx-3080-10gb-xlr8-gaming-epic-x-rgb-10gb-gddr6x-tarjeta-grafica-precio","https://www.coolmod.com/msi-geforce-rtx-3080-ventus-3x-oc-10gb-gddr6x-tarjeta-grafica-precio","https://www.coolmod.com/zotac-gaming-geforce-rtx-3080-trinity-10gb-gddr6x-tarjeta-grafica-precio"]
paginas_coolmod_nombre_gpu_3080 = ["Zotac Gaming GeForce® RTX 3080 Trinity OC 10GB GDDR6X","MSI GeForce® RTX 3080 SUPRIM X 10GB GDDR6X","EVGA GeForce® RTX 3080 FTW3 Gaming 10GB GDDR6X","EVGA GeForce® RTX 3080 XC3 Ultra Gaming 10GB GDDR6X","EVGA GeForce® RTX 3080 XC3 Gaming 10GB GDDR6X","EVGA GeForce® RTX 3080 XC3 Black Gaming 10GB GDDR6X","PNY GeForce® RTX 3080 XLR8 Gaming EPIC-X RGB 10GB GDDR6X","PNY GeForce® RTX 3080 10GB XLR8 Gaming EPIC-X RGB 10GB GDDR6X","MSI GeForce® RTX 3080 VENTUS 3X OC 10GB GDDR6X","Zotac GAMING GeForce® RTX 3080 Trinity 10GB GDDR6X"]
for pag in paginas_coolmod_nombre_gpu_3080:
    driver.get(pag)
    el = driver.find_element_by_tag_name('body')
    str1 = el.text
    p = p + 1
    pagina = paginas_coolmod_nombre_gpu_3080[p-1]

    if(str1.find("Comprar")!=-1):
        print("["+ x.strftime("%X") +"]"+"[Coolmod][Rtx 3080]:"+ bcolors.OKGREEN+''.join(pagina))
        playsound(NOMBRE)

    else:
       rev = rev + 1


if(p == rev):
    print("["+ x.strftime("%X") +"]"+ "[Coolmod][Rtx 3080]:"+Fore.RED+"OUT OF STOCK")

#RTX 3090#
rev = 0
p = 0

paginas_coolmod_nombre_gpu_3090 = ["https://www.coolmod.com/kfa2-geforce-rtx-3090-hof-premium-24gb-gddr6x-tarjeta-grafica-precio", "https://www.coolmod.com/gigabyte-aorus-geforce-rtx-3090-xtreme-waterforce-wb-24gb-gddr6x-tarjeta-grafica-precio", "https://www.coolmod.com/kfa2-geforce-rtx-3090-hof-24gb-gddr6x-tarjeta-grafica-precio","https://www.coolmod.com/kfa2-geforce-rtx-3090-hof-limited-edition-24gb-gddr6x-tarjeta-grafica-precio","https://www.coolmod.com/msi-geforce-rtx-3090-suprim-x-24gb-gddr6x-tarjeta-grafica-precio", "https://www.coolmod.com/evga-geforce-rtx-3090-xc3-ultra-gaming-24gb-gddr6x-tarjeta-grafica-precio", "https://www.coolmod.com/evga-geforce-rtx-3090-xc3-black-gaming-24gb-gddr6x-tarjeta-grafica-precio", "https://www.coolmod.com/evga-geforce-rtx-3090-xc3-gaming-24gb-gddr6x-tarjeta-grafica-precio", "https://www.coolmod.com/pny-geforce-rtx-3090-xlr8-gaming-epic-x-rgb-24gb-gddr6x-tarjeta-grafica_76404-precio", "https://www.coolmod.com/pny-geforce-rtx-3090-xlr8-gaming-epic-x-rgb-24gb-gddr6x-tarjeta-grafica-precio","https://www.coolmod.com/msi-geforce-rtx-3090-gaming-x-trio-24gb-gddr6x-tarjeta-grafica-precio", "https://www.coolmod.com/zotac-gaming-geforce-rtx-3090-trinity-24gb-gddr6x-tarjeta-grafica-precio"]
paginas_coolmod_nombre_gpu_3090 = ["KFA2 GeForce® RTX 3090 HOF Premium 24GB GDDR6X","Gigabyte AORUS GeForce® RTX 3090 Xtreme Waterforce WB 24GB GDDR6X","KFA2 GeForce® RTX 3090 HOF 24GB GDDR6X", "KFA2 GeForce® RTX 3090 HOF Limited Edition 24GB GDDR6X","MSI GeForce® RTX 3090 SUPRIM X 24GB GDDR6X","EVGA GeForce® RTX 3090 XC3 Ultra Gaming 24GB GDDR6X","EVGA GeForce® RTX 3090 XC3 Black Gaming 24GB GDDR6X","EVGA GeForce® RTX 3090 XC3 Gaming 24GB GDDR6X","PNY GeForce® RTX 3090 XLR8 Gaming EPIC-X RGB 24GB GDDR6X","PNY GeForce® RTX 3090 XLR8 Gaming EPIC-X RGB 24GB GDDR6X","MSI GeForce® RTX 3090 GAMING X TRIO 24GB GDDR6X","Zotac GAMING GeForce® RTX 3090 Trinity 24GB GDDR6X"]
for pag in paginas_coolmod_nombre_gpu_3090:
    driver.get(pag)
    el = driver.find_element_by_tag_name('body')
    str1 = el.text
    p = p + 1
    pagina = paginas_coolmod_nombre_gpu_3090[p-1]

    if(str1.find("Comprar")!=-1):
        print("["+ x.strftime("%X") +"]"+"[Coolmod][Rtx 3090]:"+ bcolors.OKGREEN+''.join(pagina))
        playsound(NOMBRE)

    else:
       rev = rev + 1


if(p == rev):
    print("["+ x.strftime("%X") +"]"+ "[Coolmod][Rtx 3090]:"+Fore.RED+"OUT OF STOCK")
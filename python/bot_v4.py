from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore,Back,Style
from colorama import init
from playsound import playsound
from os import system, name
from time import sleep
import winsound

init(autoreset=True)

import datetime


driver=webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe")
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

tabla = [
#PAGINA
["Coolmod","Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod",
 "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod",
  "Coolmod", "Coolmod", "Coolmod"],
#MARCA
[Fore.GREEN+"[Rtx 3060]",Fore.GREEN+"[Rtx 3060]", Fore.GREEN+"[Rtx 3060]", Fore.GREEN+"[Rtx 3060]", Fore.GREEN+"[Rtx 3060]",Fore.GREEN+"[Rtx 3060]", Fore.GREEN+"[Rtx 3060]", Fore.GREEN+"[Rtx 3060]",
Fore.GREEN+"[Rtx 3070]",Fore.GREEN+"[Rtx 3070]",Fore.GREEN+"[Rtx 3070]",Fore.GREEN+"[Rtx 3080]",Fore.GREEN+"[Rtx 3080]",Fore.GREEN+"[Rtx 3080]",Fore.GREEN+"[Rtx 3080]",
Fore.GREEN+"[Rtx 3080]",Fore.GREEN+"[Rtx 3080]",Fore.GREEN+"[Rtx 3080]",Fore.GREEN+"[Rtx 3080]",Fore.GREEN+"[Rtx 3080]",Fore.GREEN+"[Rtx 3080]",Fore.GREEN+"[Rtx 3090]",
Fore.GREEN+"[Rtx 3090]",Fore.GREEN+"[Rtx 3090]",Fore.GREEN+"[Rtx 3090]",Fore.GREEN+"[Rtx 3090]",Fore.GREEN+"[Rtx 3090]",Fore.GREEN+"[Rtx 3090]",Fore.GREEN+"[Rtx 3090]",
Fore.GREEN+"[Rtx 3090]",Fore.GREEN+"[Rtx 3090]",Fore.GREEN+"[Rtx 3090]",Fore.GREEN+"[Rtx 3090]"],
#MODELO
["MSI GeForce® RTX 3060 VENTUS 2X 12GB GDDR6"," MSI GeForce® RTX 3060 VENTUS 2X OC 12GB GDDR6"," Asus TUF Gaming GeForce® RTX 3060 12GB GDDR6",
" Zotac GeForce® RTX 3060 Twin Edge 12GB GDDR6"," PNY GeForce® RTX 3060 XLR8 Gaming REVEL EPIC-X RGB Single Fan 12GB GDDR6","MSI GeForce® RTX 3060 VENTUS 3X OC 12GB GDDR6",
"MSI GeForce® RTX 3060 GAMING X 12GB GDDR6","MSI GeForce® RTX 3060 GAMING X TRIO 12GB GDDR6"," MSI GeForce® RTX 3070 SUPRIM X 8GB GDDR6",
" PNY GeForce® RTX 3070 XLR8 Gaming EPIC-X RGB 8GB GDDR6"," Zotac GAMING GeForce® RTX 3070 Twin Edge 8GB GDDR6"," Zotac Gaming GeForce® RTX 3080 Trinity OC 10GB GDDR6X",
" MSI GeForce® RTX 3080 SUPRIM X 10GB GDDR6X"," EVGA GeForce® RTX 3080 FTW3 Gaming 10GB GDDR6X"," EVGA GeForce® RTX 3080 FTW3 Gaming 10GB GDDR6X",
" EVGA GeForce® RTX 3080 FTW3 Gaming 10GB GDDR6X"," EVGA GeForce® RTX 3080 XC3 Gaming 10GB GDDR6X"," EVGA GeForce® RTX 3080 XC3 Black Gaming 10GB GDDR6X",
" PNY GeForce® RTX 3080 XLR8 Gaming EPIC-X RGB 10GB GDDR6X"," PNY GeForce® RTX 3080 10GB XLR8 Gaming EPIC-X RGB 10GB GDDR6X"," MSI GeForce® RTX 3080 VENTUS 3X OC 10GB GDDR6X",
" Zotac GAMING GeForce® RTX 3080 Trinity 10GB GDDR6X"," KFA2 GeForce® RTX 3090 HOF 24GB GDDR6X"," Gigabyte AORUS GeForce® RTX 3090 Xtreme Waterforce WB 24GB GDDR6X",
" KFA2 GeForce® RTX 3090 HOF Premium 24GB GDDR6X"," KFA2 GeForce® RTX 3090 HOF Limited Edition 24GB GDDR6X"," EVGA GeForce® RTX 3090 XC3 Black Gaming 24GB GDDR6X",
" EVGA GeForce® RTX 3090 XC3 Gaming 24GB GDDR6X"," EVGA GeForce® RTX 3090 XC3 Ultra Gaming 24GB GDDR6X"," MSI GeForce® RTX 3090 SUPRIM X 24GB GDDR6X",
" PNY GeForce® RTX 3090 XLR8 Gaming EPIC-X RGB 24GB GDDR6X"," PNY GeForce® RTX 3090 XLR8 Gaming EPIC-X RGB 24GB GDDR6X"," MSI GeForce® RTX 3090 GAMING X TRIO 24GB GDDR6X",
" Zotac GAMING GeForce® RTX 3090 Trinity 24GB GDDR6X"],
#LINK
["https://www.coolmod.com/msi-geforce-rtx-3060-ventus-2x-12gb-gddr6-tarjeta-grafica-precio",
" https://www.coolmod.com/msi-geforce-rtx-3060-ventus-2x-oc-12gb-gddr6-tarjeta-grafica-precio",
" https://www.coolmod.com/asus-tuf-gaming-geforce-rtx-3060-12gb-gddr6-tarjeta-grafica-precio",
" https://www.coolmod.com/zotac-geforce-rtx-3060-twin-edge-12gb-gddr6-tarjeta-grafica-precio",
" https://www.coolmod.com/pny-geforce-rtx-3060-xlr8-gaming-revel-epic-x-rgb-single-fan-12gb-gddr6-tarjeta-grafica-precio",
" https://www.coolmod.com/msi-geforce-rtx-3060-ventus-3x-oc-12gb-gddr6-tarjeta-grafica-precio",
" https://www.coolmod.com/msi-geforce-rtx-3060-gaming-x-12gb-gddr6-tarjeta-grafica-precio",
" https://www.coolmod.com/msi-geforce-rtx-3060-gaming-x-trio-12gb-gddr6-tarjeta-grafica-precio",
" https://www.coolmod.com/msi-geforce-rtx-3070-suprim-x-8gb-gddr6-tarjeta-grafica-precio",
" https://www.coolmod.com/pny-geforce-rtx-3070-xlr8-gaming-epic-x-rgb-8gb-gddr6-tarjeta-grafica-precio",
" https://www.coolmod.com/zotac-gaming-geforce-rtx-3070-twin-edge-8gb-gddr6-tarjeta-grafica-precio",
" https://www.coolmod.com/zotac-gaming-geforce-rtx-3080-trinity-oc-10gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/msi-geforce-rtx-3080-suprim-x-10gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/evga-geforce-rtx-3080-ftw3-gaming-10gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/evga-geforce-rtx-3080-xc3-gaming-10gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/evga-geforce-rtx-3080-xc3-black-gaming-10gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/pny-geforce-rtx-3080-xlr8-gaming-epic-x-rgb-10gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/pny-geforce-rtx-3080-10gb-xlr8-gaming-epic-x-rgb-10gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/msi-geforce-rtx-3080-ventus-3x-oc-10gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/zotac-gaming-geforce-rtx-3080-trinity-10gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/kfa2-geforce-rtx-3090-hof-24gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/gigabyte-aorus-geforce-rtx-3090-xtreme-waterforce-wb-24gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/kfa2-geforce-rtx-3090-hof-premium-24gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/kfa2-geforce-rtx-3090-hof-limited-edition-24gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/evga-geforce-rtx-3090-xc3-black-gaming-24gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/evga-geforce-rtx-3090-xc3-gaming-24gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/evga-geforce-rtx-3090-xc3-ultra-gaming-24gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/msi-geforce-rtx-3090-suprim-x-24gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/pny-geforce-rtx-3090-xlr8-gaming-epic-x-rgb-24gb-gddr6x-tarjeta-grafica_76404-precio",
" https://www.coolmod.com/pny-geforce-rtx-3090-xlr8-gaming-epic-x-rgb-24gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/msi-geforce-rtx-3090-gaming-x-trio-24gb-gddr6x-tarjeta-grafica-precio",
" https://www.coolmod.com/zotac-gaming-geforce-rtx-3090-trinity-24gb-gddr6x-tarjeta-grafica-precio"]
]

p = 0
m = 0
import time
tamaño = len(tabla[1])
NOMBRE = "salida.mp3"
CLINC = "clin.mp3"
verga = 10
print("Empieza en: ")
for i in range(10):
    p = 10 - i
    print(p)
    time.sleep(1)
    clear()

playsound(CLINC,False)
clear()

while(True):
    for puntero in range(tamaño):
        pagina = tabla[0][puntero]
        gama = tabla[1][puntero]
        modelo = tabla[2][puntero]
        link = tabla[3][puntero]
        x = datetime.datetime.now()

        driver.get(link)
        el = driver.find_element_by_tag_name('body')
        str1 = el.text
        

        if(str1.find("Comprar")!=-1):
            
            print("["+x.strftime("%I")+":"+x.strftime("%M")+":"+x.strftime("%S")+" "+x.strftime("%p")+"] :: "+Fore.CYAN+"["+pagina+"]"+Style.RESET_ALL+gama+Style.RESET_ALL+"["+modelo+"]:"+Fore.GREEN +"SI HAY STOCK")
            playsound(NOMBRE, False)
        else:
            print("["+x.strftime("%I")+":"+x.strftime("%M")+":"+x.strftime("%S")+" "+x.strftime("%p")+"] :: "+Fore.CYAN+"["+pagina+"]"+Style.RESET_ALL+gama+Style.RESET_ALL+"["+modelo+"]:"+Fore.RED+"No hay stock")
    

driver.close()
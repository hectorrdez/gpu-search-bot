from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore,Back,Style
from colorama import init
from playsound import playsound
from os import system, name
from time import sleep
import winsound
import threading

init(autoreset=True)

import datetime

chromeOptions = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images':2}
chromeOptions.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe",chrome_options=chromeOptions,)
driver_f=webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe",chrome_options=chromeOptions,)
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

tabla = [
#PAgINA
["Coolmod","Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod"],
#MARCA
[Fore.GREEN+"[rtx 3060]"+Fore.WHITE,Fore.GREEN+"[rtx 3060]"+Fore.WHITE, Fore.GREEN+"[rtx 3060]"+Fore.WHITE, Fore.GREEN+"[rtx 3060]"+Fore.WHITE,Fore.GREEN+"[rtx 3060]"+Fore.WHITE,
Fore.GREEN+"[rtx 3060]"+Fore.WHITE, Fore.GREEN+"[rtx 3060]"+Fore.WHITE, Fore.GREEN+"[rtx 3060]"+Fore.WHITE,Fore.GREEN+"[rtx 3070]"+Fore.WHITE,Fore.GREEN+"[rtx 3070]"+Fore.WHITE,
Fore.GREEN+"[rtx 3070]"+Fore.WHITE,Fore.GREEN+"[rtx 3080]"+Fore.WHITE,Fore.GREEN+"[rtx 3080]"+Fore.WHITE,Fore.GREEN+"[rtx 3080]"+Fore.WHITE],
#MODELO
["msi rtx 3060 ventus 2x 12gb gddr6",
"msi rtx 3060 ventus 2x oc 12gb gddr6",
"asus tuf gaming rtx 3060 12gb gddr6",
"zotac rtx 3060 twin edge 12gb gddr6",
"pny rtx 3060 xlr8 gaming revel epic-x rgb Single fan 12gb gddr6",
"msi rtx 3060 ventus 3x oc 12gb gddr6",
"msi rtx 3060 gaming x 12gb gddr6",
"msi rtx 3060 gaming x trio 12gb gddr6",
" msi rtx 3070 suprim x 8gb gddr6",
" pny rtx 3070 xlr8 gaming epic-x rgb 8gb gddr6",
" zotac gaming rtx 3070 twin edge 8gb gddr6",
" zotac gaming rtx 3080 trinity oc 10gb gddr6x",
" msi rtx 3080 suprim x 10gb gddr6x",
" evga rtx 3080 ftw3 gaming 10gb gddr6x",
" evga rtx 3080 ftw3 gaming 10gb gddr6x"
],
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
" https://www.coolmod.com/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6x-tarjeta-grafica-precio"
]
]

tabla_3070 = [
["Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod", "Coolmod","Coolmod"],
[Fore.GREEN+"[rtx 3080]"+Fore.WHITE,Fore.GREEN+"[rtx 3080]"+Fore.WHITE,Fore.GREEN+"[rtx 3080]"+Fore.WHITE,Fore.GREEN+"[rtx 3080]"+Fore.WHITE,
Fore.GREEN+"[rtx 3080]"+Fore.WHITE,Fore.GREEN+"[rtx 3090]"+Fore.WHITE,Fore.GREEN+"[rtx 3090]"+Fore.WHITE,Fore.GREEN+"[rtx 3090]"+Fore.WHITE,Fore.GREEN+"[rtx 3090]"+Fore.WHITE,
Fore.GREEN+"[rtx 3090]"+Fore.WHITE,Fore.GREEN+"[rtx 3090]"+Fore.WHITE,Fore.GREEN+"[rtx 3090]"+Fore.WHITE,Fore.GREEN+"[rtx 3090]"+Fore.WHITE,Fore.GREEN+"[rtx 3090]"+Fore.WHITE,
Fore.GREEN+"[rtx 3090]"+Fore.WHITE,Fore.GREEN+"[rtx 3090]"+Fore.WHITE,Fore.GREEN+"[rtx 3090]"+Fore.WHITE],
["evga rtx 3080 xc3 gaming 10gb gddr6x",
"evga rtx 3080 xc3 black gaming 10gb gddr6x",
"pny rtx 3080 xlr8 gaming epic-x rgb 10gb gddr6x",
"pny rtx 3080 10gb xlr8 gaming epic-x rgb 10gb gddr6x",
"msi rtx 3080 ventus 3x oc 10gb gddr6x",
"zotac gaming rtx 3080 trinity 10gb gddr6x",
"kfa2 rtx 3090 hof 24gb gddr6x",
"gigabyte AORUS rtx 3090 xtreme waterforce WB 24gb gddr6x",
"kfa2 rtx 3090 hof premium 24gb gddr6x",
"kfa2 rtx 3090 hof limited edition 24gb gddr6x",
"evga rtx 3090 xc3 black gaming 24gb gddr6x",
"evga rtx 3090 xc3 gaming 24gb gddr6x",
"evga rtx 3090 xc3 ultra gaming 24gb gddr6x",
"msi rtx 3090 suprim x 24gb gddr6x",
"pny rtx 3090 xlr8 gaming epic-x rgb 24gb gddr6x",
"pny rtx 3090 xlr8 gaming epic-x rgb 24gb gddr6x",
"msi rtx 3090 gaming x trio 24gb gddr6x",
"zotac gaming rtx 3090 trinity 24gb gddr6x"],
[" https://www.coolmod.com/evga-geforce-rtx-3080-xc3-gaming-10gb-gddr6x-tarjeta-grafica-precio",
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
import time
print(len(tabla[0]))
print(len(tabla[1]))
print(len(tabla[2]))
print(len(tabla[3]))
time.sleep(10)
tamaño = len(tabla[1])
tamaño_3070 = len(tabla[1])
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

def stock_3060():
    while(True):
        for puntero in range(tamaño):
            pagina = tabla[0][puntero]
            gama = tabla[1][puntero]
            modelo = tabla[2][puntero]
            link = tabla[3][puntero]
            driver.get(link)
            x = datetime.datetime.now()
            
            el = driver.find_element_by_tag_name('body')
            str1 = el.text
            b = str1.find("Envío Inmediato")
            if(b!=-1):   
                print("["+x.strftime("%I")+":"+x.strftime("%M")+":"+x.strftime("%S")+" "+x.strftime("%p")+"] :: "+Fore.CYAN+"["+pagina+"]"+Style.RESET_ALL+gama+Style.RESET_ALL+"["+modelo+"]:"+Fore.GREEN +"SI HAY STOCK")
                playsound(NOMBRE, False)
            else:
                print("["+x.strftime("%I")+":"+x.strftime("%M")+":"+x.strftime("%S")+" "+x.strftime("%p")+"] :: "+Fore.CYAN+"["+pagina+"]"+Style.RESET_ALL+gama+Style.RESET_ALL+"["+modelo+"]:"+Fore.RED+"No hay stock")
    
def stock_3070():
    while(True):
        for puntero_3070 in range(tamaño_3070):
            pagina = tabla_3070[0][puntero_3070]
            gama = tabla_3070[1][puntero_3070]
            modelo = tabla_3070[2][puntero_3070]
            link = tabla_3070[3][puntero_3070]
            driver_f.get(link)
            x = datetime.datetime.now()
            
            el2 = driver_f.find_element_by_tag_name('body')
            str2 = el2.text
            b = str2.find("Envío Inmediato")
            if(b!=-1):   
                print("["+x.strftime("%I")+":"+x.strftime("%M")+":"+x.strftime("%S")+" "+x.strftime("%p")+"] :: "+Fore.CYAN+"["+pagina+"]"+Style.RESET_ALL+gama+Style.RESET_ALL+"["+modelo+"]:"+Fore.GREEN +"SI HAY STOCK")
                playsound(NOMBRE, False)
            else:
                print("["+x.strftime("%I")+":"+x.strftime("%M")+":"+x.strftime("%S")+" "+x.strftime("%p")+"] :: "+Fore.CYAN+"["+pagina+"]"+Style.RESET_ALL+gama+Style.RESET_ALL+"["+modelo+"]:"+Fore.RED+"No hay stock")


def stock_3060_pccomponentes():
    while(True):
        for puntero_3060_pccomponentes in range(tamaño_3060_pccomponentes):
            pagina = tabla_3060_pccomponentes[0][puntero_3060_pccomponentes]
            gama = tabla_3060_pccomponentes[1][puntero_3060_pccomponentes]
            modelo = tabla_3060_pccomponentes[2][puntero_3060_pccomponentes]
            link = tabla_3060_pccomponentes[3][puntero_3060_pccomponentes]
            driver_3.get(link)
            x = datetime.datetime.now()
            
            el3 = driver_3.find_element_by_tag_name('body')
            str3 = el3.text
            b = str3.find("Envío Inmediato")
            if(b!=-1):   
                print("["+x.strftime("%I")+":"+x.strftime("%M")+":"+x.strftime("%S")+" "+x.strftime("%p")+"] :: "+Fore.CYAN+"["+pagina+"]"+Style.RESET_ALL+gama+Style.RESET_ALL+"["+modelo+"]:"+Fore.GREEN +"SI HAY STOCK")
                playsound(NOMBRE, False)
            else:
                print("["+x.strftime("%I")+":"+x.strftime("%M")+":"+x.strftime("%S")+" "+x.strftime("%p")+"] :: "+Fore.CYAN+"["+pagina+"]"+Style.RESET_ALL+gama+Style.RESET_ALL+"["+modelo+"]:"+Fore.RED+"No hay stock")

t1 = threading.Thread(target=stock_3060)
t2 = threading.Thread(target=stock_3070)
t3 = threading.Thread(target=stock_3060_pccomponentes)
t1.start()
t2.start()
t3.start()        



        
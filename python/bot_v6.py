from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore,Back,Style
from colorama import init
from playsound import playsound
from os import system, name

import winsound
import threading
import datetime
import time

init(autoreset=True)
alert = "salida.mp3"
ini = "clin.mp3"

chromeOptions = webdriver.ChromeOptions()
prefs = {'profile.managd_default_content_settings.images':2,'javascript.enable'}
chromeOptions.add_experimental_option("prefs",prefs)
driver_3060=webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe",chrome_options=chromeOptions)
driver_3060ti=webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe",chrome_options=chromeOptions)
driver_3070=webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe",chrome_options=chromeOptions)
driver_3080=webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe",chrome_options=chromeOptions)
driver_3090=webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe",chrome_options=chromeOptions)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

tabla_3060 = [[],[],[],[]]
tabla_3060ti = [[],[],[],[]]
tabla_3070 = [[],[],[],[]]
tabla_3080 = [[],[],[],[]]
tabla_3090 = [[],[],[],[]]

tamaño_3060 = len(tabla_3060[3])
tamaño_3060ti = len(tabla_3060ti[3])
tamaño_3070 = len(tabla_3070[3])
tamaño_3080 = len(tabla_3080[3])
tamaño_3090 = len(tabla_3090[3])

def stock_3060():
    while(True):
        for p_3060 in range(tamaño_3060):
            pag_3060 = tabla_3060[0][p_3060]
            gama_3060 = tabla_3060[1][p_3060]
            modelo_3060 = tabla_3060[2][p_3060]
            link_3060 = tabla_3060[3][p_3060]

            driver_3060.get(link_3060)
            h = datetime.datetime.now()
            el_3060 = driver_3060.find_element_by_tag_name('body')
            str_3060 = el_3060.text

            if(str_3060.find("Envío Inmediato") != -1):
                print("["+h.strftime("%I")+":"+h.strftime("%M")+":"+h.strftime("%S")+" "+h.strftime("%p")+"] : : "+pag_3060+gama_3060+modelo_3060+": "+Fore.GREEN+"SI HAY STOCK")
                playsound(alert, False)
            else:
                print("["+h.strftime("%I")+":"+h.strftime("%M")+":"+h.strftime("%S")+" "+h.strftime("%p")+"] : : "+pag_3060+gama_3060+modelo_3060+": "+Fore.RED+"NO HAY STOCK")

def stock_3060ti():
    while(True):
        for p_3060ti in range(tamaño_3060ti):
            pag_3060ti = tabla_3060ti[0][p_3060ti]
            gama_3060ti = tabla_3060ti[1][p_3060ti]
            modelo_3060ti = tabla_3060ti[2][p_3060ti]
            link_3060ti = tabla_3060ti[3][p_3060ti]

            driver_3060ti.get(link_3060ti)
            h = datetime.datetime.now()
            el_3060ti = driver_3060ti.find_element_by_tag_name('body')
            str_3060ti = el_3060ti.text

            if(str_3060ti.find("Envío Inmediato") != -1):
                print("["+h.strftime("%I")+":"+h.strftime("%M")+":"+h.strftime("%S")+" "+h.strftime("%p")+"] : : "+pag_3060ti+gama_3060ti+modelo_3060ti+": "+Fore.GREEN+"SI HAY STOCK")
                playsound(alert, False)
            else:
                print("["+h.strftime("%I")+":"+h.strftime("%M")+":"+h.strftime("%S")+" "+h.strftime("%p")+"] : : "+pag_3060ti+gama_3060ti+modelo_3060ti+": "+Fore.RED+"NO HAY STOCK")

def stock_3070():
    while(True):
        for p_3070 in range(tamaño_3070):
            pag_3070 = tabla_3070[0][p_3070]
            gama_3070 = tabla_3070[1][p_3070]
            modelo_3070 = tabla_3070[2][p_3070]
            link_3070 = tabla_3070[3][p_3070]

            driver_3070.get(link_3070)
            h = datetime.datetime.now()
            el_3070 = driver_3070.find_element_by_tag_name('body')
            str_3070 = el_3070.text

            if(str_3070.find("Envío Inmediato") != -1):
                print("["+h.strftime("%I")+":"+h.strftime("%M")+":"+h.strftime("%S")+" "+h.strftime("%p")+"] : : "+pag_3070+gama_3070+modelo_3070+": "+Fore.GREEN+"SI HAY STOCK")
                playsound(alert, False)
            else:
                print("["+h.strftime("%I")+":"+h.strftime("%M")+":"+h.strftime("%S")+" "+h.strftime("%p")+"] : : "+pag_3070+gama_3070+modelo_3070+": "+Fore.RED+"NO HAY STOCK")
    

def stock_3080():
    while(True):
        for p_3080 in range(tamaño_3080):
            pag_3080 = tabla_3080[0][p_3080]
            gama_3080 = tabla_3080[1][p_3080]
            modelo_3080 = tabla_3080[2][p_3080]
            link_3080 = tabla_3080[3][p_3080]

            driver_3080.get(link_3080)
            h = datetime.datetime.now()
            el_3080 = driver_3080.find_element_by_tag_name('body')
            str_3080 = el_3080.text

            if(str_3080.find("Envío Inmediato") != -1):
                print("["+h.strftime("%I")+":"+h.strftime("%M")+":"+h.strftime("%S")+" "+h.strftime("%p")+"] : : "+pag_3080+gama_3080+modelo_3080+": "+Fore.GREEN+"SI HAY STOCK")
                playsound(alert, False)
            else:
                print("["+h.strftime("%I")+":"+h.strftime("%M")+":"+h.strftime("%S")+" "+h.strftime("%p")+"] : : "+pag_3080+gama_3080+modelo_3080+": "+Fore.RED+"NO HAY STOCK")
    

def stock_3090():
    while(True):
        for p_3090 in range(tamaño_3090):
            pag_3090 = tabla_3090[0][p_3090]
            gama_3090 = tabla_3090[1][p_3090]
            modelo_3090 = tabla_3090[2][p_3090]
            link_3090 = tabla_3090[3][p_3090]

            driver_3090.get(link_3090)
            h = datetime.datetime.now()
            el_3090 = driver_3090.find_element_by_tag_name('body')
            str_3090 = el_3090.text

            if(str_3090.find("Envío Inmediato") != -1):
                print("["+h.strftime("%I")+":"+h.strftime("%M")+":"+h.strftime("%S")+" "+h.strftime("%p")+"] : : "+pag_3090+gama_3090+modelo_3090+": "+Fore.GREEN+"SI HAY STOCK")
                playsound(alert, False)
            else:
                print("["+h.strftime("%I")+":"+h.strftime("%M")+":"+h.strftime("%S")+" "+h.strftime("%p")+"] : : "+pag_3090+gama_3090+modelo_3090+": "+Fore.RED+"NO HAY STOCK")
    

t3060 = threading.Thread(target=stock_3060)
t3060ti = threading.Thread(target=stock_3060ti)
t3070 = threading.Thread(target=stock_3070)
t3080 = threading.Thread(target=stock_3080)
t3090 = threading.Thread(target=stock_3090)

t3060.start()
t3060ti.start()
t3070.start()
t3080.start()
t3090.start()
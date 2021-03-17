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
rev = 0
p = 0

paginas_coolmod_nombre_gpu_3060 = ["https://www.coolmod.com/msi-geforce-rtx-3060-gaming-x-12gb-gddr6-tarjeta-grafica-precio"]
paginas_coolmod_nombre_gpu_3060 = ["MSI GeForce® RTX 3060 GAMING X 12GB GDDR6"]
for pag in paginas_coolmod_nombre_gpu_3060:
    driver.get(pag)
    el = driver.find_element_by_tag_name('body')
    str1 = el.text
    p = p + 1

    if(str1.find("Comprar")!=-1):
        pagina = paginas_coolmod_nombre_gpu_3060[p-1]
        print("["+ x.strftime("%X") +"]"+"[Coolmod][Rtx 3060]:"+ bcolors.OKGREEN+''.join(pagina))
        playsound(NOMBRE)

    else:
       rev = rev + 1


if(p == rev):
    print("["+ x.strftime("%X") +"]"+ "[Coolmod][Rtx 3060]:"+Fore.RED+"OUT OF STOCK")
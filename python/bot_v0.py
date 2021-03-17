from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe")
el = driver.find_element_by_tag_name('body')
str1 = el.text

i = 0

driver.get("https://www.pccomponentes.com/powercolor-red-devil-radeon-rx-5700-xt-8-gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1

driver.get("https://www.pccomponentes.com/gigabyte-amd-radeon-rx-5700-xt-gaming-oc-8gb-gddr6-reacondicionado")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1


driver.get("https://www.pccomponentes.com/sapphire-amd-radeon-rx-5700-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1


driver.get("https://www.pccomponentes.com/gigabyte-aorus-radeon-rx-5700-xt-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1


driver.get("https://www.pccomponentes.com/gigabyte-amd-radeon-rx-5700-xt-gaming-oc-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1


driver.get("https://www.pccomponentes.com/asus-amd-radeon-rx-5700-dual-evo-oc-edition-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1


driver.get("https://www.pccomponentes.com/asus-radeon-rx-5700-xt-rog-strix-gaming-oc-edition-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1

driver.get("https://www.pccomponentes.com/gigabyte-amd-radeon-rx-5700-xt-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1


driver.get("https://www.pccomponentes.com/sapphire-nitro-radeon-rx-5700-xt-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1

driver.get("https://www.pccomponentes.com/gigabyte-amd-radeon-rx-5700-gaming-oc-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1

driver.get("https://www.pccomponentes.com/msi-amd-radeon-rx-5700-xt-mech-oc-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1


driver.get("https://www.pccomponentes.com/powercolor-radeon-rx-5700-xt-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1

driver.get("https://www.pccomponentes.com/xfx-amd-radeon-rx-5700-xt-triple-dissipation-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i + 1

driver.get("https://www.pccomponentes.com/xfx-radeon-rx-5700-xt-thicc-iii-ultra-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i+1

driver.get("https://www.pccomponentes.com/gigabyte-amd-radeon-rx-5700-8gb-gddr6")
if(str1.find("Comprar") != -1):
    print("[pccomponentes][rx5700xt]: HAY STOCK")
else:
    i=i+1

#driver.get("")
#if(str1.find("Comprar") == -1):
#    print("[pccomponentes][rx5700xt]: HAY STOCK")
#else:
#    i + 1
if(i == 15):
    print("[pccomponentes][rx5700xt]: OUT OF STOCK")
else:
    print("[pccomponentes][rx5700xt]: HAY STOCK!")


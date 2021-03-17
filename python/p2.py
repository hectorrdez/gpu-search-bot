from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe")
for i in range(10): 
    driver.get("https://www.amazon.es/ASUS-TUF-RTX3070-O8G-GAMING-Tarjeta-DisplayPort-rodamiento/dp/B08LLG9KQT/ref=sr_1_fkmr0_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=gpu+3060+ti&qid=1615652329&sr=8-1-fkmr0")
    el = driver.find_element_by_tag_name('body')
    str1 = el.text
    if(str1.find("Comprar ya") != -1):
        print("[amazon][asustuf3060ti]: si hay stock")
        
    else:
        print("[amazon][asustuf3060ti]: OUT OF STOCK")

    driver.get("https://www.pccomponentes.com/amd-ryzen-5-3600-36ghz-box")
    el = driver.find_element_by_tag_name('body')
    str1 = el.text
    if(str1.find("Comprar") != -1):
        print("[pccomponentes][ryzen3600]: encontrado")
        
    else:
        print("[pccomponentes][ryzen3600]: ha fallado")
        
    
driver.close()

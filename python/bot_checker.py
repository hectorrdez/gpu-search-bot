from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from twilio.rest import Client
#client = Client("your_twillio_keys", "your_twillio_id")
driver = webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe")
driver.get("https://www.pccomponentes.com/amd-ryzen-5-3600-36ghz-box")


el = driver.find_element_by_tag_name('body')
str1=el.text 
if(str1.find("Currently unavailable.")!=-1):
    print("its still not available my guy")
else:
    print("disponible")


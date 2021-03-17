from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe")
driver.get("http://google.es")
driver.close()
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
t = 2
driver.get("https://demoqa.com/links")
driver.maximize_window()
time.sleep(t)

#obteniendo todos los links de la página
links = driver.find_elements(By.TAG_NAME, "a")

print("el numero de links que hay en la página es: ", len(links))

for num in links:
    print(num.text)

driver.find_element(By.LINK_TEXT, "Home").click()
time.sleep(t)

driver.close()


'''
try:
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Descubre más')]")))
    buscar = driver.find_element(By.XPATH, "//span[contains(.,'Descubre más')]")
    ir = driver.execute_script("arguments[0].scrollIntoView();", buscar)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")
'''
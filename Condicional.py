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

driver.get("https://demoqa.com/")
driver.maximize_window()
t = 1

titulo = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
time.sleep(1)
print(titulo.is_displayed())
btn1 = driver.find_element(By.XPATH, "//div[@class='card-body'][contains(.,'Elements')]")
ir = driver.execute_script("arguments[0].scrollIntoView();", btn1)
time.sleep(2)

if(titulo.is_displayed()==True):
    print("existe la imagen")
    btn1.click()
    time.sleep(t)
else:
    print("no existe la imagen")

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
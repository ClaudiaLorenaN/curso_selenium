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

driver.get("https://demoqa.com/alerts")
driver.maximize_window()
t = 2

driver.find_element(By.XPATH, "//button[@id='alertButton']").click()
time.sleep(3)

driver.switch_to.alert.accept()  #ejecutar el boton aceptar
driver.switch_to.alert.dismiss() #ejecutar el boton cerrar

'''
send = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
driver.execute_script("arguments[0].scrollIntoView();", send)
send.click()
'''
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
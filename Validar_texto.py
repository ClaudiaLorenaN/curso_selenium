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

driver.get("https://testingqarvn.com.es/campos-requeridos/")
driver.maximize_window()
t = 2

btn = driver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
btn.click()
time.sleep(t)

name_val = driver.find_element(By.XPATH, "//div[@class='wsf-invalid-feedback'][contains(.,'Minimum character count: 4')]")
name = name_val.text
#print("El valor es: " + name)

if(name == "Minimum character count: 4"):
    cn=driver.find_element(By.XPATH, "//input[@placeholder='Nombre:']")
    cn.send_keys("Claudia")
    print("nombre correcto")
else:
    print("falta el nombre")

em_val = driver.find_element(By.XPATH, "//div[@class='wsf-invalid-feedback'][contains(.,'Please provide a valid email.')]")
em = em_val.text
#print("El valor es: " + name)

if(em == "Please provide a valid email."):
    em=driver.find_element(By.XPATH, "//input[contains(@placeholder,'Email')]")
    em.send_keys("Claudia@gmail.com")
    print("email correcto")
else:
    print("falta el email")

print(btn.is_enabled())
if(btn.is_enabled()==False):
    print("faltan campos por diligenciar")
else:
    print("listo todo OK")

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
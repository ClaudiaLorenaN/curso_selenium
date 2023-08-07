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

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
t = 2

#driver.execute_script("window.scrollTo(0,500)")

try:
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))
    buscar = driver.find_element(By.XPATH, "//input[contains(@id,'fileinput')]")
    buscar.send_keys("C://Users//Claudia//PycharmProjects//curso_selenium//imagenes//demo1.jpg")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[@id='itsanimage']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")


time.sleep(t)
driver.close()
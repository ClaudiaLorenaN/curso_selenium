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

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
t = 2

driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Claudia" + Keys.TAB + "Naranjo" + Keys.TAB + "Claudia.2210.cn@gmail.com")
#driver.find_element(By.XPATH, "//input[contains(@id,'lastName')]").send_keys("Naranjo" + Keys.TAB)
#driver.find_element(By.XPATH, "//input[contains(@id,'userEmail')]").send_keys("claudia.2210.cn@gmail.com")


check = driver.find_element(By.XPATH, "//div[@class='col-md-9 col-sm-12'][contains(.,'MaleFemaleOther')]")
driver.execute_script("arguments[0].scrollIntoView();", check)

driver.find_element(By.XPATH, "//label[contains(.,'Female')]").click()
driver.find_element(By.XPATH, "//input[@id='userNumber']").send_keys("123456")
driver.find_element(By.XPATH, "//div[@class='col-md-3 col-sm-12'][contains(.,'Hobbies')]")
driver.find_element(By.XPATH, "//label[contains(.,'Music')]").click()
driver.find_element(By.XPATH, "//input[@id='uploadPicture']").send_keys("C://Users//Claudia//PycharmProjects//curso_selenium//imagenes//demo1.jpg")

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
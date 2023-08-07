import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

t = 3

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

nom = driver.find_element(By.XPATH, "//input[@id='userName']")
nom.send_keys("Claudia")
time.sleep(t)

driver.find_element(By.XPATH, "//input[contains(@id,'userEmail')]").send_keys("claudia.22t0.cn@gmail.com")
time.sleep(t)

driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys("direcciont")
time.sleep(t)

driver.find_element(By.XPATH, "//textarea[contains(@id,'permanentAddress')]").send_keys("Hola soy Claudia")
time.sleep(t)

driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)

driver.find_element(By.XPATH, "//button[contains(@id,'submit')]").click()
time.sleep(2)

driver.close()



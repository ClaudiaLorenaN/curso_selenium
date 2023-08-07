import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#driver = webdriver.Firefox()



driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
#driver.implicitly_wait(10)
t = 0.5

driver.execute_script("window.scrollTo(0,500)")

wait = WebDriverWait(driver, 10)
btn1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//label[contains(@class,'custom-control-label')])[4]")))
btn1.click()
time.sleep(t)

btn2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//label[contains(@class,'custom-control-label')])[5]")))
btn2.click()
time.sleep(t)

btn3 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//label[contains(@class,'custom-control-label')])[6]")))
btn3.click()
time.sleep(t)


driver.close()



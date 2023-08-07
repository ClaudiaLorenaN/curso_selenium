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

nom = driver.find_element(By.XPATH, "//Input[@type='text' and @id='userName']")
nom.send_keys("Claudia")
nom.send_keys(Keys.TAB + "claudia.22t0.cn@gmail.com" + Keys.TAB + "Direcciont" + Keys.TAB + "Soy Claudia" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)

driver.find_element(By.XPATH, "(//span[contains(@class,'text')])[2]").click()
time.sleep(2)

driver.close()



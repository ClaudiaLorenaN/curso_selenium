import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
driver.implicitly_wait(10)
t = 0.5

#driver.execute_script("window.scrollTo(0,600)")

wait = WebDriverWait(driver, 10)
#city = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class=' css-1wa3eu0-placeholder'][contains(.,'Select State')]")))

productSelect = Select(driver.find_element(By.XPATH, "//*[@id='cars']"))

productSelect.select_by_index(1)
time.sleep(t)

productSelect.select_by_index(3)
time.sleep(t)

driver.close()

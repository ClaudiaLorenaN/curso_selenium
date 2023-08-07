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

driver.get("https://www.selenium.dev/documentation/webdriver/elements/finders/")
driver.maximize_window()
time.sleep(t)

driver.get("https://www.geeksforgeeks.org/send_keys-element-method-selenium-python/")
driver.maximize_window()
time.sleep(t)

#driver.back()
driver.execute_script("window.history.go(-1)")
time.sleep(t)

#driver.back()
driver.execute_script("window.history.go(-1)")
time.sleep(t)

#driver.forward()
driver.execute_script("window.history.go(2)")
time.sleep(t)

driver.close()



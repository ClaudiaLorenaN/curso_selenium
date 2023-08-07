import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#driver = webdriver.Firefox()



driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
driver.implicitly_wait(10)
t = 3

driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Catalog')]").click()
driver.find_element(By.XPATH, "(//p[contains(.,'Products')])[1]").click()

#driver.execute_script("window.scrollTo(0,600)")

wait = WebDriverWait(driver, 10)
#city = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class=' css-1wa3eu0-placeholder'][contains(.,'Select State')]")))

productSelect = driver.find_element(By.XPATH, "//select[contains(@id,'SearchCategoryId')]")
ps = Select(productSelect)

ps.select_by_visible_text("Computers")
time.sleep(t)

ps.select_by_index(3)
time.sleep(t)

ps.select_by_value("5")
time.sleep(t)


driver.close()

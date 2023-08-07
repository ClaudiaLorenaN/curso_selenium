import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#driver = webdriver.Firefox()



driver.get("https://www.matrimonio.com.co/articulos/poemas-de-amor-para-mi-novia--c6325")
driver.maximize_window()
#driver.implicitly_wait(10)
t = 0.5

wait = WebDriverWait(driver, 10)
btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='onetrust-accept-btn-handler']")))
btn.click()

#driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()

driver.find_element(By.XPATH, "//a[@href='https://www.matrimonio.com.co/users-login.php'][contains(.,'Accede')]").click()

driver.find_element(By.XPATH, "//input[contains(@id,'Mail')]").send_keys("claudia.2210.cn@gmail.com" + Keys.TAB)

time.sleep(t)
driver.close()



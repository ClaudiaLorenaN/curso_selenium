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

driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
t = 2

driver.execute_script("window.scrollTo(0,500)")

try:
    colorSelect = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='oldSelectMenu']")))

    color = Select(colorSelect)

    color.select_by_visible_text("Black")
    time.sleep(t)

    color.select_by_index(3)
    time.sleep(t)

    color.select_by_value("6")
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

driver.execute_script("window.scrollTo(0,500)")

productSelect = Select(driver.find_element(By.XPATH, "//*[@id='cars']"))

productSelect.select_by_index(1)
time.sleep(t)

productSelect.select_by_index(3)
time.sleep(t)

driver.close()
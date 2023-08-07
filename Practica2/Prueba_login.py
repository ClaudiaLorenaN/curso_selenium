import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PruebaLogin(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        bt = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("Claudia")
        clave.send_keys("admin123")
        bt.click()


        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error =error.text
        #print(error)

        if error == "Epic sadface: Username and password do not match any user in this service":
            print("el error de datos es correcto")
            print("prueba un OK")
        time.sleep(3)

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        bt = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        clave.send_keys("admin123")
        bt.click()

        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        print(error)

        if error == "Epic sadface: Username is required":
            print("Falta el nombre")
            print("prueba dos OK")
        time.sleep(3)

    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        bt = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("Claudia")
        clave.send_keys("")
        bt.click()

        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        print(error)

        if error == "Epic sadface: Password is required":
            print("Falta el password")
            print("prueba tres OK")
        time.sleep(3)


    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        bt = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        clave.send_keys("")
        bt.click()

        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        print(error)

        if error == "Epic sadface: Username is required":
            print("Falta el password")
            print("prueba cuatro pendiente")
        time.sleep(3)

    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        bt = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("standard_user")
        clave.send_keys("secret_sauce")
        bt.click()

        element = driver.find_element(By.XPATH, "//div[@class='app_logo'][contains(.,'Swag Labs')]")
        element = element.is_enabled()

        print("El elemento es: " +str(element))

        if element == True:
            print("todo OK")
            print("prueba 5 ok")
        time.sleep(3)



    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
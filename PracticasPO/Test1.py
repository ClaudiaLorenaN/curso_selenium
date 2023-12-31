import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Funciones.Funciones import Funciones_Globales

t = 2
class base_test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()



    def test1(self):
        driver = self.driver
        f=Funciones_Globales(driver)
        f.saludos()
        f.saludo2()

    def test2(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.navegar("https://www.saucedemo.com/", t)
        #f.Texto_xpath_validar("//input[contains(@id,'user-name')]","Claudia", t)
        #f.Texto_xpath_validar("//input[contains(@id,'password')]", "admin123", t)
        f.Texto_ID_validar("user-name", "Claudia", t)
        f.Texto_ID_validar("password", "admin123", t)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
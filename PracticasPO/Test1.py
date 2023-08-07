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
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        f.tiempo(5)




    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Funciones_Globales():

    def __init__(self, driver):
        self.driver = driver

    def saludos(self):
        print("Bienvenidos a page object model")

    def saludo2(self):
        print("Saludo 2")

    def tiempo(self, tie):
        t = time.sleep(tie)
        return t
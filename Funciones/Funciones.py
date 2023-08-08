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

    def navegar(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        t = time.sleep(Tiempo)
        return t

    def Texto_xpath(self, xpath, texto, Tiempo):
        val = self.driver.find_element(By.XPATH, xpath)
        val.clear()
        val.send_keys(texto)
        t = time.sleep(Tiempo)
        return t

    def Texto_xpath_validar(self, xpath, texto, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.clear()
            val.send_keys(texto)
            t = time.sleep(Tiempo)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + xpath)

    def Texto_ID_validar(self, ID, texto, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, ID)
            val.clear()
            val.send_keys(texto)
            t = time.sleep(Tiempo)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + ID)




    def Texto_ID(self, ID, texto, Tiempo):
        val = self.driver.find_element(By.ID, ID)
        val.clear()
        val.send_keys(texto)
        t = time.sleep(Tiempo)
        return t
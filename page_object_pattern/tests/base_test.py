
from selenium import webdriver
import unittest
from page_object_pattern.pages.home_page import HomePage
from time import sleep
class BaseTest(unittest.TestCase): #klasa bazowa każdego testu
    def setUp(self): #warunki wstepne kazdego testu
        self.driver = webdriver.Chrome() #Korzystanie z przeglądarki homedriver
        #self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://www.supermemo.com/pl")
        self.driver.implicitly_wait(5)
        self.home_page = HomePage(self.driver)
        self.home_page.click_cookis_accept()

    def tearDown(self):
        self.driver.quit()
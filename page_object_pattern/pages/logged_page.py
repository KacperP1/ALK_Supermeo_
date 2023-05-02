#
#
# from page_object_pattern.pages.base_page import BasePage
# from page_object_pattern.locators_all.locators import Logged
# from page_object_pattern.locators_all.locators import PaymentDetails
# from faker import Faker
# fake_data = Faker()
# from faker.providers.credit_card import Provider as CreditCardProvider
# fake_card = CreditCardProvider()
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
#
# class CorrectLogged(BasePage):
#
#     def clicl_get_acces_orange_buttom(self):
#         cgaob = self.driver.find_element(*Logged.get_acces_orange_buttom)
#         cgaob.click()
#
#
#
#     def input_your_fullname(self):
#
#         #wait = WebDriverWait.until(EC.visibility_of_element_located(*PaymentDetails.full_name))
#         iyf = self.driver.find_element(*PaymentDetails.full_name)
#         iyf.send_keys(fake_data.name())
#
#
#     def input_card_number(self):
#         icn = self.driver.find_element(*PaymentDetails.card_number)
#         icn.send_keys(fake_card.credit_card_number())
#
#     def input_MM(self):
#         imm = self.driver.find_element(*PaymentDetails.MM)
#         imm.send_keys(fake_card.credit_card_expire())
#
#


import faker.providers.credit_card

from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.locators_all.locators import Logged
from page_object_pattern.locators_all.locators import PaymentDetails
from faker import Faker
from faker.providers.credit_card import Provider as CreditCardProvider
fake_card = CreditCardProvider(Faker())



class CorrectLogged(BasePage):

    def clicl_get_acces_orange_buttom(self):
        cgaob = self.driver.find_element(*Logged.get_acces_orange_buttom)
        cgaob.click()

    def input_your_fullname(self):
        iyf = self.driver.find_element(*PaymentDetails.full_name)
        iyf.send_keys(Faker().name())

    def input_card_number(self):
        icn = self.driver.find_element(*PaymentDetails.card_number)
        icn.send_keys(fake_card.credit_card_number())

    def input_MM(self):
        imm = self.driver.find_element(*PaymentDetails.MM)
        imm.send_keys(fake_card.credit_card_expire())

    def input_YYYY(self):
        iyyyy = self.driver.find_element(*PaymentDetails.YYYY_year)
        iyyyy.send_keys("2024")

    def credit_card_security_code(self):
        ccsc = self.driver.find_element(*PaymentDetails.CVC_CVV)
        ccsc.send_keys(fake_card.credit_card_security_code())

    def cardholder_name(self):
        noo = self.driver.find_element(*PaymentDetails.Cardholder_name)
        noo.send_keys(Faker().name())

    def start_your_free_month(self):
        syfm = self.driver.find_element(*PaymentDetails.free_month)
        syfm.click()

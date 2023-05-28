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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.locators_all.locators import Logged
from page_object_pattern.locators_all.locators import PaymentDetails
from faker import Faker
fake = Faker()
fake_number = fake.random_number(digits=1000)
from faker.providers.credit_card import Provider as CreditCardProvider
fake_card = CreditCardProvider(Faker())
from time import sleep



class CorrectLogged(BasePage):

    def clicl_get_acces_orange_buttom(self):
        sleep(4)
        cgaob = self.driver.find_element(*Logged.get_acces_orange_buttom)
        cgaob.click()
    def unlock_click(self):
        uc = self.driver.find_element(*Logged.unlock)
        uc.click()
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

    def catalog_of_courses_click(self):
        cocc = self.driver.find_element(*Logged.catalog_buttom)
        cocc.click()

    def click_course_language(self):
        ccl = self.driver.find_element(*Logged.course_language)
        ccl.click()

    def select_chinese(self):
        sc = self.driver.find_element(*Logged.chinese)
        sc.click()

    def apply_bottom(self):
        ab = self.driver.find_element(*Logged.apply)
        ab.click()

    def courses_chniese(self):
        ch = self.driver.find_elements(*Logged.courses)
        print("Jest dostępnych "+ str(len(ch)) +" kursuw w języku Chińskim")

    def more_bottom(self):
        self.driver.implicitly_wait(10)
        mb = self.driver.find_element(*Logged.more)
        mb.click()

    def access_code(self):
        ac = self.driver.find_element(*Logged.redeem_your_access_code)
        sleep(2)
        ac.click()

    def enter_your_acces_code(self):
        eyac = self.driver.find_element(*Logged.enter_your_access_code)
        eyac.send_keys(fake_number)


    def confirm_bottom(self):
        cb = self.driver.find_element(*Logged.confirm_code)
        cb.click()

    def get_incorrect_code_text(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element(Logged.incorrect_code, 'Błędny kod'))
        return self.driver.find_element(*Logged.incorrect_code).text



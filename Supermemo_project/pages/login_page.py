from Supermemo_project.pages.base_page import BasePage
from Supermemo_project.locators_all.locators import LogIn
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Supermemo_project.pages import logged_page
from selenium.common.exceptions import NoSuchElementException, TimeoutException
valid_email = "testerakademialk@gmail.com"
password = "testeralk"
from faker import Faker
fake_data = Faker()

class LogginYourself(BasePage):


    def confirm_the_country_u_r_logging_in_from(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LogIn.country_u_r_li_input)))
        self.driver.find_element(*LogIn.input_to_sent_key).send_keys("Tur")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LogIn.countries))).click()


    def click_next_on_login_page(self):
        sleep(4)
        cnolp = self.driver.find_element(*LogIn.next_button)
        cnolp.click()

    def email_address_input(self):
        eai = self.driver.find_element(*LogIn.email_address)
        eai.send_keys(valid_email)

    def fake_email(self):
        fe = self.driver.find_element(*LogIn.email_address)
        fe.send_keys(fake_data.email())

    def password_input(self):
        pi = self.driver.find_element(*LogIn.password)
        pi.send_keys(password)

    def fake_password(self):
        fp = self.driver.find_element(*LogIn.password)
        fp.send_keys(fake_data.password(6))

    def loggin_button_click(self):
        lbc = self.driver.find_element(*LogIn.loggin_buttom)
        lbc.click()
        return logged_page

    def enter_your_email_address_message(self):
        try:
            eyeam = self.driver.find_element(*LogIn.message_enter_your_email)
            return eyeam.text
        except NoSuchElementException:
            return "Element not found"


    def enter_your_password_message(self):
        eypm = self.driver.find_element(*LogIn.message_enter_your_password)
        return eypm.text

    def incorrect_data_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LogIn.incorrect_data))
        idm = self.driver.find_element(*LogIn.incorrect_data)
        return idm.text



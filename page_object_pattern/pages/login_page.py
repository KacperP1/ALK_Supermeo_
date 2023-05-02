from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.locators_all.locators import LogIn
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object_pattern.pages import logged_page
valid_email = "testerakademialk@gmail.com"
password = "testeralk"

class LogginYourself(BasePage):

    def waiting(self):
        wait = WebDriverWait.until(self.driver, 10).until()
        # wait.click()
        # pass
    def confirm_the_country_u_r_logging_in_from(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LogIn.country_u_r_li_input)))
        self.driver.find_element(*LogIn.input_to_sent_key).send_keys("Tur")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((LogIn.countries))).click()


        # driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + 200;', scrollable_element)
    def click_next_on_login_page(self):
        #cnolp = self.waiting(EC._element_if_visible(LogIn.next_button))
        sleep(4)
        cnolp = self.driver.find_element(*LogIn.next_button)
        cnolp.click()

    def email_address_input(self):
        #eai = self.waiting(EC.visibility_of(*LogIn.email_address))
        eai = self.driver.find_element(*LogIn.email_address)
        eai.send_keys(valid_email)

    def password_input(self):
        pi = self.driver.find_element(*LogIn.password)
        pi.send_keys(password)

    def loggin_button_click(self):
        lbc = self.driver.find_element(*LogIn.loggin_buttom)
        lbc.click()
        return logged_page





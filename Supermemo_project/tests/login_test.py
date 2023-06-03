# gmial:
# testerakademialk@gmail.com
# hasło do gmail:
# testeralk
#supermemo hasło:
# testeralk

from Supermemo_project.tests.base_test import BaseTest
from time import sleep

class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = self.home_page.click_login_ypurself()

    def test_login_yourself(self):
        #self.login_page.confirm_the_country_u_r_logging_in_from()
        self.login_page.click_next_on_login_page()
        self.login_page.email_address_input()
        self.login_page.password_input()
        self.login_page.loggin_button_click()

    def test_trail_to_login_without_an_email_address(self):
        self.driver.implicitly_wait(5)
        #self.login_page.confirm_the_country_u_r_logging_in_from()
        self.login_page.click_next_on_login_page()
        self.login_page.password_input()
        self.login_page.loggin_button_click()
        self.assertEqual(self.login_page.enter_your_email_address_message(), "Wpisz swój adres e-mail")

    def test_trial_to_login_without_a_passwird(self):
        self.driver.implicitly_wait(5)
        #self.login_page.confirm_the_country_u_r_logging_in_from()
        self.login_page.click_next_on_login_page()
        self.login_page.email_address_input()
        self.login_page.loggin_button_click()
        self.assertEqual(self.login_page.enter_your_password_message(), "Wpisz swoje hasło")

    def test_trial_to_login_with_incorrect_data(self):
        self.driver.implicitly_wait(5)
        #self.login_page.confirm_the_country_u_r_logging_in_from()
        self.login_page.click_next_on_login_page()
        self.login_page.fake_email()
        self.login_page.fake_password()
        self.login_page.loggin_button_click()
        self.assertEqual(self.login_page.incorrect_data_message(), "Niepoprawny e-mail lub hasło, albo konto nie zostało potwierdzone.")











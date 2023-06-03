# gmial:
# testerakademialk@gmail.com
# hasło do gmail:
# testeralk
#supermemo hasło:
# testeralk

from page_object_pattern.tests.base_test import BaseTest
from page_object_pattern.pages.login_page import LogIn
from time import sleep




class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = self.home_page.click_login_ypurself()

    def test_login_yourself(self):

        self.login_page.confirm_the_country_u_r_logging_in_from()
        self.login_page.click_next_on_login_page()
        self.login_page.email_address_input()
        self.login_page.password_input()
        self.login_page.loggin_button_click()






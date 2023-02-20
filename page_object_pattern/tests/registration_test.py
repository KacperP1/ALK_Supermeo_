
from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.locators_all.locators import SuperMemoLocators
from page_object_pattern.tests.base_test import BaseTest
from time import sleep

class RegistrationTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.home_page.click_register_yourself()
        self.registration_page = self.home_page.click_register_yourself()

    def test_login_with_6(self):
        self.registration_page.firstname_input()
        self.registration_page.next_click()
        self.registration_page.your_email_address()
        self.registration_page.create_password()
        self.registration_page.sing_up_button_registration()
        self.registration_page.terms_of_use_and_privacy_policy()
        self.registration_page.send_button()

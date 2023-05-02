import page_object_pattern.pages
from page_object_pattern.pages import logged_page
from page_object_pattern.tests.login_test import LoginTest
from time import sleep

class PaymentTest(LoginTest):

    def setUp(self):
        super().setUp()
        self.payment_page = page_object_pattern.pages.logged_page.CorrectLogged(self.driver)



    def test_payment(self):

        self.test_login_yourself()
        self.payment_page.clicl_get_acces_orange_buttom()
        self.payment_page.input_your_fullname()
        self.payment_page.input_card_number()
        self.payment_page.input_MM()
        self.payment_page.input_YYYY()
        self.payment_page.credit_card_security_code()
        self.payment_page.cardholder_name()
        self.payment_page.start_your_free_month()
        self.driver.save_screenshot("/Users/kacper/PycharmProjects/projekt_na_zaliczenie/page_object_pattern/screenshots/scr1.png")
        sleep(20)








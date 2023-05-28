import page_object_pattern.pages
from page_object_pattern.pages import logged_page
from page_object_pattern.tests.login_test import LoginTest
from time import sleep

class PaymentTest(LoginTest):

    def setUp(self):
        super().setUp()
        # self.payment_page = page_object_pattern.pages.logged_page.CorrectLogged(self.driver)
        self.logged_page = page_object_pattern.pages.logged_page.CorrectLogged(self.driver)



    def test_payment(self):
        self.driver.implicitly_wait(10)
        self.test_login_yourself()
        sleep(2)
        self.logged_page.clicl_get_acces_orange_buttom()
        sleep(2)
        self.logged_page.unlock_click()
        self.logged_page.input_your_fullname()
        self.logged_page.input_card_number()
        self.logged_page.input_MM()
        self.logged_page.input_YYYY()
        self.logged_page.credit_card_security_code()
        self.logged_page.cardholder_name()
        self.logged_page.start_your_free_month()
        sleep(2)
        self.driver.save_screenshot("/Users/kacper/PycharmProjects/projekt_na_zaliczenie/page_object_pattern/screenshots/scr1.png")
        sleep(2)


    def test_amount_of_available_courses(self):
        self.test_login_yourself()
        self.logged_page.catalog_of_courses_click()
        self.logged_page.click_course_language()
        self.logged_page.select_chinese()
        self.logged_page.apply_bottom()
        self.logged_page.courses_chniese()

    def test_assert_access_code(self):
        self.test_login_yourself()
        self.logged_page.more_bottom()
        self.logged_page.access_code()
        self.logged_page.enter_your_acces_code()
        self.logged_page.confirm_bottom()
        self.assertEqual(self.logged_page.get_incorrect_code_text(), "Błędny kod")





"""
<button _ngcontent-sns-c40="" class="filter-btn ng-star-inserted">
<span _ngcontent-sns-c40="">Język kursu</span>

//button[@class="filter-btn ng-star-inserted"]//span[text()="Język kursu"]
"""





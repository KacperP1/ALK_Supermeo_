import Supermemo_project.pages
from Supermemo_project.pages import logged_page
from Supermemo_project.tests.login_test import LoginTest
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentTest(LoginTest):

    def setUp(self):
        super().setUp()
        self.logged_page = Supermemo_project.pages.logged_page.CorrectLogged(self.driver)


    def test_payment(self):
        self.driver.implicitly_wait(10)
        self.test_login_yourself()
        self.logged_page.clicl_get_acces_orange_buttom()
        self.logged_page.unlock_click()
        self.logged_page.input_your_fullname()
        self.logged_page.input_card_number()
        self.logged_page.input_MM()
        self.logged_page.input_YYYY()
        self.logged_page.credit_card_security_code()
        self.logged_page.cardholder_name()
        self.logged_page.start_your_free_month()
        now = str(datetime.now())
        self.driver.save_screenshot(f"/Users/kacper/PycharmProjects/ALK_SuperMemo/Supermemo_project/screenshots/scr1{now}.png")
        self.logged_page.the_payment_has_not_been_completed()




    def test_amount_of_available_courses(self):
        self.driver.implicitly_wait(10)
        self.test_login_yourself()
        self.logged_page.catalog_of_courses_click()
        self.logged_page.click_course_language()
        self.logged_page.select_chinese()
        self.logged_page.apply_bottom()
        self.logged_page.courses_chniese()


    def test_assert_access_code(self):
        self.driver.implicitly_wait(5)
        self.test_login_yourself()
        self.logged_page.more_bottom()
        self.logged_page.access_code()
        self.logged_page.enter_your_acces_code()
        self.logged_page.confirm_bottom()
        self.assertEqual(self.logged_page.get_incorrect_code_text(), "Błędny kod")


    def test_find_hello_polski_course(self):
        self.driver.implicitly_wait(5)
        self.test_login_yourself()
        self.logged_page.catalog_of_courses_click()
        self.logged_page.click_icon_magnifying()
        self.logged_page.search_course_input()
        if self.logged_page.hello_polski_course().is_displayed():
            pass


    def test_log_out(self):
        self.driver.implicitly_wait(5)
        self.test_login_yourself()
        self.logged_page.log_out()
        expected_url = "https://learn.supermemo.com/pl/authorization/v2/entry?returnUrl=%2Fpl%2Fapp"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        assert self.driver.current_url == expected_url
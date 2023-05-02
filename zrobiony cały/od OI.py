from faker import Faker
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SuperMemoRegistration:
    def __init__(self, driver):
        self.driver = driver
        self.fake_data = Faker('pl_PL')
        self.url = "https://www.supermemo.com/"
        self.cookie_alert_button = (By.ID, "cn-accept-cookie")
        self.register_button = (By.XPATH, "//a[@href='https://learn.supermemo.com/pl/authorization/v2/register?returnUrl=https://www.supermemo.com' and @class='register-button c-ml-4 c-mr-4 c-mr-xl-0 crunch-button crunch-button__full-background crunch-button__full-background--primary-color fz-14 d-none d-md-inline-block' and @target='_self']")
        self.first_name_input = (By.XPATH, "//*[@id='firstname']")
        self.next_button = (By.XPATH, "//button[@class='action-btn' and @type='submit']")
        self.email_input = (By.XPATH, "//input[@formcontrolname='email']")
        self.password_input = (By.XPATH, "//input[@type='password' and @name='password']")
        self.create_account_button = (By.XPATH, "//button[@class='action-btn' and @type='submit']")
        self.accept_statute_checkbox = (By.XPATH, "//input[@type='checkbox']")
        self.send_button = (By.XPATH, "//button[@class='action-btn']")
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def accept_cookies(self):
        self.wait.until(EC.element_to_be_clickable(self.cookie_alert_button)).click()

    def click_register_button(self):
        self.wait.until(EC.element_to_be_clickable(self.register_button)).click()

    def enter_first_name(self):
        first_name = self.fake_data.first_name()
        self.wait.until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)
        return first_name

    def click_next_button(self):
        self.wait.until(EC.element_to_be_clickable(self.next_button)).click()

    def enter_email(self):
        email = self.fake_data.email()
        self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)
        return email

    def enter_password(self):
        password = self.fake_data.password(6)
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        return password

    def click_create_account_button(self):
        self.wait.until(EC.element_to_be_clickable(self.create_account_button)).click()

    def accept_statute(self):
        self.wait.until(EC.element_to_be_clickable(self.accept_statute_checkbox)).click()

    def click_send_button(self):
        self.wait.until(EC.element_to_be_clickable(self.send_button)).click()



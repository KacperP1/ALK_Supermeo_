
from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.locators_all.locators import SuperMemoLocators
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
fake_data = Faker('pl_PL')
from time import sleep
class RegistrationPage(BasePage): #kalsa strony rejestracji, gdzie wykonujemy kroki

    def firstname_input(self): #wpisanie imienia przez fkera
        fni = self.driver.find_element(*SuperMemoLocators.first_name)
        fni.send_keys(fake_data.first_name())

    def next_click(self): #klikamy przycisk "dalej"
        nc = self.driver.find_element(*SuperMemoLocators.button_next)
        nc.click

    def your_email_address(self): #wpisanie adresu emial
        yma = self.driver.find_element(*SuperMemoLocators.email)
        yma.send_keys(fake_data.email())

    def create_password(self): #podawanie hasła
        cp = self.driver.find_element(*SuperMemoLocators.password)
        cp.send_keys(fake_data.password(6))

    def sing_up_button_registration(self): #kliknięcie przycisku na stronie rejestracji "zarejestrój"
        subr = self.driver.find_element(*SuperMemoLocators.sign_up_button)
        subr.click

    def terms_of_use_and_privacy_policy(self): #zatwierdzenie statusu
        touapp = self.driver.find_element(*SuperMemoLocators.accept_statute)
        touapp.click

    def send_button(self): #kliknięcie przycisku wyślij
        sb = self.driver.find_element(*SuperMemoLocators.send)
        sb.click
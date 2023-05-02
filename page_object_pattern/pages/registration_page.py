
from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.locators_all.locators import SuperMemoLocators
from page_object_pattern.locators_all.locators import SelectLanguage
# from page_object_pattern.tests.registration_test import RegistrationTest
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
fake_data = Faker('pl_PL')
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class RegistrationPage(BasePage): #kalsa strony rejestracji, gdzie wykonujemy kroki


    def firstname_input(self):
        #wait = WebDriverWait(self.driver, 10)
        #element = wait.until(EC.visibility_of_element_located(SuperMemoLocators.first_name))
        #element.send_keys(fake_data.first_name())
        #ten działa
        '''
        button_next = self.driver.find_element(*SuperMemoLocators.button_next)
        button_next_enabled = EC.element_to_be_clickable(SuperMemoLocators.button_next)
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value(SuperMemoLocators.first_name, fake_data.first_name()))
        WebDriverWait(self.driver, 10).until(button_next_enabled)
        button_next.click()
        '''

    #def firstname_input(self): #wpisanie imienia przez fkera
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(EC.element_to_be_clickable(SuperMemoLocators.first_name))
        #wait.until(EC.visibility_of_element_located(*SuperMemoLocators.first_name.send_keys(fake_data.first_name())))

        sleep(4)
        fni = self.driver.find_element(*SuperMemoLocators.first_name)
        fni.send_keys(fake_data.first_name())


    #def scroll(self):
        # self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        # self.driver.execute_script("window.scrollBy(0, 1000)","")



    def next_click(self): #klikamy przycisk "dalej"
        wait = WebDriverWait(self.driver, 10)
        nc = wait.until(EC.presence_of_element_located(SuperMemoLocators.button_next))
        #nc = wait.until(EC.visibility_of_element_located(SuperMemoLocators.button_next)) and wait.until(EC.element_to_be_clickable(SuperMemoLocators.button_next))
        #nc = wait.until(EC.visibility_of_element_located(SuperMemoLocators.button_next))
        #nc = wait.until(EC.element_to_be_clickable(SuperMemoLocators.button_next))
        #nc = self.driver.find_element(*SuperMemoLocators.button_next)
        nc.click()





    def your_email_address(self): #wpisanie adresu emial
        wait = WebDriverWait(self.driver, 10)
        yma = wait.until(EC.visibility_of_element_located(SuperMemoLocators.email))
        #yma = self.driver.find_element(*SuperMemoLocators.email)
        yma.send_keys(fake_data.email())

    def create_password(self): #podawanie hasła
        cp = self.driver.find_element(*SuperMemoLocators.password)
        cp.send_keys(fake_data.password(6))

    def create_password_less_then_6(self):
        cplt6 = self.driver.find_element(*SuperMemoLocators.password)
        cplt6.send_keys(fake_data.password(5))

    def create_password_more_than_64(self):
        cpmt250 = self.driver.find_element(*SuperMemoLocators.password)
        cpmt250.send_keys(fake_data.password(65))
    def get_error_password_message_5(self):
        #wait = WebDriverWait(self.driver, 10)
        #wb = wait.until(EC.text_to_be_present_in_element_value(SuperMemoLocators.error_paassword_message_5))
        wb = self.driver.find_element(*SuperMemoLocators.error_paassword_message_5)
        sleep(3)
        text = wb.text
        return text



    def sing_up_button_registration(self): #kliknięcie przycisku na stronie rejestracji "zarejestrój"
        subr = self.driver.find_element(*SuperMemoLocators.sign_up_button)
        subr.click()

    def terms_of_use_and_privacy_policy(self): #zatwierdzenie statusu
        touapp = self.driver.find_element(*SuperMemoLocators.accept_statute)
        touapp.click()

    def send_button(self): #kliknięcie przycisku wyślij
        sb = self.driver.find_element(*SuperMemoLocators.send)
        sb.click()


    def choose_english(self):
        ce = self.driver.find_element(*SelectLanguage.english)
        ce.click()

    def choose_spanish(self):
        cs = self.driver.find_element(*SelectLanguage.spanish)
        cs.click()
    def choose_german(self):
        cg = self.driver.find_element(*SelectLanguage.german)
        cg.click()
    def choose_russian(self):
        cr = self.driver.find_element(*SelectLanguage.russian)
        cr.click()
    def choose_frenc(self):
        cf = self.driver.find_element(*SelectLanguage.french)
        cf.click()
    def choose_chinese(self):
        cc = self.driver.find_element(*SelectLanguage.chinese)
        cc.click()
    def choose_japanese(self):
        cj = self.driver.find_element(*SelectLanguage.japanese)
        cj.click()
    def choose_dutch(self):
        cd = self.driver.find_element(*SelectLanguage.dutch)
        self.driver.execute_script("arguments[0].scrollIntoView();", cd)
        cd.click()

    def choose_italian(self):
        ci = self.driver.find_element(*SelectLanguage.italian)
        self.driver.execute_script("arguments[0].scrollIntoView();", ci)
        ci.click()

    def choose_portugese(self):
        cp = self.driver.find_element(*SelectLanguage.portuguese)
        self.driver.execute_script("arguments[0].scrollIntoView();", cp)
        cp.click()

    def choose_swedish(self):
        cs = self.driver.find_element(*SelectLanguage.swedish)
        self.driver.execute_script("arguments[0].scrollIntoView();", cs)
        cs.click()

    def choose_danish(self):
        cd = self.driver.find_element(*SelectLanguage.danish)
        self.driver.execute_script("arguments[0].scrollIntoView();", cd)
        cd.click()

    def choose_norwegian(self):
        cn = self.driver.find_element(*SelectLanguage.norwegian)
        self.driver.execute_script("arguments[0].scrollIntoView();", cn)
        cn.click()

    def choose_czech(self):
        cc = self.driver.find_element(*SelectLanguage.czech)
        self.driver.execute_script("arguments[0].scrollIntoView();", cc)
        cc.click()

    def choose_finnish(self):
        cf = self.driver.find_element(*SelectLanguage.finnish)
        self.driver.execute_script("arguments[0].scrollIntoView();", cf)
        cf.click()

    def choose_arabic(self):
        ca = self.driver.find_element(*SelectLanguage.arabic)
        self.driver.execute_script("arguments[0].scrollIntoView();", ca)
        ca.click()

    def choose_hungarian(self):
        ch = self.driver.find_element(*SelectLanguage.hungarian)
        self.driver.execute_script("arguments[0].scrollIntoView();", ch)
        ch.click()



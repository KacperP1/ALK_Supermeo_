
from page_object_pattern.tests.base_test import BaseTest
from page_object_pattern.locators_all.locators import CourseAccess
from time import sleep
from page_object_pattern.pages.registration_page import RegistrationPage
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




class RegistrationTest(BaseTest):

    def setUp(self):
        super().setUp()
        #self.home_page.click_register_yourself()
        self.registration_page = self.home_page.click_register_yourself()

    def test_register_with_6(self):
        self.driver.implicitly_wait(5)
        self.registration_page.firstname_input()
        self.registration_page.next_click()
        self.registration_page.your_email_address()
        self.registration_page.create_password()
        self.registration_page.sing_up_button_registration()
        self.registration_page.terms_of_use_and_privacy_policy()
        self.registration_page.send_button()



    def test_register_5(self):
        #self.driver.implicitly_wait(10)
        self.registration_page.firstname_input()
        self.registration_page.next_click()
        self.registration_page.your_email_address()
        self.registration_page.create_password_less_then_6()
        self.registration_page.sing_up_button_registration()
        self.assertEqual(self.registration_page.get_error_password_message_5(), "Hasło musi mieć więcej niż 6 znaków")
        #self.assertEqual("Hasło musi mieć więcej niż 6 znaków", self.registration_page.get_error_password_message_5())


    def test_register_65(self):
        #self.driver.implicitly_wait(10)
        self.registration_page.firstname_input()
        self.registration_page.next_click()
        self.registration_page.your_email_address()
        self.registration_page.create_password_more_than_64()
        self.registration_page.sing_up_button_registration()
        #sleep(5)




#class AccesToTheFreeCourse(RegistrationTest):

    # def test_learn_engish(self):
    #     self.test_register_with_6()
    #     self.registration_page.choose_english()
    #     english_course_element = self.driver.find_element(*CourseAccess.english_course)
    #     if english_course_element.is_displayed():
    #         pass
            #print("Masz dostęp do darmowego kursu")
        #else:
            #print("Nie masz dostępu do darmowego kursu")




    # def test_learn_spanish(self):
    #     self.test_register_with_6()
    #     self.registration_page.choose_spanish()

    # def test_wybranie_losowego_języka(self):
    #     self.driver.implicitly_wait(10)
    #     self.test_register_with_6()
    #     registration_page = RegistrationPage(self.driver)  # utworzenie instancji RegistrationPage
    #     wybór = [registration_page.choose_english, registration_page.choose_spanish, registration_page.choose_german]
    #     losowy_wybór = random.choice(wybór)
    #     #sleep(2)
    #     losowy_wybór()
    #     # sleep(4)
    #     if losowy_wybór == registration_page.choose_english():
    #          english_course_element = self.driver.find_element(*CourseAccess.english_course)
    #          if english_course_element.is_displayed():
    #              print("Masz dostęp do nauki języka angielskiego")
    #          else:
    #              print("Nie")
    #     elif losowy_wybór == registration_page.choose_spanish():
    #          spanish_course_element = self.driver.find_element(*CourseAccess.spanish_course)
    #          if spanish_course_element.is_displayed():
    #              print("Masz dostęp do nauki języka hiszpańskiego")
    #     elif losowy_wybór == registration_page.choose_german():
    #         german_course_element = self.driver.find_element(*CourseAccess.german_course)
    #         if german_course_element.is_displayed():
    #             print("Niemiecki")
        # elif losowy_wybór == registration_page.choose_italian():
        #     italia_course_element = self.driver.find_element(*CourseAccess.italian_course)
        #     if italia_course_element.is_displayed():
        #         print("Masz dostęp do nauki języka włoskiego")

    def test_wybranie_losowego_języka(self):
        #self.driver.implicitly_wait(10)
        self.test_register_with_6()
        registration_page = RegistrationPage(self.driver)  # utworzenie instancji RegistrationPage
        wybór = [registration_page.choose_english, registration_page.choose_spanish, registration_page.choose_german,
                 registration_page.choose_russian, registration_page.choose_frenc, registration_page.choose_chinese,
                 registration_page.choose_japanese, registration_page.choose_dutch, registration_page.choose_italian,
                 registration_page.choose_portugese, registration_page.choose_swedish, registration_page.choose_danish,
                 registration_page.choose_norwegian, registration_page.choose_czech, registration_page.choose_finnish,
                 registration_page.choose_arabic, registration_page.choose_hungarian]
        #wybór = [registration_page.choose_arabic]
        losowy_wybór = random.choice(wybór)
        losowy_wybór()  # wywołanie wylosowanej metody
        if losowy_wybór == registration_page.choose_english:  # porównaj wywołaną metodę z oryginalnymi metodami
            english_course_element = self.driver.find_element(*CourseAccess.english_course)
            if english_course_element.is_displayed():
                print("Masz dostęp do nauki języka angielskiego")
            else:
                print("Nie")
        elif losowy_wybór == registration_page.choose_spanish:
            spanish_course_element = self.driver.find_element(*CourseAccess.spanish_course)
            if spanish_course_element.is_displayed():
                print("Masz dostęp do nauki języka hiszpańskiego")
            else:
                print("Nie")
        elif losowy_wybór == registration_page.choose_german:
            german_course_element = self.driver.find_element(*CourseAccess.german_course)
            if german_course_element.is_displayed():
                print("Niemiecki")
        elif losowy_wybór == registration_page.choose_russian:
            russian_course_element = self.driver.find_element(*CourseAccess.russian_course)
            if russian_course_element.is_displayed():
                print("Russian")
        elif losowy_wybór == registration_page.choose_frenc:
            french_course_element = self.driver.find_element(*CourseAccess.french_course)
            if french_course_element.is_displayed():
                print("Francuski")
        elif losowy_wybór == registration_page.choose_chinese:
            chinese_course_element = self.driver.find_element(*CourseAccess.chinese_course)
            if chinese_course_element.is_displayed():
                print("Chiński")
        elif losowy_wybór == registration_page.choose_japanese:
            japanese_course_element = self.driver.find_element(*CourseAccess.japanese_course)
            if japanese_course_element.is_displayed():
                print("Japoński")
        elif losowy_wybór == registration_page.choose_dutch:
            dutch_course_element = self.driver.find_element(*CourseAccess.dutch_course)
            if dutch_course_element.is_displayed():
                print("Holenderski")
        elif losowy_wybór == registration_page.choose_italian:
            italian_course_element = self.driver.find_element(*CourseAccess.italian_course)
            if italian_course_element.is_displayed():
                print("wloski")
        elif losowy_wybór == registration_page.choose_portugese:
            portugese_course_element = self.driver.find_element(*CourseAccess.portuguese_course)
            if portugese_course_element.is_displayed():
                print("portugalski")
        elif losowy_wybór == registration_page.choose_swedish:
            swedish_course_element = self.driver.find_element(*CourseAccess.swedish_course)
            if swedish_course_element.is_displayed():
                print("szwedzki")
        elif losowy_wybór == registration_page.choose_danish:
            danish_course_element = self.driver.find_element(*CourseAccess.danish_course)
            if danish_course_element.is_displayed():
                print("duński")
        elif losowy_wybór == registration_page.choose_norwegian:
            norwegian_course_element = self.driver.find_element(*CourseAccess.norwegian_course)
            if norwegian_course_element.is_displayed():
                print("norweski")
        elif losowy_wybór == registration_page.choose_czech:
            czech_course_element = self.driver.find_element(*CourseAccess.czech_course)
            if czech_course_element.is_displayed():
                print("czeski")
        elif losowy_wybór == registration_page.choose_finnish:
            finnish_course_element = self.driver.find_element(*CourseAccess.finnish_course)
            if finnish_course_element.is_displayed():
                print("fiński")
        elif losowy_wybór == registration_page.choose_arabic:
            arabic_course_element = self.driver.find_element(*CourseAccess.arabic_course)
            if arabic_course_element.is_displayed():
                print("arabski")
        elif losowy_wybór == registration_page.choose_hungarian:
            hungarian_course_element = self.driver.find_element(*CourseAccess.hungarian_course)
            if hungarian_course_element.is_displayed:
                print("wegierski")
        else:
            print("błąd!!!")











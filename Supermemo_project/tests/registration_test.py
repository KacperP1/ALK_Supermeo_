
import unittest
from Supermemo_project.tests.base_test import BaseTest
from Supermemo_project.locators_all.locators import CourseAccess
from Supermemo_project.pages.registration_page import RegistrationPage
import random



class RegistrationTest(BaseTest):

    def setUp(self):
        super().setUp()
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
        self.driver.implicitly_wait(5)
        self.registration_page.firstname_input()
        self.registration_page.next_click()
        self.registration_page.your_email_address()
        self.registration_page.create_password_less_then_6()
        self.registration_page.sing_up_button_registration()
        self.assertEqual(self.registration_page.get_error_password_message_5(), "Hasło musi mieć więcej niż 6 znaków")



    def test_register_65(self):
        self.driver.implicitly_wait(5)
        self.registration_page.firstname_input()
        self.registration_page.next_click()
        self.registration_page.your_email_address()
        self.registration_page.create_password_more_than_64()
        self.registration_page.sing_up_button_registration()
        self.assertEqual(self.registration_page.get_error_password_message_65(), "Hasło nie może mieć więcej niż 64 znaki")

    @unittest.SkipTest
    def test_wybranie_losowego_języka(self):
        self.driver.implicitly_wait(10)
        self.test_register_with_6()
        registration_page = RegistrationPage(self.driver)
        wybór = [registration_page.choose_english, registration_page.choose_spanish, registration_page.choose_german,
                 registration_page.choose_frenc, registration_page.choose_chinese,
                 registration_page.choose_japanese, registration_page.choose_dutch, registration_page.choose_italian,
                 registration_page.choose_portugese, registration_page.choose_swedish, registration_page.choose_danish,
                 registration_page.choose_norwegian, registration_page.choose_czech, registration_page.choose_finnish,
                 registration_page.choose_arabic, registration_page.choose_hungarian]
        losowy_wybór = random.choice(wybór)
        losowy_wybór()
        if losowy_wybór == registration_page.choose_english:
            english_course_element = self.driver.find_element(*CourseAccess.english_course)
            if english_course_element.is_displayed():
                print("Masz dostęp do nauki języka angielskiego")
            else:
                print("Nie masz dostępu do nauki języka angielskiego")
        elif losowy_wybór == registration_page.choose_spanish:
            spanish_course_element = self.driver.find_element(*CourseAccess.spanish_course)
            if spanish_course_element.is_displayed():
                print("Masz dostęp do nauki języka hiszpańskiego")
            else:
                print("Nie masz dostęp do nauki języka hiszpańskiego ")
        elif losowy_wybór == registration_page.choose_german:
            german_course_element = self.driver.find_element(*CourseAccess.german_course)
            if german_course_element.is_displayed():
                print("Masz dostęp do nauki języka niemieckiego")
            else:
                print("Nie masz dośtepu do nauki języka niemieckiego")
        elif losowy_wybór == registration_page.choose_russian:
            russian_course_element = self.driver.find_element(*CourseAccess.russian_course)
            if russian_course_element.is_displayed():
                print("Masz dostęp do nauki języka rosyjskiego")
            else:
                print("Nie masz dostepu do nauki języka rosyjskiego")
        elif losowy_wybór == registration_page.choose_frenc:
            french_course_element = self.driver.find_element(*CourseAccess.french_course)
            if french_course_element.is_displayed():
                print("Masz dostęp do nauki języka francuskiego")
            else:
                print("Nie masz dostępu do nauki języka francuskiego")
        elif losowy_wybór == registration_page.choose_chinese:
            chinese_course_element = self.driver.find_element(*CourseAccess.chinese_course)
            if chinese_course_element.is_displayed():
                print("Masz dostęp do nauki języka chińskiego")
            else:
                print("Nie masz dostępu do nauki języka chińskiego")
        elif losowy_wybór == registration_page.choose_japanese:
            japanese_course_element = self.driver.find_element(*CourseAccess.japanese_course)
            if japanese_course_element.is_displayed():
                print("Masz dostęp do nauki języka japońskiego")
            else:
                print("Nie masz dostępu do nauki języka japońskiego")
        elif losowy_wybór == registration_page.choose_dutch:
            dutch_course_element = self.driver.find_element(*CourseAccess.dutch_course)
            if dutch_course_element.is_displayed():
                print("Masz dostęp do nauki języka holenderskiego")
            else:
                print("Nie masz dostępu do nauki języka holenderskiego")
        elif losowy_wybór == registration_page.choose_italian:
            italian_course_element = self.driver.find_element(*CourseAccess.italian_course)
            if italian_course_element.is_displayed():
                print("Masz dostęp do nauki języka włoskiego")
            else:
                print("Nie masz dostepu do nauki języka włoskiego")
        elif losowy_wybór == registration_page.choose_portugese:
            portugese_course_element = self.driver.find_element(*CourseAccess.portuguese_course)
            if portugese_course_element.is_displayed():
                print("Masz dostęp do nauki języka portugalskiego")
            else:
                print("Nie masz dostępu do nauki języka portugalskiego")
        elif losowy_wybór == registration_page.choose_swedish:
            swedish_course_element = self.driver.find_element(*CourseAccess.swedish_course)
            if swedish_course_element.is_displayed():
                print("Masz dostęp do nauki języka szwedzkiego")
            else:
                print("Nie masz dostępu do nauki języka szwedzkiego")
        elif losowy_wybór == registration_page.choose_danish:
            danish_course_element = self.driver.find_element(*CourseAccess.danish_course)
            if danish_course_element.is_displayed():
                print("Masz dostęp do nauki języka duńskiego")
            else:
                print("Nie masz dostępu do nauki języka duńskiego")
        elif losowy_wybór == registration_page.choose_norwegian:
            norwegian_course_element = self.driver.find_element(*CourseAccess.norwegian_course)
            if norwegian_course_element.is_displayed():
                print("Masz dostęp do nauki języka norweskiego")
            else:
                print("Nie masz dostępu do nauki języka norweskiego")
        elif losowy_wybór == registration_page.choose_czech:
            czech_course_element = self.driver.find_element(*CourseAccess.czech_course)
            if czech_course_element.is_displayed():
                print("Masz dostęp do nauki języka czeskiego")
            else:
                print("Nie masz dostęp do nauki języka czeskiego")
        elif losowy_wybór == registration_page.choose_finnish:
            finnish_course_element = self.driver.find_element(*CourseAccess.finnish_course)
            if finnish_course_element.is_displayed():
                print("Masz dostęp do nauki języka czeskiego fińskiegp")
            else:
                print("Nie masz dostepu do nauki języka fińskiego")
        elif losowy_wybór == registration_page.choose_arabic:
            arabic_course_element = self.driver.find_element(*CourseAccess.arabic_course)
            if arabic_course_element.is_displayed():
                print("Masz dostęp do nauki arabskiego")
            else:
                print("Nie masz dostępu do nauki arabskiego")
        elif losowy_wybór == registration_page.choose_hungarian:
            hungarian_course_element = self.driver.find_element(*CourseAccess.hungarian_course)
            if hungarian_course_element.is_displayed:
                print("Masz dostęp do nauki języka węgierskiego")
            else:
                print("Nie masz dostępu do nauki języka węgierskiego")
        else:
            print("błąd!!!")












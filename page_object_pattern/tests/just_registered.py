"""
from page_object_pattern.pages.registration_page import SelectLanguageToLearn
from time import sleep


class AccesToTheFreeCourse(SelectLanguageToLearn):
    def test_english_course_acces(self):
        self.test_register_with_6()
        self.choos_english()
        sleep(4)
"""
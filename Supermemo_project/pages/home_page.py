from Supermemo_project.pages.base_page import BasePage
from Supermemo_project.pages.registration_page import RegistrationPage
from Supermemo_project.locators_all.locators import SuperMemoLocators
from Supermemo_project.pages.login_page import LogginYourself


class HomePage(BasePage):
    def click_register_yourself(self):
        rs = self.driver.find_element(*SuperMemoLocators.register_yourself)
        rs.click()
        return RegistrationPage(self.driver)

    def click_login_ypurself(self):
        ly = self.driver.find_element(*SuperMemoLocators.login_yourself)
        ly.click()
        return LogginYourself(self.driver)


    def click_cookis_accept(self):
        ca = self.driver.find_element(*SuperMemoLocators.cookies_alert)
        ca.click()



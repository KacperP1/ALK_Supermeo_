from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.pages.registration_page import RegistrationPage
from page_object_pattern.locators_all.locators import SuperMemoLocators
from page_object_pattern.pages.login_page import LogginYourself


class HomePage(BasePage): #klasa strony główniej, na której znajdują ssię odnośniki do dalszych czynnosci
    def click_register_yourself(self): #kliknięcie na stronie głownej przycisku "zarejestrój się", który przenosi nas do strony rejestrowania
        rs = self.driver.find_element(*SuperMemoLocators.register_yourself)
        rs.click() #klikanie na przycisk "Zarejestruj sie" na stronie gównej.
        return RegistrationPage(self.driver)

    def click_login_ypurself(self): #kliknięcie na stronie głowniej przycisku zaloguj sie
        ly = self.driver.find_element(*SuperMemoLocators.login_yourself)
        ly.click() ##klikanie na przycisk "Zaloguj sie" na stronie gównej.
        return LogginYourself(self.driver)


    def click_cookis_accept(self): #znajdz i akceptuj pliki cookis
        #wait = WebDriverWait(self.driver, 5, 0,5)
        #wait.until(EC.element_to_be_clickable(SuperMemoLocators.cookies_alert)).click
        #self.driver.implicitly_wait(10)
        ca = self.driver.find_element(*SuperMemoLocators.cookies_alert)
        ca.click()



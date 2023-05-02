from selenium.webdriver.common.alert import Alert
class BasePage(): #klasa bazowa, z której będą korzystały wszystkie strony
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()
        self.alert = Alert(self.driver)
        #self.wait = WebDriverWait(self.driver) - do sprawdzenia


    def _verify_page(self):
        return

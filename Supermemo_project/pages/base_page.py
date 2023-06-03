from selenium.webdriver.common.alert import Alert
class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()
        self.alert = Alert(self.driver)


    def _verify_page(self):
        return

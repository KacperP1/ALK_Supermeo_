from selenium.webdriver.common.by import By

class SuperMemoLocators:
        cookies_alert = (By.XPATH, '//*[@id="cn-accept-cookie"]') #lokalizator plików cookies
        login_yourself = (By.XPATH, "//a[@class='login-button c-mr-4 c-mr-md-0 crunch-button crunch-button__full-background crunch-button__full-background--white-color border-1 border-primary fz-14 d-inline-block']") #przycisk zalogój na głównej stronie
        register_yourself = (By.XPATH, '//a[@href="https://learn.supermemo.com/pl/authorization/v2/register?returnUrl=https://www.supermemo.com" and @class="register-button c-ml-4 c-mr-4 c-mr-xl-0 crunch-button crunch-button__full-background crunch-button__full-background--primary-color fz-14 d-none d-md-inline-block" and @target="_self"]') #przycisk zarejestrój się na główniej stronie
        first_name = (By.XPATH, '//*[@id="firstname"]') #podaj swoje imię
        button_next = (By.XPATH, '//button[@class="action-btn" and @type="submit"]') #przycisk dalej na stronie rejestracji
        email = (By.XPATH, '//input[@formcontrolname="email"]') #wpisz adres emial
        password = (By.XPATH, '//input[@type="password" and @name="password"]') #tworzenie hasła
        sign_up_button = (By.XPATH, '//button[@class="action-btn" and @type="submit"]') #zarejestrój się
        accept_statute = (By.XPATH, '//input[@type="checkbox"]') #akceptacja statusu
        send = (By.XPATH, '//button[@class="action-btn"]') #wysyłanie zgłoszenia rejestracji

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
        error_paassword_message_5 = (By.XPATH, '//div[@class="error show" and text()=" Hasło musi mieć więcej niż 6 znaków "]')

class LogIn:
        country_list_bottom = (By.XPATH, "//span[@class='ng-arrow-wrapper']")
        country_u_r_li_input = (By.XPATH, "//div[@class='ng-select-container ng-has-value']")
        input_to_sent_key = (By.XPATH, "//input[@aria-autocomplete='list']")
        countries = (By.XPATH, "//div[@role='option']/span[contains(text(), 'Turcja')]/..")
        # scroll_element = (By.CLASS_NAME, "scrollable-content")
        next_button = (By.XPATH, "//button[@class='action-btn' and @type='submit']")
        email_address = (By.XPATH, "//input[@name='email']")
        password = (By.XPATH, "//input[@name='password']")
        loggin_buttom = (By.XPATH, "//button[text()='Zaloguj się']")

class Logged:
        get_acces_orange_buttom = (By.XPATH, '//a[@class="purchase-cta button button--orange" and @href="/pl/app/my-learning/catalog/course/37324" and text()=" Odblokuj dostęp "]')
        unlock = (By.XPATH, "//a[@class='action-btn ng-star-inserted' and @href='/pl/app/order/payment/subscription?target=37324']")
        catalog_buttom = (By.ID, "catalogTooltip")
        course_language = (By.XPATH, '//button[@class="filter-btn ng-star-inserted"]//span[text()="Język kursu"]')
        chinese = (By.XPATH, '//button[@class="filter-btn choose-option" and text()=" chiński "]')
        apply = (By.XPATH, '//*[text()=" Zastosuj "]')
        courses = (By.XPATH, '//*[@class="course"]')
        more = (By.ID, 'more')
        redeem_your_access_code = (By.CSS_SELECTOR, 'a[href="/pl/app/my-learning/more/code"]')
        enter_your_access_code = (By.XPATH, '//input[@placeholder="Wpisz kod dostępu"]')
        confirm_code = (By.XPATH, '//button[text()=" Zatwierdź "]')
        incorrect_code = (By.XPATH, "//div[@class='warning ng-star-inserted' and contains(text(), ' Błędny kod ')]")
class PaymentDetails:
        full_name = (By.XPATH, '//input[@placeholder="Imię i nazwisko"]')
        card_number = (By.XPATH, "//input[@placeholder='Numer karty']")
        MM = (By.XPATH, '//input[@placeholder="MM"]')
        YYYY_year = (By.XPATH, '//input[@placeholder="YYYY"]')
        CVC_CVV = (By.XPATH, '//input[@placeholder="CVC/CVV"]')
        Cardholder_name = (By.XPATH, '//input[@placeholder="Imię i nazwisko posiadacza"]')
        free_month = (By.XPATH, "//button[text()=' Rozpocznij darmowy miesiąc ']")
class SelectLanguage:
        english = (By.XPATH, '//span[@class="item-text" and  text()=" angielski "]')
        spanish = (By.XPATH, '//span[@class="item-text" and  text()=" hiszpański "]')
        german = (By.XPATH, '//span[@class="item-text" and  text()=" niemiecki "]')
        russian = (By.XPATH, '//span[@class="item-text" and  text()=" rosysjki "]')
        french = (By.XPATH, '//span[@class="item-text" and  text()=" francuski "]')
        chinese = (By.XPATH, '//span[@class="item-text" and  text()=" chiński "]')
        japanese = (By.XPATH, '//span[@class="item-text" and  text()=" japoński "]')
        dutch = (By.XPATH, '//span[@class="item-text" and  text()=" angielski "]')
        italian = (By.XPATH, '//span[@class="item-text" and  text()=" włoski "]')
        portuguese = (By.XPATH, '//span[@class="item-text" and  text()=" portugalski "]')
        swedish = (By.XPATH, '//span[@class="item-text" and  text()=" szwedzki "]')
        danish = (By.XPATH, '//span[@class="item-text" and  text()=" duński "]')
        norwegian = (By.XPATH, '//span[@class="item-text" and  text()=" norweski "]')
        czech = (By.XPATH, '//span[@class="item-text" and  text()=" czeski "]')
        finnish = (By.XPATH, ' //span[@class="item-text" and  text()=" fiński "]')
        arabic = (By.XPATH, '//span[@class="item-text" and  text()=" arabski "]')
        hungarian =(By.XPATH, '//span[@class="item-text" and  text()=" węgierski "]')

class CourseAccess:
        english_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! English"]')
        spanish_course = (By.XPATH,'//span[@class="ng-star-inserted" and text()="Hello! Español"]')
        german_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! Deutsch"]')
        russian_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! Русский"]')
        french_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! Français"]')
        chinese_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! 中文"]')
        japanese_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! 日本語"]')
        dutch_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! Nederlands"]')
        italian_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! Italiano"]')
        portuguese_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! Português"]')
        swedish_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! Svenska"]')
        danish_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! Dansk"]')
        norwegian_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! Norsk"]')
        czech_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! Čeština"]')
        finnish_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! Suomi"]')
        arabic_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! اَلْعَرَبِيَّة"]')
        hungarian_course = (By.XPATH, '//span[@class="ng-star-inserted" and text()="Hello! Magyar"]')





        loggin_page_next = (By.XPATH, "//button[contains(@class, 'action-btn') and contains(text(), 'Dalej')]")

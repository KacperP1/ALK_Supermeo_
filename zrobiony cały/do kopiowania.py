import faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
fake_data = Faker('pl_PL')



driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
# otwarcie strony
driver.get("https://www.supermemo.com/pl")
driver.maximize_window()
driver.implicitly_wait(10)
#akceptacja alertu
driver.find_element(By.XPATH, '//*[@id="cn-accept-cookie"]').click()
driver.implicitly_wait(10)
# sleep(3)
# klikniecie na głównij stronie "zarejestruj się"
driver.find_element(By.XPATH, "//a[@href='https://learn.supermemo.com/pl/authorization/v2/register?returnUrl=https://www.supermemo.com' and @class='register-button c-ml-4 c-mr-4 c-mr-xl-0 crunch-button crunch-button__full-background crunch-button__full-background--primary-color fz-14 d-none d-md-inline-block' and @target='_self']").click()
driver.implicitly_wait(5)
# sleep(10)
driver.find_element(By.XPATH,"//*[@id='firstname']").send_keys(fake_data.first_name())

sleep(5) # <---(tu problemy)
#wait.until(EC.element_to_be_clickable(By.XPATH, "//button[@class='action-btn' and @type='submit' and contains(text(),'Dalej')]"))
# nie działa   WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='action-btn' and @type='submit' and contains(text(),'Dalej')]")))
#driver.implicitly_wait(10)
#WebDriverWait.until(EC.visibility_of_element_located(By.XPATH,"//button[@class='action-btn' and @type='submit' and contains(text(),'Dalej')]")).click
# Klikanie dalej na pierwszym kroku rejestracji
driver.find_element(By.XPATH,"//button[@class='action-btn' and @type='submit' and contains(text(),'Dalej')]").click()
#driver.find_element(By.XPATH, "//button[@class='action-btn' and @type='submit']").click()

#lokalizator pola do wpisania adresu e-mail
poczta = driver.find_element(By.XPATH, "//input[@formcontrolname='email']")
poczta.send_keys(fake_data.email())
#lokalizator do wpisania hasła
haslo = driver.find_element(By.XPATH, "//input[@type='password' and @name='password']")
haslo.send_keys(fake_data.password(6))
#klikanie na przycisk tworzenia konta "Zarejestruj się" na drugim etapie rejestracji
driver.find_element(By.XPATH, "//button[@class='action-btn' and @type='submit']").click()

#krok 3 z rejestracji i akcpetacjia regulaminu
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
#klikanie na wyślij w rejestracji.
driver.find_element(By.XPATH, "//button[@class='action-btn']").click()
sleep(10)




"""f
rom selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.supermemo.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cn-accept-cookie"]')))
element.click()

try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='register-button crunch-button crunch-button__full-background crunch-button__full-background--primary-color fz-14 c-mt-only-2' and @href='https://learn.supermemo.com/pl/authorization/v2/register?returnUrl=https://www.supermemo.com' and @target='_self']")))
    element.click()
except TimeoutException:
    print("Element not found")


driver.quit()
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



APP_URL = "http://localhost:4444"
APP_LOGIN_BUTTON_XPATH = "/html/body/button"
OKTA_USERNAME_XPATH = '//*[@id="okta-signin-username"]'
OKTA_PASSWORD_XPATH = '//*[@id="okta-signin-password"]'
OKTA_BUTTON_XPATH = '//*[@id="okta-signin-submit"]' 
USERNAME = ""
PASSWORD = ""


driver = webdriver.Chrome()
driver.get(APP_URL)
login_button = driver.find_elements_by_xpath(APP_LOGIN_BUTTON_XPATH)[0]
login_button.click()

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, OKTA_USERNAME_XPATH)))

finally:
    login_field = driver.find_elements_by_xpath(OKTA_USERNAME_XPATH)[0]
    pw_field = driver.find_elements_by_xpath(OKTA_PASSWORD_XPATH)[0]
    signin_button = driver.find_elements_by_xpath(OKTA_BUTTON_XPATH)[0]
    login_field.send_keys(USERNAME)
    pw_field.send_keys(PASSWORD)
    signin_button.click()


try:
    profile_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'profilelogin')))
finally:
    print("Signed in!")

from selenium import webdriver
from selenium.webdriver.common.by import By
from creds import email, password, path, databaseURL
from loggedInScraper import goToClass

def login(e, p):
    url = 'https://www.gradescope.com/'
    browser = webdriver.Chrome()
    browser.get(url)
    init_button = browser.find_element(By.CSS_SELECTOR, "[class='tiiBtn tiiBtn-secondarySplash js-logInButton']")    
    init_button.click()

    email_box = browser.find_element(By.ID, "session_email")
    password_box = browser.find_element(By.ID, "session_password")

    email_box.send_keys(e)
    password_box.send_keys(p)
    form = browser.find_element(By.CSS_SELECTOR, "form")
    form.submit()
    goToClass(browser)


login(email, password)


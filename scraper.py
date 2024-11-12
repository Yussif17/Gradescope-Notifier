from selenium import webdriver
from selenium.webdriver.common.by import By
from creds import email, password, path, databaseURL
from loggedInScraper import goToClass
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def login(e, p):
    url = 'https://www.gradescope.com/'
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    browser = webdriver.Chrome(options=chrome_options)
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


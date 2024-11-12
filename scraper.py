from selenium import webdriver
from selenium.webdriver.common.by import By
from creds import email, password, path, databaseURL
from loggedInScraper import goToClass
import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate(path)
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': databaseURL
    })
ref = db.reference("/")
numAssignments = 0
assignmentStatus = 0

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
    goToClass(browser,numAssignments,assignmentStatus)


login(email, password)


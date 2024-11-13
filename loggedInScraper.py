from selenium import webdriver
from selenium.webdriver.common.by import By
from alert_user import alert_user
import firebase_admin
from firebase_admin import db
from creds import path, databaseURL

def goToClass(driver, className):

  # cred_obj = firebase_admin.credentials.Certificate(path)
  # default_app = firebase_admin.initialize_app(cred_obj, {
  #   'databaseURL': databaseURL
  # })
  # ref = db.reference("/")

  if not firebase_admin._apps:
      cred_obj = firebase_admin.credentials.Certificate(path)
      default_app = firebase_admin.initialize_app(cred_obj, {
          'databaseURL': databaseURL
      })
  ref = db.reference("/")
  # numAssignments = ref.get()['numAssignments{className}']
  # assignmentStatus = ref.get()['assignmentStatus{className}']
  data = ref.get()
  refinedClassName = className
  if (className == "CSE 247/502N"):
    refinedClassName = "CSE 247"
  numAssignments = ref.get()[f'numAssignments{refinedClassName}']
  assignmentStatus = ref.get()[f'assignmentStatus{refinedClassName}']
  
  courseBox = driver.find_element(By.XPATH, f"//*[text()='{className}']")
  courseBox.click()

  rows = driver.find_elements(By.XPATH, '//table/tbody/tr[@role="row"]')
  numberOfAssignments = 0
  for i in range(len(rows)):
    numberOfAssignments += 1
  

  assignments = driver.find_elements(By.CSS_SELECTOR, ".submissionStatus--score")
  testList = list()
  for el in assignments:
    testList.append(el.text)
  if (testList != assignmentStatus):
    alert_user()
    ref.update({f'assignmentStatus{refinedClassName}' : testList})
  if (numAssignments != numberOfAssignments):
    alert_user()
    ref.update({f'numAssignments{refinedClassName}' : numberOfAssignments})
  driver.back()



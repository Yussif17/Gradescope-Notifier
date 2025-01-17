from selenium import webdriver
from selenium.webdriver.common.by import By
from alert_user import alert_user
import firebase_admin
from firebase_admin import db
from creds import path, databaseURL
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
  refinedClassName = className
  if (className == "CSE 247/502N"):
    refinedClassName = "CSE 247"
  
  retries = 3
  for attempt in range(retries):
    try:
        data = ref.get()
        if data:
            numAssignments = data.get(f'numAssignments{refinedClassName}')
            assignmentStatus = data.get(f'assignmentStatus{refinedClassName}')
        if numAssignments is not None and assignmentStatus is not None:
            break
        else:
            print("Retrying data retrieval...")
            time.sleep(2) 
            attempt += 1
    except Exception as e:
        print(f"Error during data retrieval: {e}")
        time.sleep(2)

  courseBox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"//*[text()='{className}']"))
  )
  courseBox.click()

  rows = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//table/tbody/tr[@role="row"]'))
  )
  numberOfAssignments = 0
  for i in range(len(rows)):
    numberOfAssignments += 1
  
  assignments = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".submissionStatus--score"))
  )
  testList = list()
  for el in assignments:
    testList.append(el.text)
  if (testList != assignmentStatus):
    alert_user("New Grade Dropped")
    ref.update({f'assignmentStatus{refinedClassName}' : testList})
  if (numAssignments != numberOfAssignments):
    alert_user("New Assignment Dropped")
    ref.update({f'numAssignments{refinedClassName}' : numberOfAssignments})
  driver.back()



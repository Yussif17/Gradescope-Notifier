from selenium import webdriver
from selenium.webdriver.common.by import By
#from alert_user import alert_user

def goToClass(driver, numAssignments, assignmentStatus):
  courseBox = driver.find_element(By.XPATH, "//*[text()='Math 203']")
  courseBox.click()

  rows = driver.find_elements(By.XPATH, '//table/tbody/tr[@role="row"]')
  numberOfAssignments = 0
  for i in range(len(rows)):
    numberOfAssignments += 1

  assignmentStatus = driver.find_elements(By.CSS_SELECTOR, ".submissionStatus--score")
  testList = list()
  for el in assignmentStatus:
    testList.append(el.text)
  if (testList!=assignmentStatus):
    alert_user()
    assignmentStatus = testList
  if (numAssignments!=numberOfAssignments):
      alert_user()
      numAssignments = numberOfAssignments
  driver.quit()

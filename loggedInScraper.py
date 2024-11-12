from selenium import webdriver
from selenium.webdriver.common.by import By


def goToClass(driver):
  courseBox = driver.find_element(By.XPATH, "//*[text()='Math 203']")
  courseBox.click()

  rows = driver.find_elements(By.XPATH, '//table/tbody/tr[@role="row"]')
  numberOfAssignments = 0
  for i in range(len(rows)):
    numberOfAssignments += 1
  numAssignments = numberOfAssignments
  assignmentStatus = driver.find_elements(By.CSS_SELECTOR, ".submissionStatus--score")
  for el in assignmentStatus:
    print(el.text)
  input(' ')

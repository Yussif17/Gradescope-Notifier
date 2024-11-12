from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.gradescope.com/courses')


driver.find_element(By.CSS_SELECTOR, ".courseBox").click()

rows = driver.find_elements(By.XPATH, '//table//tr')
print(rows)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()

time.sleep(5)

title = driver.find_element(By.XPATH, './/div/h1')
print(title.text)

time.sleep(2)

elements = driver.find_element(By.CLASS_NAME, 'accordion-button')
elements.click()

time.sleep(2)


name = driver.find_element(By.ID, 'name' )
name.click()
name.clear()
name.send_keys("Somesh")

time.sleep(2)

email = driver.find_element(By.ID, 'email')
email.click()
email.clear()
email.send_keys('somesh@gmail.com')

time.sleep(2)

gender = driver.find_element(By.ID, 'gender')
gender.click()
print(gender.text)

time.sleep(2)

mobile = driver.find_element(By.ID, 'mobile')
mobile.click()
mobile.clear()
mobile.send_keys('123456789')

time.sleep(2)

dob = driver.find_element(By.ID, 'dob')
dob.clear()
dob.click()
dob.send_keys('26-02-1994')

time.sleep(2)

subjects = driver.find_element(By.ID, 'subjects')
subjects.click()
subjects.clear()
subjects.send_keys("English, Maths, Science")

time.sleep(5)

file = driver.find_element(By.ID, 'picture')
file.send_keys(r"C:\Users\kalya\OneDrive\Documents\Feature User Login.txt")

time.sleep(3)

state = driver.find_element(By.ID, 'state')
Select(state).select_by_visible_text("NCR")

time.sleep(5)

city = driver.find_element(By.ID, 'city')
Select(city).select_by_visible_text("Agra")

time.sleep(5)

login = driver.find_element(By.XPATH, "//input[@type='submit']")
login.click()

time.sleep(5)

driver.close()


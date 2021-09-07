from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
user_folder = ""
selfdrvn_goal_link = ""
email = ""
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--user-data-dir=C:/Users/" + user_folder + "/AppData/Local/Google/Chrome/User Data/Person 1") 
driver = webdriver.Chrome("./chromedriver.exe", options=options)
driver.get(selfdrvn_goal_link)
try:
    sleep(1)
    email_login = driver.find_element_by_css_selector("input[type='email']")
    email_login.send_keys(email)
    driver.find_element_by_css_selector("button#checkButton").click()
except Exception:
    pass
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-goal"))).click()
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".personal-goal"))).click()
goal = driver.find_element_by_css_selector(".cdk-text-field-autofill-monitored")
goal.send_keys("-")
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".input-group.date"))).click()
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".today"))).click()
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-blue.pull-right"))).click()
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Ongoing')]"))).click()
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/modal-container/div/div/complete-goal/div[3]/button"))).click()
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Yes')]//parent::button"))).click()
sleep(2)
driver.quit()

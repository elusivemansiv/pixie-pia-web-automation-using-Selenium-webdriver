from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

excute_path = ("C:\\Driver\\chromedriver-win64\\chromedriver.exe")
service = Service(excute_path)
driver = webdriver.Chrome(service=service)

driver.get("https://pixie-pia.web.app/login")

time.sleep(5)

# login to pixipia
uname = driver.find_element(By.NAME, 'email')
uname.send_keys('mansib@gmail.com')

password = driver.find_element(By.NAME, 'password')
password.send_keys('Mansib123#')

login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/form/div[4]/button')
login_button.click()

time.sleep(5)

logout_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/a/button')
logout_button.click()
time.sleep(5)

driver.quit()

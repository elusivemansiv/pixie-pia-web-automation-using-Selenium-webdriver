from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
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

# View my Toy List
driver.get("https://pixie-pia.web.app/mytoys")

time.sleep(5)  # Sleep for 5 seconds

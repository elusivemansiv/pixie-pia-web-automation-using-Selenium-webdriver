from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Path to the ChromeDriver executable
chrome_driver_path = "C:\\Browser Driver\\chromedriver.exe"

# Set up the Chrome WebDriver service
service = Service(chrome_driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Log In
driver.get("https://pixie-pia.web.app/login")
wait = WebDriverWait(driver, 60)

# Wait for the email input field to be visible
email_input = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
email_input.send_keys("mansib@gmail.com")

# Find the password input field and enter password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("Mansib123#")

# Click on the login button
login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/form/div[4]/button')
login_button.click()

time.sleep(5)  # Sleep for 5 seconds

# Add Toy
driver.get("https://pixie-pia.web.app/addtoy")

time.sleep(5)  # Sleep for 5 seconds

# Fill in toy details
driver.find_element(By.NAME, "toyName").send_keys("Cowboy")
driver.find_element(By.NAME, "price").send_keys("5")

category_select = Select(wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/form/div[1]/div[3]/select'))))
category_select.select_by_visible_text("Playsets")

subcategory_select = Select(wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/form/div[1]/div[4]/select'))))
subcategory_select.select_by_visible_text("Toy Story Playset")

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div[1]/div[5]/textarea').send_keys("Toy")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div[1]/div[6]/textarea').send_keys("Very good")

driver.find_element(By.NAME, "availableQuantity").send_keys("5")
driver.find_element(By.NAME, "pictureUrl").send_keys("https://i5.walmartimages.com/seo/Award-Winning-Disney-Pixar-Toy-Story-4-Woody-And-Buzz-Lightyear-2-Character-Pack-Movie-Inspired-Relative-Scale-For-Storytelling-Play_c5719fb2-ffe3-47ab-849f-840409636c0a_1.a24a047099e9e0740e47177ecd67d45d.jpeg")
driver.find_element(By.NAME, "rating").send_keys("5")
driver.find_element(By.NAME, "brand").send_keys("disney")
driver.find_element(By.NAME, "ageRange").send_keys("3-6")
driver.find_element(By.NAME, "material").send_keys("Plastic")
driver.find_element(By.NAME, "weight").send_keys("200gm")
driver.find_element(By.NAME, "color").send_keys("Yellow Blue")
driver.find_element(By.NAME, "countryOfOrigin").send_keys("Usa")

# Click on the add toy button
add_toy_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/form/div[2]/button')))
add_toy_button.click()

# View my Toy List
driver.get("https://pixie-pia.web.app/mytoys")

time.sleep(5)  # Sleep for 5 seconds

# Delete Toy
delete_toy_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div/table/tbody/tr[3]/td[7]/div[3]')))
delete_toy_button.click()

confirm_delete = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')))
confirm_delete.click()

confirm_delete_final = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')))
confirm_delete_final.click()

time.sleep(5)  # Sleep for 5 seconds

# Close the browser
driver.quit()

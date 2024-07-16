from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

# Add Toy
driver.get("https://pixie-pia.web.app/addtoy")

time.sleep(5)  # Sleep for 5 seconds
# Fill in toy details
driver.find_element(By.NAME, "toyName").send_keys("Cowgirl")
driver.find_element(By.NAME, "price").send_keys("25")

internal_title = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div[1]/div[3]/select')
select = Select(internal_title)
select.select_by_visible_text("Playsets")

internal_title = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/form/div[1]/div[4]/select')
select = Select(internal_title)
select.select_by_visible_text("Toy Story Playset")

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


# Wait until the add_toy_button is clickable
add_toy_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/form/div[2]/button'))
)
add_toy_button.click()

time.sleep(5)

# View my Toy List
driver.get("https://pixie-pia.web.app/mytoys")

time.sleep(5)  # Sleep for 5 seconds
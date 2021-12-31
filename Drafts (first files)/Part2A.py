import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_sum_of_prices(sum):
    assert sum > 2500, "Sum of prices is less or equal to 2500!"
    print("Sum of prices is larger than 2500!")


chrome_driver_path = "C:\Windows\chromedriver.exe"
site_URL = "https://demo.nopcommerce.com"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
action = ActionChains(driver)
driver.maximize_window()
driver.get(site_URL)

# Get inside the Desktops page
computers_element = driver.find_element(By.LINK_TEXT, "Computers")
time.sleep(2)
action.move_to_element(computers_element).perform()
time.sleep(2)
desktops_element = driver.find_element(By.LINK_TEXT, "Desktops")
action.move_to_element(desktops_element)
action.click()
action.perform()

# Find all prices on the Desktops page
prices = driver.find_elements(By.CLASS_NAME, 'price')
prices = [price.text for price in prices]
prices_floats = list(map(lambda price: float(price.replace('$', '').replace(',', '')), prices))
sum_of_prices = sum(prices_floats)
print(sum_of_prices)

# Test - if sum is larger than 2500$
test_sum_of_prices(sum_of_prices)

driver.quit()

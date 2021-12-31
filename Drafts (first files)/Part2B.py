import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from Tests import Tests


def test_sum_of_ids(sum):
    assert sum > 5, 'Sum of ids is less or equal to 5!'
    print('Sum of ids is larger than 5!')


chrome_driver_path = "C:\Windows\chromedriver.exe"
site_URL = "https://demo.nopcommerce.com"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
action = ActionChains(driver)
driver.maximize_window()
driver.get(site_URL)

# Get inside the Notebooks page
computers_element = driver.find_element(By.LINK_TEXT, "Computers")
time.sleep(2)
action.move_to_element(computers_element).perform()
time.sleep(2)
desktops_element = driver.find_element(By.LINK_TEXT, "Notebooks")
action.move_to_element(desktops_element)
action.click()
action.perform()

# Find all ids on the Notebooks page
product_items = driver.find_elements(By.CLASS_NAME, 'product-item')
ids = [int(element.get_attribute('data-productid')) for element in product_items]
sum_ids = sum(ids)
print(sum_ids)

# Test if the sum of product id's is larger than 5
# test_sum_of_ids(sum_ids)
Tests.test_sum_of_ids(sum_ids)
driver.quit()

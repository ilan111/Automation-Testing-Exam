import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def check_price(price):
    assert price > 1000, "Price is <= 1000"
    print("Price is greater than 1000!")


chrome_driver_path = "C:\Windows\chromedriver.exe"
site_URL = "https://demo.nopcommerce.com"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(site_URL)
time.sleep(2)
search_element = driver.find_element(By.NAME, "q")
search_element.send_keys("macbook")
time.sleep(2)
search_element.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
search_element.send_keys(Keys.ENTER)
time.sleep(2)

price = driver.find_element(By.CLASS_NAME, "product-price").text
price_float = float(price.replace("$", "").replace(",", ""))
description = driver.find_element(By.CLASS_NAME, "short-description").text

print("The Macbook's price is: " + price + "\nDescription:\n" + description)

check_price(price_float)
driver.quit()

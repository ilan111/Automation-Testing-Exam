import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:
    chrome_driver_path = r"C:\Windows\chromedriver.exe"
    site_URL = "https://demo.nopcommerce.com"
    global s
    global driver
    global action

    # General methods
    def open_site(self):
        self.s = Service(executable_path=self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.s)
        self.action = ActionChains(self.driver)
        self.driver.get(self.site_URL)
        self.driver.maximize_window()
        time.sleep(2)

    def driver_quit(self):
        self.driver.close()
        time.sleep(2)
        self.driver.quit()

    # Methods for Part 1
    def search(self, keyword):
        search_element = self.driver.find_element(By.NAME, "q")
        search_element.send_keys(keyword)
        time.sleep(2)
        search_element.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        search_element.send_keys(Keys.ENTER)
        time.sleep(2)

    def print_price_and_description(self):
        price = self.driver.find_element(By.CLASS_NAME, "product-price").text
        price_float = float(price.replace("$", "").replace(",", ""))
        description = self.driver.find_element(By.CLASS_NAME, "short-description").text
        print("The price is: " + price + "\nDescription:\n" + description)
        return price_float

    # Methods for Part 2
    def navigate_to_page(self, category, sub_category):
        computers_element = self.driver.find_element(By.LINK_TEXT, category)
        time.sleep(2)
        self.action.move_to_element(computers_element).perform()
        time.sleep(2)
        desktops_element = self.driver.find_element(By.LINK_TEXT, sub_category)
        self.action.move_to_element(desktops_element)
        self.action.click()
        self.action.perform()

    def summarize_prices(self):
        prices = self.driver.find_elements(By.CLASS_NAME, 'price')
        prices = [price.text for price in prices]
        prices_floats = list(map(lambda price: float(price.replace('$', '').replace(',', '')), prices))
        sum_of_prices = sum(prices_floats)
        print("The sum of the prices is: " + str(sum_of_prices))
        return sum_of_prices

    def summarize_ids(self):
        product_items = self.driver.find_elements(By.CLASS_NAME, 'product-item')
        ids = [int(element.get_attribute('data-productid')) for element in product_items]
        sum_ids = sum(ids)
        print("The sum of the id's is: " + str(sum_ids))
        return sum_ids

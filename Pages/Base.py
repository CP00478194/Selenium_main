from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


class Base():

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, by_locator):

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator))).click()

    def send_data(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator))).send_keys(text)

    def hover_on_element(self, by_locator):
        action = ActionChains(self.driver)
        Hover = action.move_to_element(by_locator).perform()

    def window_handle(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_on_product_and_give_product_name(self, by_locator):
        for i in by_locator:
            i.click()
            return i.text
            break

    def back_to_parent_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def backward(self):
        self.driver.back()















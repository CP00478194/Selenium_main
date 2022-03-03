import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Config.config import TestData


class Login():


    def __init__(self, driver):
        self.driver = driver

    username = "//input[@class='_2IX_2- VJZDxU']"
    password = "//input[@type='password']"
    login_btn = "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']"



    def login_into_app(self):
        self.driver.find_element(By.XPATH, self.username).send_keys(TestData.Username)
        self.driver.find_element(By.XPATH, self.password).send_keys(TestData.Password)
        self.driver.find_element(By.XPATH, self.login_btn).click()
        time.sleep(5)









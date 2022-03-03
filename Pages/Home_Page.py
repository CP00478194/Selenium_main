import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Pages.Base import Base


class Home_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    Grocery = "//div[text()='Grocery']"
    Fashion = "//div[text()='Fashion']"
    footwear = "//a[@class='_6WOcW9 _2-k99T']"
    Appliances = "//div[text()='Appliances']"
    kitchen_appliance = "//a[@class='_6WOcW9 _2-k99T']"
    home = "//div[text()='Home']"
    home_element = "//a[@class='_6WOcW9 _2-k99T']"
    Mobile = "//div[text()='Mobiles']"
    Electronics = "//div[text()='Electronics']"
    grocery_prod_details = "//div[@class='iyJgcM qY_4g_']"  # lists
    Add_item_grocery = "//span[text()='Add Item']"
    realme_mobile = "//div[text()='realme']"
    realme_mobile_product_details = "//div[@class='_4rR01T']"  # lists
    realme_Add_item = "//button[text()='ADD TO CART']"
    Men_footwear = "//a[@class='IRpwTa']"
    cart = "//span[text()='Cart']"
    serach_box = "//input[@name='q']"
    cross_sign = "//button[@class='_2KpZ6l _2doB4z']"
    title = "//div[@class='_3qX0zy']"

    def select_grocery(self):
        self.click_on_element(self.Grocery)


    def hover_fashion_and_select_element(self):
        fashion = self.driver.find_element(By.XPATH, self.Fashion)
        self.hover_on_element(fashion)
        self.click_on_element(self.footwear)

    def hover_appliances_and_select_element(self):
        hover_element = self.driver.find_element(By.XPATH, self.Appliances)
        self.hover_on_element(hover_element)
        self.click_on_element(self.kitchen_appliance)
        time.sleep(5)

    def hover_home_and_select_element(self):
        time.sleep(5)
        Home = self.driver.find_element(By.XPATH, self.home)
        self.hover_on_element(Home)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.kitchen_appliance).click()
        time.sleep(5)

    def home(self):
        self.driver.find_element(By.XPATH, self.Grocery).click()
        grocery_details = self.driver.find_elements(By.XPATH, self. grocery_prod_details)
        time.sleep(4)
        for i in grocery_details:
            print(i.text)
            self.driver.find_element(By.XPATH, self.Add_item_grocery).click()
            break
        print("complete")

    def search_functionality(self):
        self.send_data(self.serach_box, "Besan")
        self.driver.find_element(By.XPATH, self.serach_box).send_keys(Keys.ENTER)

    def click_on_cart(self):
        self.click_on_element(self.cart)

    def back_to_old_window(self):
        self.back_to_parent_window()

























import time

from selenium.webdriver.common.by import By

from Pages.Base import Base


class Appliances(Base):

    def __init__(self, driver):
        super().__init__(driver)

    Appliances = "//div[text()='Appliances']"
    kitchen_appliance ="//a[@class='_6WOcW9 _2-k99T']"
    select_kitchen_prod = "//a[@class='s1Q9rs']"
    kitchen_add_to_cart = "//button[text()='ADD TO CART']"

    def select_and_add_to_cart_Appliances(self):

        hover_element = self.driver.find_element(By.XPATH, self.Appliances)
        self.hover_on_element(hover_element)
        time.sleep(2)
        self.click_on_element(self.kitchen_appliance)
        product_details = self.driver.find_elements(By.XPATH, self.select_kitchen_prod)
        for i in product_details:
            print(i.text)
            i.click()
            break

        self.window_handle()
        self.click_on_element(self.kitchen_add_to_cart)

    def select_appliances_product_and_add_to_cart(self):

        product_details = self.driver.find_elements(By.XPATH, self.select_kitchen_prod)
        product_name = self.check_on_product_and_give_product_name(product_details)
        print("Grocery product name which added in your cart", product_name)
        self.window_handle()
        self.click_on_element(self.kitchen_add_to_cart)
        return product_name







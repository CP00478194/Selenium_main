import time

from selenium.webdriver.common.by import By

from Pages.Base import Base


class Grocery(Base):

    def __init__(self, driver):
        super().__init__(driver)

    grocery_prod_details = "//div[@class='iyJgcM qY_4g_']"  # lists
    Add_item_grocery = "//button[text()='ADD TO BASKET']"

    def select_product_and_add_to_cart(self):
        grocery_details = self.driver.find_elements(By.XPATH, self.grocery_prod_details)
        time.sleep(4)
        for i in grocery_details:
            print(i.text)
            self.driver.find_element(By.XPATH, self.Add_item_grocery).click()
            break
        print("complete")

    def select_grocery_product_and_add_to_cart(self):

        product_details = self.driver.find_elements(By.XPATH, self.grocery_prod_details)
        product_name = self.check_on_product_and_give_product_name(product_details)
        print("Grocery product name which added in your cart", product_name)
        self.window_handle()
        self.click_on_element(self.Add_item_grocery)
        return product_name





from selenium.webdriver.common.by import By

from Pages.Base import Base


class Home_Link(Base):

    def __init__(self, driver):
        super().__init__(driver)

    kitchen_product_details = "//a[@class='s1Q9rs']"
    kitchen_add_to_cart = "//button[text()='ADD TO CART']"

    def select_kitchen_product_and_add_to_cart(self):

        product_details = self.driver.find_elements(By.XPATH, self.kitchen_product_details)
        product_name = self.check_on_product_and_give_product_name(product_details)
        print("Fashion product name which is added in your cart", product_name)
        self.window_handle()
        self.click_on_element(self.kitchen_add_to_cart)
        return product_name


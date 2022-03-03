import time

from selenium.webdriver.common.by import By

from Pages.Base import Base


class Cart(Base):


    product_name = "//div[@class='_2-uG6-']"

    def verify_product_name(self):
        time.sleep(4)
        cart_product_name = self.driver.find_elements(By.XPATH, self.product_name)
        print(len(cart_product_name))
        name = []
        for i in cart_product_name:
            name.append(i.text)
        return name













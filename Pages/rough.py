import time

from selenium.webdriver.common.by import By

from Pages.Base import Base


class rough(Base):

    def __init__(self, driver):
        super().__init__(driver)

    Grocery = "//div[text()='Grocery']"
    Mobile = "//div[text()='Mobiles']"
    Electronics = "//div[text()='Electronics']"
    grocery_prod_details = "//div[@class='iyJgcM qY_4g_']"  # lists
    Add_item_grocery = "//span[text()='Add Item']"
    realme_mobile = "//div[text()='realme']"
    realme_mobile_product_details = "//div[@class='_4rR01T']"  # lists
    realme_Add_item = "//button[text()='ADD TO CART']"
    Men_footwear = "//a[@class='IRpwTa']"
    cart = "//span[text()='Cart']"
    search_item = "//ul[@class='col-12-12 _1MRYA1 _38UFBk']//li/descendant::div[@class='lrtEPN _17d0yO']"
    serach_box = "//input[@name='q']"


    def rough1(self):
        self.click_on_element(self.Grocery)
        grocery_details = self.driver.find_elements(By.XPATH, self. grocery_prod_details)
        time.sleep(4)
        for i in grocery_details:
            print(i.text)
            self.driver.find_element(By.XPATH, self.Add_item_grocery).click()
            break
        print("complete")

    def serach(self):
        self.driver.find_element(By.XPATH, self.serach_box).send_keys("Mi")
        item = self.driver.find_elements(By.XPATH, self.search_item)
        print(len(item))

















from selenium.webdriver.common.by import By

from Pages.Base import Base


class serach_result(Base):



    def __init__(self, driver):
        super().__init__(driver)

    tata_brand = "//div[text()='Tata']"
    product_details = "//a[@class='s1Q9rs']"

    def select_brand(self):
        self.click_on_element(self.tata_brand)


    def verify_brand(self):
        brand_details = self.driver.find_elements(By.XPATH, self.product_details)
        for i in brand_details:
            print(i.text())




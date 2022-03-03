import time
import unittest
from selenium import webdriver

import pytest

from Config.config import TestData
from Pages.Appliances import Appliances
from Pages.Cart import Cart
from Pages.Fashion import Fashion
from Pages.Grocery_Page import Grocery
from Pages.Home_Link import Home_Link
from Pages.Home_Page import Home_Page
from Pages.Login import Login
from Pages.rough import rough


class login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=TestData.Chrome_Executable_Path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(TestData.Base_Url)

    def test_login_into_app(self):
        login = Login(self.driver)
        login.login_into_app()
        time.sleep(4)
        home = Home_Page(self.driver)
        home.home()

    def test_fashion(self):
        login = Login(self.driver)
        login.login_into_app()
        time.sleep(5)
        Fash = Fashion(self.driver)
        Fash.fashion_test()


    def test_click(self):
        login = Login(self.driver)
        login.login_into_app()
        time.sleep(4)
        b = rough(self.driver)
        b.rough1()


    def test_Appliances(self):
        login = Login(self.driver)
        login.login_into_app()
        time.sleep(4)
        App = Appliances(self.driver)
        App.select_and_add_to_cart_Appliances()

    def test_serach(self):
        login = Login(self.driver)
        login.login_into_app()
        time.sleep(4)
        b = rough(self.driver)
        b.serach()

    def test_fashion_wishlist(self):
        login = Login(self.driver)
        login.login_into_app()
        time.sleep(4)
        F = Fashion(self.driver)
        F.wishlist_check_fashion()

    def test_home_item(self):
        login = Login(self.driver)
        login.login_into_app()
        home = Home_Page(self.driver)
        home.hover_home_and_select_element()
        home_link = Home_Link(self.driver)
        kitchen_product_name = home_link.select_kitchen_product_and_add_to_cart()

        time.sleep(4)

    def test_appliance(self):
        login = Login(self.driver)
        login.login_into_app()
        home = Home_Page(self.driver)
        appliances = Appliances(self.driver)
        home.hover_appliances_and_select_element()
        appliances_product_name = appliances.select_appliances_product_and_add_to_cart()

    def test_cart_check(self):
        login = Login(self.driver)
        login.login_into_app()
        home = Home_Page(self.driver)
        home.click_on_cart()
        cart = Cart(self.driver)
        name1 = cart.verify_product_name()
        print(name1)














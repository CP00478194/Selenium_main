import unittest

from Config.config import TestData
from selenium import webdriver

from Pages.Home_Page import Home_Page
from Pages.Login import Login
from Pages.Search_Result_Page import serach_result


class search_and_filter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=TestData.Chrome_Executable_Path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(TestData.Base_Url)

    def test_search_and_filter_fun(self):
        login = Login(self.driver)
        login.login_into_app()
        home = Home_Page(self.driver)
        home.search_functionality()
        serach = serach_result(self.driver)
        serach.select_brand()
        filtered_result= serach.verify_brand()
        print(len(filtered_result))


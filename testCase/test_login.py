from selenium import webdriver
from pages.login_page import LoginPage
import unittest


class MyTestCase(unittest.TestCase):


    def test_valid_login():
        driver = webdriver.Chrome()
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("demo")
        login_page.enter_password("password")
        login_page.click_login()
        assert login_page.on_home_page()
        driver.close()

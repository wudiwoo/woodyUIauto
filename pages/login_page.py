class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.baidu.com/")

    def enter_username(self, username):
        pass

    def enter_password(self, password):
        pass

    def click_login(self):
        pass

    def on_home_page(self):
        # check if home page loaded
        return True

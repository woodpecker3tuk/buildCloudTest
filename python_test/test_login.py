from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogin():
    def setup_method(self,method):
        # 复用浏览器
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)

        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self,method):
        self.driver.quit()



from selenium.webdriver.common.by import By

from buildCloud_test.test_login import TestLogin


class Test_setProduct(TestLogin):
    def test_projectcreat(self):
        self.driver.find_element(By.LINK_TEXT,"项目创建与维护").click()
        self.driver.find_element(By.CLASS_NAME,"create-button").click

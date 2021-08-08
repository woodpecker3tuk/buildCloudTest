# 用cookie自动登录
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestLogin():
    def setup_method(self,method):

        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self,method):
        self.driver.quit()

    def test_cookie(self):
        # cookie若不是开发给个定死的，过段时间是需要更新的
        db = shelve.open("mydb/cookie")
        cookies = db['cookie']
        db.close()
        # 先打开要访问的页面，存入cookie值
        self.driver.get("https://app.jiansheyun.com.cn/view/ProductionManagement/Project")
        for cookie in cookies:
            if 'exoiry' in cookie.keys():
                cookie.pop('exoiry')
            self.driver.add_cookie(cookie)
        # 再次打开存好cookie值的页面，找到需要定位的内容
        self.driver.get("https://app.jiansheyun.com.cn/view/ProductionManagement/Project")
        self.driver.find_element(By.XPATH, "//*[@id='lay_applist']/li[2]").click()


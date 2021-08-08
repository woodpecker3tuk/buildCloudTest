import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestLogin():
    def setup_method(self,method):
        # # 复用浏览器
        # option = Options()
        # option.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://app.jiansheyun.com.cn/view/BIMCollaborationPlatform/Project")

        self.driver = webdriver.Chrome()

        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self,method):
        self.driver.quit()

    def test_contact(self):

        sleep(2)
        self.driver.find_element(By.XPATH,"//*[@id='lay_applist']/li[2]").click()

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        self.driver.get("https://app.jiansheyun.com.cn/view/ProductionManagement/Project")
        cookies = [{'domain': 'app.jiansheyun.com.cn', 'expiry': 1628411174, 'httpOnly': True, 'name': 'acw_tc', 'path': '/', 'secure': False, 'value': '7b39758516284093744214845eeeb1be3f2734781c1f453b612201082b0e75'}, {'domain': 'app.jiansheyun.com.cn', 'httpOnly': False, 'name': 'ispclient', 'path': '/', 'secure': False, 'value': 'undefined'}, {'domain': 'app.jiansheyun.com.cn', 'httpOnly': False, 'name': 'SERVERID', 'path': '/', 'secure': False, 'value': '51443bab1af53b72f830e210bf28fb1b|1628409379|1628409374'}, {'domain': 'app.jiansheyun.com.cn', 'httpOnly': False, 'name': 'sessionid', 'path': '/', 'secure': False, 'value': '87bd3952-00c2-4a38-bf92-5521d7b49005'}]

        sleep(3)
        for cookie in cookies:
            if 'exoiry' in cookie.keys():
                cookie.pop('exoiry')
            self.driver.add_cookie(cookie)

        self.driver.get("https://app.jiansheyun.com.cn/view/ProductionManagement/Project")
        self.driver.find_element(By.XPATH, "//*[@id='lay_applist']/li[2]").click()

    def test_cookies1(self):
        # shelve小型数据库，对象持久化保存方法
        cookies = [{'domain': 'app.jiansheyun.com.cn', 'expiry': 1628411174, 'httpOnly': True, 'name': 'acw_tc', 'path': '/', 'secure': False, 'value': '7b39758516284093744214845eeeb1be3f2734781c1f453b612201082b0e75'}, {'domain': 'app.jiansheyun.com.cn', 'httpOnly': False, 'name': 'ispclient', 'path': '/', 'secure': False, 'value': 'undefined'}, {'domain': 'app.jiansheyun.com.cn', 'httpOnly': False, 'name': 'SERVERID', 'path': '/', 'secure': False, 'value': '51443bab1af53b72f830e210bf28fb1b|1628409379|1628409374'}, {'domain': 'app.jiansheyun.com.cn', 'httpOnly': False, 'name': 'sessionid', 'path': '/', 'secure': False, 'value': '87bd3952-00c2-4a38-bf92-5521d7b49005'}]
        db = shelve.open("mydb/cookie")
        db['cookie'] = cookies
        db.close()

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin:
    def test_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookie = self.driver.get_cookies()
        # 打开yaml文件，设置为写模式覆盖以前写的东西
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)  # 向yaml文件中写入fcookie变量,将python转换为yaml格式

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)  # 将yaml转换为python格式
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()
        self.driver.find_element_by_link_text("添加成员").click()
        self.driver.find_element_by_id("username").send_keys("段少")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("000001")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("18012345678")
        self.driver.find_element_by_link_text("保存").click()
        iphone = self.driver.find_element_by_xpath('//*[@title="18012345678"]')
        assert iphone.text == '18012345678'










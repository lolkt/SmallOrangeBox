import unittest
from public import PySele
from vecode import VerificationCood
import time


class SearchTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = PySele(brower="NotChrome")
        self.driver.open(url="http://admin.kf.vizhuo.cn/")
        self.driver.make_maxwindow()

    def check(self, result, result1, username, password, tipstap):
        # 判断元素是否存在
        element = self.driver.element(fangfa="name", dingwei="verificationCode").is_displayed()
        if element is True:
            e1 = "F"
        else:
            e1 = "T"
        if e1 == "T":
            time.sleep(1)
            # 用户名输入框
            self.driver.element(fangfa="name", dingwei="account").send_keys(username)
            time.sleep(1)
            # 密码输入框
            self.driver.element(fangfa="name", dingwei="plaintext").send_keys(password)
            time.sleep(1)
            # 点击登录
            self.driver.double_click(fangfa="id", dingwei="bl")
            tips = self.driver.element(fangfa="xpath", dingwei="//*[@id=\"pageForm\"]/div/div[4]").text
            tips1 = tipstap
            self.assertEqual(tips, tipstap)
            if tips == tips1:
                print(result)
            else:
                print(result1)
        elif e1 == "F":
            # 识别验证码
            code = VerificationCood().vecode(self.driver)
            print(code)
            # 用户名输入框
            self.driver.element(fangfa="name", dingwei="account").send_keys(username)
            time.sleep(1)
            # 密码输入框
            self.driver.element(fangfa="name", dingwei="plaintext").send_keys(password)
            # 输入验证码
            time.sleep(1)
            self.driver.element(fangfa="xpath", dingwei="//*[@id=\"pageForm\"]/div/div[3]/div/input\"]/div/div[4]") \
                .send_keys(code)
            time.sleep(1)
            # 点击登录
            self.driver.double_click(fangfa="id", dingwei="bl")
            tips = self.driver.element(fangfa="xpath", dingwei="//*[@id=\"pageForm\"]/div/div[4]").text
            tips1 = tipstap
            self.assertEqual(tips, tipstap)
            if tips == tips1:
                print(result)
            else:
                print(result1)
        else:
            print("未知错误请检查代码")

    def test_one(self):
        self.check(result="用户名错误,密码正确用例执行成功", result1="用户名错误,密码正确用例执行失败", username="admin", password="111",
                   tipstap="用户名或密码错误、或账户被停用")

    def test_two(self):
        self.check(result="用户名正确,密码错误用例执行成功", result1="用户名正确,密码错误用例执行失败", username="admin", password="111",
                   tipstap="用户名或密码错误、或账户被停用")

    def test_three(self):
        self.check(result="用户名错误,密码错误用例执行成功", result1="用户名错误,密码错误用例执行失败", username="admin111", password="111",
                   tipstap="用户名或密码错误、或账户被停用")

    def tearDown(self):
        self.driver.close()
        self.driver.kill()


if __name__ == '__main__':
    unittest.main()

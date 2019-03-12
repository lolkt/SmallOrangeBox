# -*- coding: UTF-8 -*-
import time

from SmallOrangeBox.public import PySele
import unittest
# 打开浏览器
# driver = PySele(brower="Chrome")
# 不开开浏览器
driver = PySele(brower="NotChrome")
driver.open(url="http://admin.kf.vizhuo.cn/")
driver.make_maxwindow()
# option = webdriver.ChromeOptions()  # 不开开浏览器
# option.add_argument("headless")  # 不开开浏览器
# driver = webdriver.Chrome(chrome_options=option)
# driver.maximize_window()
# driver.get("http://admin.kf.vizhuo.cn/")




# noinspection PyBroadException
try:
    driver.check(result="用户名错误,密码正确用例执行成功", result1="用户名错误,密码正确用例执行失败", username="admin", password="111",
          tipstap="用户名或密码错误、或账户被停用")
except Exception:
        print("用户名错误,密码正确用例执行失败")
        driver.kill()
# noinspection PyBroadException
try:
    driver.check(result="用户名正确,密码错误用例执行成功", result1="用户名正确,密码错误用例执行失败", username="admin", password="111",
          tipstap="用户名或密码错误、或账户被停用")
except Exception:
        print("用户名错误,密码正确用例执行失败")
        driver.kill()
# noinspection PyBroadException
try:
    driver.check(result="用户名错误,密码错误用例执行成功", result1="用户名错误,密码错误用例执行失败", username="admin111", password="111",
          tipstap="用户名或密码错误、或账户被停用")
except Exception:
        print("用户名错误,密码错误用例执行失败")
        driver.kill()
driver.signin(username="admin", password="1", title="彩营营销管理系统")
driver.kill()
exit()

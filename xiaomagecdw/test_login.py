# coding:utf-8
'''
Created on 2017年7月18日
@author: chendaiwu
'''

#from selenium import webdriver
from time import sleep

from xiaomagecdw.PublicClass import PublicClass


class login_page(PublicClass):

    def test_case01(self):

        driver = self.driver

        #driver = ChoiceBrowser('fire') #输入浏览器类型，调用选择浏览器设置
        #driver = webdriver.Firefox()
        #driver.maximize_window()
        driver.get("http://www.baidu.com/")
        driver.implicitly_wait(5)

        driver.find_element_by_link_text(u"登录").click()
        sleep(2)
        driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        sleep(2)
        driver.find_element_by_name("userName").send_keys(u"小马哥xxy")
        driver.find_element_by_name("password").send_keys(u"cdw520xxy1314")
        driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
        sleep(12)
        #driver.close()

# coding=utf-8
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select
import time


class PySele(object):
    # 初始化浏览器
    def __init__(self, brower):
        if brower == 'firefox' or brower == 'Firefox' or brower == 'f' or brower == 'F':
            deriver = webdriver.Firefox()
        elif brower == 'Ie' or brower == 'ie' or brower == 'i' or brower == 'I':
            deriver = webdriver.Ie()
        elif brower == 'Chrome' or brower == 'chrome' or brower == 'Ch' or brower == 'ch':
            deriver = webdriver.Chrome()
        # 不开开浏览器
        elif brower == 'NotChrome' or brower == 'notchrome' or brower == 'No' or brower == 'no':
            option = webdriver.ChromeOptions()
            option.add_argument("headless")
            deriver = webdriver.Chrome(chrome_options=option)
        elif brower == 'PhantomJS' or brower == 'phantomjs' or brower == 'ph' or brower == 'phjs':
            deriver = webdriver.PhantomJS()
        elif brower == 'Edge' or brower == 'edge' or brower == 'Ed' or brower == 'ed':
            deriver = webdriver.Edge()
        elif brower == 'Opera' or brower == 'opera' or brower == 'op' or brower == 'OP':
            deriver = webdriver.Opera()
        elif brower == 'Safari' or brower == 'safari' or brower == 'sa' or brower == 'saf':
            deriver = webdriver.Safari()
        else:
            raise NameError('只能输入firefox,Ie,Chrome,PhantomJS,Edge,Opera,Safari')
        self.driver = deriver

    def element(self, fangfa, dingwei):  # 定位
        if fangfa == 'id':
            element = self.driver.find_element_by_id(dingwei)
        elif fangfa == "name":
            element = self.driver.find_element_by_name(dingwei)
        elif fangfa == "class":
            element = self.driver.find_element_by_class_name(dingwei)
        elif fangfa == "link_text":
            element = self.driver.find_element_by_link_text(dingwei)
        elif fangfa == "xpath":
            element = self.driver.find_element_by_xpath(dingwei)
        elif fangfa == "tag":
            element = self.driver.find_element_by_tag_name(dingwei)
        elif fangfa == "css":
            element = self.driver.find_element_by_css_selector(dingwei)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element

    # 组定位
    def elements(self, fangfa, dingwei):
        if fangfa == 'id':
            element = self.driver.find_elements_by_id(dingwei)
        elif fangfa == "name":
            element = self.driver.find_elements_by_name(dingwei)
        elif fangfa == "class":
            element = self.driver.find_elements_by_class_name(dingwei)
        elif fangfa == "link_text":
            element = self.driver.find_elements_by_link_text(dingwei)
        elif fangfa == "xpath":
            element = self.driver.find_elements_by_xpath(dingwei)
        elif fangfa == "tag":
            element = self.driver.find_elements_by_tag_name(dingwei)
        elif fangfa == "css":
            element = self.driver.find_elements_by_css_selector(dingwei)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element

    # 等待
    def element_wait(self, fangfa, dingwei, wati=3):

        if fangfa == "id":
            WebDriverWait(self.driver, wati, 1).until(ec.presence_of_element_located((By.ID, dingwei)))
        elif fangfa == "name":
            WebDriverWait(self.driver, wati, 1).until(ec.presence_of_element_located((By.NAME, dingwei)))
        elif fangfa == "class":
            WebDriverWait(self.driver, wati, 1).until(ec.presence_of_element_located((By.CLASS_NAME, dingwei)))
        elif fangfa == "link_text":
            WebDriverWait(self.driver, wati, 1).until(ec.presence_of_element_located((By.LINK_TEXT, dingwei)))
        elif fangfa == "xpath":
            WebDriverWait(self.driver, wati, 1).until(ec.presence_of_element_located((By.XPATH, dingwei)))
        elif fangfa == "css":
            WebDriverWait(self.driver, wati, 1).until(ec.presence_of_element_located((By.CSS_SELECTOR, dingwei)))
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css'.")

    # 打开网页
    def open(self, url):
        self.driver.get(url)

    # 最大化浏览器
    def make_maxwindow(self):
        self.driver.maximize_window()

    # 设置窗口
    def set_winsize(self, wide, hight):
        self.driver.set_window_size(wide, hight)

    # 发送内容
    def send_key(self, fangfa, dingwei, text):
        self.element(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.clear()
        e1.send_keys(text)

    # 清空
    def clear(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.clear()

    # 单击
    def clic(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.click()

    # 右击
    def right_click(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        ActionChains(self.driver).context_click(e1).perform()

    # 移动到
    def move_element(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        ActionChains(self.driver).move_to_element(e1).perform()

    # 双击
    def double_click(self, dingwei, fangfa):
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        ActionChains(self.driver).double_click(e1).perform()

    # 从e1到e2
    def drag_and_drop(self, fangfa1, e1, fangfa2, e2):
        self.element_wait(fangfa1, e1)
        eme1 = self.element(fangfa1, e1)
        self.element_wait(fangfa2, e2)
        eme2 = self.element(fangfa2, e2)
        ActionChains(self.driver).drag_and_drop(eme1, eme2).perform()

    # 点击文字
    def click_text(self, text):
        self.driver.find_element_by_link_text(text).click()

    # 关闭
    def close(self):
        self.driver.close()

    # 退出
    def kill(self):
        self.driver.quit()

    # 提交
    def sublimit(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.sublimit()

    # 刷新
    def f5(self):
        self.driver.refresh()

    # 执行js
    def js(self, sprit):
        self.driver.execute_script(sprit)

    def get_attribute(self, fangfa, dingwei, attribute):
        e1 = self.element(fangfa, dingwei)
        return e1.get_attribute(attribute)

    def get_text(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        return e1.text

    def get_is_dis(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        return e1.is_displayed()

    # 获取title
    # def get_title(self, fangfa, dingwei):
    def get_title(self):
        return self.driver.title

    # 获取当前页面url
    def get_url(self):
        return self.driver.current_url

    # 截屏
    def get_screen(self, file_path):
        self.driver.get_screenshot_as_file(file_path)

    # 等待
    def wait(self, fangfa, dingwei):
        self.driver.implicitly_wait((fangfa, dingwei))

    # 允许
    def accpet(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    # 切换iframe
    def switch_to_frame(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        if1 = self.element(fangfa, dingwei)
        self.driver.switch_to.frame(if1)

    def frame(self, dingwei):
        self.driver.switch_to.frame(dingwei)

    # 切出iframe
    def out_iframe(self):
        self.driver.switch_to.default_content()

    # 下拉框
    # index
    def select_index(self, fangfa, dingwei, index):
        Select(self.element(fangfa, dingwei)).select_by_index(index)

    # value
    def select_value(self, fangfa, dingwei, value):
        Select(self.element(fangfa, dingwei)).select_by_value(value)

    # text
    def select_text(self, fangfa, dingwei, text):
        Select(self.element(fangfa, dingwei)).select_by_visible_text(text)

    # option
    def select_option(self, fangfa, dingwei):
        self.element(fangfa, dingwei).select_by_option()

    # 登录模块
    def signin(self, username, password, title):
        element = self.element(fangfa="name", dingwei="verificationCode").is_displayed()
        if element is True:
            e1 = "F"
        else:
            e1 = "T"
        if e1 == "T":
            # 用户名输入框
            self.element(fangfa="name", dingwei="account").send_keys(username)
            # 密码输入框
            self.element(fangfa="name", dingwei="plaintext").send_keys(password)
            # 双击
            self.double_click(fangfa="id", dingwei="bl")
            title1 = self.get_title()
            if title1 == title:
                print("登录成功")
            else:
                print("登录失败,退出测试")
        elif e1 == "F":
            # 识别验证码
            code = VerificationCood().vecode(self.driver)
            # 用户名输入框
            self.element(fangfa="name", dingwei="account").send_keys(username)
            # 密码输入框
            self.element(fangfa="name", dingwei="plaintext").send_keys(password)
            # 输入验证码
            self.element(fangfa="name", dingwei="verificationCode").send_keys(code)
            # 双击
            self.double_click(fangfa="id", dingwei="bl")
            title1 = self.get_title()
            if title1 == title:
                print("登录成功")
            else:
                print("登录失败,退出测试")

    # 弹窗
    def popup(self):
        self.driver.switch_to.alert()

    # 获取弹窗信息
    def popup_text(self):
        return self.popup().text

    # 隐性等待
    def waiting_y(self, times):
        self.driver.implicitly_wait(times)

    # 判断元素是否存在
    # noinspection PyBroadException
    def iselementexist(self, fangfa, dingwei):
        flag = True
        try:
            self.element(fangfa, dingwei)
            return flag
        except Exception:
            flag = False
            return flag


    def check(self, result, result1, username, password, tipstap):
        # 判断元素是否存在
        element = self.element(fangfa="name", dingwei="verificationCode").is_displayed()
        if element is True:
            e1 = "F"
        else:
            e1 = "T"
        if e1 == "T":
            time.sleep(1)
            # 用户名输入框
            self.element(fangfa="name", dingwei="account").send_keys(username)
            time.sleep(1)
            # 密码输入框
            self.element(fangfa="name", dingwei="plaintext").send_keys(password)
            time.sleep(1)
            # 点击登录
            self.double_click(fangfa="id", dingwei="bl")
            tips = self.element(fangfa="xpath", dingwei="//*[@id=\"pageForm\"]/div/div[4]").text
            tips1 = tipstap
            if tips == tips1:
                print(result)
            else:
                print(result1)
        elif e1 == "F":
            # 识别验证码
            code = VerificationCood().vecode(self.driver)
            print(code)
            # 用户名输入框
            self.element(fangfa="name", dingwei="account").send_keys(username)
            time.sleep(1)
            # 密码输入框
            self.element(fangfa="name", dingwei="plaintext").send_keys(password)
            # 输入验证码
            time.sleep(1)
            self.element(fangfa="xpath", dingwei="//*[@id=\"pageForm\"]/div/div[3]/div/input\"]/div/div[4]") \
                .send_keys(code)
            time.sleep(1)
            # 点击登录
            self.double_click(fangfa="id", dingwei="bl")
            tips = self.element(fangfa="xpath", dingwei="//*[@id=\"pageForm\"]/div/div[4]").text
            tips1 = tipstap
            if tips == tips1:
                print(result)
            else:
                print(result1)
        else:
            print("未知错误请检查代码")
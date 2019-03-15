from vecode import *
from selenium.webdriver.common.action_chains import ActionChains

option = webdriver.ChromeOptions()  # 不开开浏览器
option.add_argument("headless")  # 不开开浏览器
driver = webdriver.Chrome(chrome_options=option)
# driver = webdriver.Chrome()
# driver.maximize_window()
User_name = ["admin", "admin1", ""]
Password = ["1", "123", ""]
driver.get("http://admin.kf.vizhuo.cn/")
driver.find_element_by_name("account").send_keys(User_name[1])
driver.find_element_by_name("plaintext").send_keys(Password[0])
mouse = driver.find_element_by_xpath('//*[@id="bl"]').click()
ActionChains(driver).double_click(mouse).perform()
Tips2 = driver.find_element_by_xpath('//*[@id="pageForm"]/div/div[4]').text
Tips3 = "验证码不能为空、请写验证码"
if Tips2 == Tips3:
    vcode = VerificationCood().Vcode(driver)
    driver.find_element_by_name("account").send_keys(User_name[1])
    driver.find_element_by_name("plaintext").send_keys(Password[0])
    driver.find_element_by_xpath('//*[@id="pageForm"]/div/div[3]/div/input').send_keys(vcode)
    ActionChains(driver).double_click(mouse).perform()
    Tips = driver.find_element_by_xpath('//*[@id="pageForm"]/div/div[4]').text
    Tips1 = "用户名或密码错误、或账户被停用"
    if Tips == Tips1:
        print("用户名错误,密码正确用例执行成功")
    else:
        print("用户名错误,密码正确用例执行失败")
else:
    Tips = driver.find_element_by_xpath('//*[@id="pageForm"]/div/div[4]').text
    Tips1 = "用户名或密码错误、或账户被停用"
    if Tips == Tips1:
        print("用户名错误,密码正确用例执行成功")
    else:
        print("用户名错误,密码正确用例执行失败")
driver.quit()
# Verification = driver.find_element_by_xpath('//*[@id="pageForm"]/div/div[3]/div/em/img')
# print(Verification)
# 判断元素是否存在方法一:
# def isElementExist(xpath):
#     try:
#         driver.find_element_by_xpath('//*[@id="pageForm"]/div/div[3]/div/em/img').is_displayed()
#         return False
#     except:
#         return True
# print(isElementExist(""))
# 判断元素是否存在方法二:
# def is_element_exist(css):
#     exist = driver.find_elements_by_css_selector("#pageForm > div > div.yzm-code > div > em > img")
#     if len(exist) == 1:
#         return True
#     else:
#         return False
# print(is_element_exist("css"))
# if is_element_exist("css") == False:
#     print(driver.current_url)
# else:
#     vcode = Verification_Code().Vcode(driver)
# print(vcode)
# driver.quit()

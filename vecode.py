# -*- coding: UTF-8 -*-
from selenium import webdriver
from PIL import Image
import pytesseract


class VerificationCood:
    def vecode(self, driver):
        imgelement = driver.find_element_by_xpath('//*[@id="pageForm"]/div/div[3]/div/em/img')
        # print(imgelement)
        # 图片坐标
        locations = imgelement.location
        # print(locations)
        # 图片大小
        sizes = imgelement.size
        # print(sizes)
        # 构造指数的位置
        rangle = (int(locations['x']), int(locations['y']), int(locations['x'] + sizes['width']), int(locations['y'] + sizes['height']))
        # print(rangle)
        # 截取全屏
        driver.save_screenshot("D:\\test\\yanzhengma.png")
        img = Image.open("D:\\test\\yanzhengma.png")
        # 按照坐标截图
        nimg = img.crop(rangle)
        nimg.save("D:\\test\\new_test.png")
        # 打开截图
        image = Image.open("D:\\test\\new_test.png")
        # 识别图中验证码
        mcode = pytesseract.image_to_string(image)
        return mcode


if __name__ == '__main__':
    # 不开开浏览器
    option = webdriver.ChromeOptions()
    # 不开开浏览器
    option.add_argument("headless")
    # 不开开浏览器
    driver = webdriver.Chrome(chrome_options=option)
    account = "admin"
    password = "2"
    password1 = "1"
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://admin.kf.vizhuo.cn/")
    print(driver.title)
    driver.find_element_by_xpath('//*[@id="bl"]').click()
    driver.find_element_by_xpath('//*[@id="bl"]').click()
    driver.find_element_by_xpath('//*[@id="bl"]').click()
    driver.find_element_by_xpath('//*[@id="bl"]').click()
    ccode = VerificationCood().vecode(driver)
    print(ccode)
    driver.find_element_by_name("account").send_keys(account)
    driver.find_element_by_name("plaintext").send_keys(password1)
    driver.find_element_by_xpath('//*[@id="pageForm"]/div/div[3]/div/input').send_keys(ccode)
    driver.find_element_by_xpath('//*[@id="bl"]').click()
    url = driver.current_url
    print(url)
    User_name = driver.find_element_by_xpath('/html/body/div[1]/div[1]/a[4]').text
    print(User_name)
    User_name1 = "系统管理员:admin"
    if User_name == User_name1:
        print("测试成功，结果和预期结果匹配！")
    else:
        print("测试失败，结果和预期结果不匹配！")
    driver.quit()

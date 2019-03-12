# -*- coding: UTF-8 -*-

from SmallOrangeBox.public import PySele
# 打开浏览器
# driver = PySele(brower="Chrome")
# 不开开浏览器
driver = PySele(brower="Chrome")
driver.open(url="http://admin.kf.vizhuo.cn/")
driver.make_maxwindow()
driver.signin(username="admin", password="1", title="彩营营销管理系统")
driver.click_text(text="业主管理")
driver.click_text(text="业主信息")
driver.switch_to_frame(fangfa="css", dingwei="#tt > div.tabs-panels > div:nth-child(2) > div > iframe")
driver.clic(fangfa="css", dingwei="#z-top > a.form_Btn_green")
# 返回主iframe
driver.out_iframe()
driver.switch_to_frame(fangfa="css", dingwei="#tt > div.tabs-panels > div:nth-child(3) > div > iframe")
driver.select_value(fangfa="name", dingwei="sysAreaOperateId", value="22")
driver.send_key(fangfa="css", dingwei="#name", text="赵承钰")
driver.send_key(fangfa="css", dingwei="#idCard", text="411503199508055315")
driver.send_key(fangfa="css", dingwei="#mobile", text="15910586223")
driver.clic(fangfa="css", dingwei="#pageForm > div.formBox > div.Button.t-left > input")
# 返回主iframe
driver.out_iframe()
# noinspection PyBroadException
try:
    driver.element_wait(fangfa="css", dingwei="#layui-layer1")
except Exception:
    print("响应超时")
element = driver.iselementexist(fangfa="css", dingwei="#layui-layer1")
print(element)
if element is False:
    driver.switch_to_frame(fangfa="css", dingwei="#tt > div.tabs-panels > div:nth-child(2) > div > iframe")
driver.out_iframe()

# texts = driver.element(fangfa="css", dingwei="#layui-layer1 > div.layui-layer-content").text
# print(texts)
# driver.clic(fangfa="css", dingwei="#layui-layer1 > div.layui-layer-btn > a")
driver.kill()

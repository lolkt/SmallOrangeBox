# coding=utf-8
import HTMLTestRunnerCN
import unittest
import time
from SmallOrangeBox.untext import SearchTestCase


suite = unittest.TestSuite()
# 获取TestSuite的实例对象
suite.addTest(SearchTestCase("test_one"))
suite.addTest(SearchTestCase("test_two"))
suite.addTest(SearchTestCase("test_three"))
# 把测试用例添加到测试容器中

times = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
# 获取当前时间
filename = times + "test.html"
# 文件名

fp = open(filename, "wb")
# 以二进制的方式打开文件并写入结果
runner = HTMLTestRunnerCN.HTMLTestRunner(
    stream=fp,
    verbosity=1,
    title="测试报告的标题",
    description="测试报告的详情",
    tester="赵承钰")

runner.run(suite)

fp.close()
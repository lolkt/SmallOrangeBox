# coding:utf-8
'''
Created on 2017年7月18日
@author: chendaiwu
'''

import unittest
from xiaomagecdw.choiceBrowser import ChoiceBrowser

class PublicClass(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = ChoiceBrowser("ch")


    def tearDown(self):
        self.driver.close()

    #def test01(self):
        #print "执行第一个用例！"
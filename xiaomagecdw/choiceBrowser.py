# coding:utf-8
'''
Created on 2017年7月18日
@author: chendaiwu
'''

from selenium import webdriver
import time
import re

def ChoiceBrowser(type):
    if type.strip().lower() == 'ch':
        try:
            driver = webdriver.Chrome()
        except:
            driver = None
    elif type.strip().lower() == 'fire':
        try:
            driver = webdriver.Firefox()
        except:
            driver = None
    elif type.strip().lower() == 'ie':
        try:
            driver = webdriver.Ie()
        except:
            driver = None
    else:
        print ( "浏览器类型错误："+type)
        driver = None

    if driver is not None:
        driver.maximize_window()
        time.sleep(2)
    return driver
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import unittest
from appium import webdriver
from time import sleep

sys.path.append("../BusinessUtils")
import business
from business import NewDriver

# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )

#类继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
class ContactsAndroidTests(unittest.TestCase):
    #setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。
    def setUp(self):
        self.driver = NewDriver()
    def tearDown(self):
        self.driver.driver.close_app()
        self.driver.driver.quit()

    def test_add_contacts(self):
        print('start sleep')
        sleep(10)
        print("sleep 10s")
        self.driver.clickOnElementByName('备孕')
        self.driver.clickOnElementByName('下一步')
        self.driver.clickOnElementByName('完成')
        self.driver.clickOnElementByName('帮生活')
        sleep(3)
        self.driver.clickOnElementByName('月子会所')
        sleep(3)
        print("Edit clicked")

#unitest.main()函数用来测试 类中以test开头的测试用例
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
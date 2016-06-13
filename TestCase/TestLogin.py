#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import unittest
from time import sleep
sys.path.append("../Base")
from base import myDriver

#类继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
class ContactsAndroidTests(unittest.TestCase):
    #setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。
    def setUp(self):
        self.driver = myDriver()

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    def test_add_contacts(self):
        print('start sleep')
<<<<<<< HEAD
        sleep(6)
=======
        sleep(7)
>>>>>>> study

        # print("sleep 10s")
        self.driver.clickOnElementByXpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[2]")
        print("xpath clicked")
        self.driver.set_value("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[1]","13661962542")
        # self.driver.clickOnElementByXpath()
        self.driver.set_value("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASecureTextField[1]","qq123456")
        
        # self.driver.clickOnElementByXpath("")
        sleep(5)
        # self.driver.clickOnElementByName('备孕')
        # self.driver.clickOnElementByName('下一步')
        # self.driver.clickOnElementByName('完成')
        # self.driver.clickOnElementByName('帮生活')
        # sleep(3)
        # self.driver.clickOnElementByName('月子会所')
        # sleep(3)

#unitest.main()函数用来测试 类中以test开头的测试用例
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
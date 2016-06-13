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

#类继承unittest.TestCase类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
class ContactsAndroidTests(unittest.TestCase):
    #setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。
    def setUp(self):
        self.driver = myDriver()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    def test_add_contacts(self):
        print('start sleep')

        # print("sleep 10s")
        self.driver.click_on_element("UIAButton","name","登录")
        print("xpath clicked")
        self.driver.set_value("UIATextField","value","手机号／网站帐号","13661962542")
        # self.driver.clickOnElementByXpath()
        self.driver.set_value("UIASecureTextField","value","密码","qq123456")
        

#unitest.main()函数用来测试类中以test开头的测试用例
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

#类继承unittest.TestCase 类，从TestCase类继承是告诉unittest模块的方式，这是一个测试案例。
class ContactsAndroidTests(unittest.TestCase):
    #setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。
    def setUp(self):
        desired_caps = {}
        #### desired_caps['udid'] = 'B6DDF5FC-FB4A-4EA0-BD81-063EB3D5172D'

        # desired_caps['platformName'] = 'iOS'
        # desired_caps['platformVersion'] = '9.3'
        # desired_caps['deviceName'] = 'iPhone 6 Plus'
        # desired_caps['app'] = PATH(
        #     '/Users/jimmy_zhou/Library/Developer/Xcode/DerivedData/Recipes-dazjfqhcqpgvvwgcndxbuupitdzk/Build/Products/Debug-iphonesimulator/Recipes.app'
        # )
        # desired_caps['bundleId'] = 'com.example.apple-samplecode.Recipes' 
        # instruments -w f599ef571c56f9f2ecd18a49244b2690285ec750 -v -t "Activity Monitor" -D Activity_Monitor.trace com.mmbang.main
        desired_caps['udid'] = 'f599ef571c56f9f2ecd18a49244b2690285ec750'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '8.3'
        desired_caps['deviceName'] = '周冬彬的 iPhone'
        desired_caps['app'] = PATH(
        	'/Users/jimmy_zhou/appium/apk/MMbang_master_3.13.3_43365_Test_DEBUG.ipa'
        	)
        desired_caps['bundleId'] = 'com.mmbang.main'
        
        print '连接中...'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        print '连接完成'
    #earDown 方法在每个测试方法执行后调用，这个地方做所有清理工作，如退出
    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    #放置的就是我们的测试脚本了，这部分我们并不陌生；因为我们执行的脚本就在这里。
    def test_add_contacts(self):
        # '''el = self.driver.find_element_by_name("Add Contact")
        # el.click()

        # textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        # textfields[0].send_keys("Appium User")
        # textfields[2].send_keys("someone@appium.io")

        # self.assertEqual('Appium User', textfields[0].text)
        # self.assertEqual('someone@appium.io', textfields[2].text)

        # self.driver.find_element_by_name("Save").click()

        # # for some reason "save" breaks things
        # alert = self.driver.switch_to_alert()

        # # no way to handle alerts in Android
        # self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

        # self.driver.keyevent(3)'''
        # self.driver.find_element_by_id('com.android.calculator2:id/digit9').click()
        self.driver.find_element_by_name('登录').click()
        # self.driver.find_element_by_name('Edit').click()
        # self.driver.find_element_by_name()
        sleep(3)
        print("Edit clicked")
        # self.driver.find_element_by_name('Done').click()
        # sleep(2)

    # def test_add_contacts2(self):
    # 	self.driver.find_element_by_name('Edit').click()
    # 	sleep(3)
    #     self.driver.find_element_by_name('Done').click()
    #     sleep(3)
    #     print("Done clicked")
#unitest.main()函数用来测试 类中以test开头的测试用例
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
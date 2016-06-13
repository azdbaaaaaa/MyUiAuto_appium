#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
from appium import webdriver
from time import sleep
reload(sys)
sys.setdefaultencoding('utf-8')


class myDriver(object):
    """docstring for myDriver"""
    def __init__(self):
        super(myDriver, self).__init__()
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        try:
            # print '连接中...'
            # self.desired_caps = {}
            # self.desired_caps['platformName'] = 'android'
            # # self.desired_caps['platformVersion'] = '4.2.1'
            # self.desired_caps['deviceName'] = '7SW84TYHLFSGCM4S'
            # # self.desired_caps['app'] = PATH(
            # #     '/Users/jimmy_zhou/Documents/workspace/MyUiAuto_appium/mmbang_svn-test.apk'
            # # )
            # self.desired_caps['appPackage'] = 'com.yaya.mmbang'
            # self.desired_caps['appActivity'] = '.activity.SplashActivity'
            # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
            # print '连接完成'
            print("开始设置desired_caps内容")
            self.desired_caps = {}
            self.desired_caps['udid'] = 'f599ef571c56f9f2ecd18a49244b2690285ec750'
            self.desired_caps['platformName'] = 'iOS'
            self.desired_caps['platformVersion'] = '8.3'
            self.desired_caps['deviceName'] = '周冬彬的 iPhone'
            self.desired_caps['app'] = PATH(
                '/Users/jimmy_zhou/appium/apk/MMbang_master_3.13.3_43365_Test_DEBUG.ipa'
            )
            self.desired_caps['bundleId'] = 'com.mmbang.main'
            print '连接中...'
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
            print '连接完成'
            # print self.session
        except Exception, e:
            raise e
        

    def click_on_element(self, UIA_type, method, name):
        try:
            print 1
            # //UIAButton[@name='登录']
            xpath = "//%s[@%s='%s']" % (UIA_type,method,name)
            print("PATH:" + xpath)
            e1 = self.driver.find_element_by_xpath(xpath)
            e1.click()
            print('点击元素成功')
        except Exception, e:
            print('点击元素失败')
            print(e)


    def clickOnElementByXpath(self, xpath):
        try:
            # sleep(3)
            e1 = self.driver.find_element_by_xpath(xpath)
            e1.click()
            print('点击元素成功')
        except Exception, e:
            print('点击元素失败')
            print(e)

    def set_value(self, UIA_type, method, value, content):
        try:
            xpath = "//%s[@%s='%s']" % (UIA_type,method,value)
            print("PATH:" + xpath)
            element = self.driver.find_element_by_xpath(xpath)
            self.driver.set_value(element, content)
            print("输入成功")
        except Exception, e:
            print("输入失败")
            print(e)

    def close_app(self):
        """Stop the running application, specified in the desired capabilities, on
        the device.
        """
        try:
            self.driver.close_app()
            print("退出应用成功")
        except Exception, e:
            print("退出应用失败")
            print(e)

    def quit(self):
        try:
            self.driver.quit()
            print("关闭成功")
        except Exception, e:
            print("关闭失败")
            print(e)

    def implicitly_wait(self, time):
        try:
            self.driver.implicitly_wait(time)
        except Exception, e:
            print(e)
    # def clickOnElementByXpath(self, driver):
    #     pass

    # def function():
    #     pass


# self.driver.close_app()
# self.driver.quit()

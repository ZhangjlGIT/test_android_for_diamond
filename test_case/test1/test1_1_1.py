# -*- coding:utf-8 _*-
"""
@author:zhangjianlang
@file: test1_1_1.py
@time: 2019/8/5 15:31
"""
from test_case.models import myunit
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
import unittest
import time


class testcase(myunit.MyTest):
    """测试用例说明注释，如首页"""
    def test1(self):
        """测试用例详情注释，如打开简介"""
        # 连接手机
        self.imgs = []  # 截图列表
        driver = self.uiHelper._driver
        time.sleep(10)

        driver.find_element_by_xpath("//android.view.View[@text='钻石会测试']").click()
        driver.implicitly_wait(10)
        self.imgs.append(driver.get_screenshot_as_base64())  # 截图

    def test2(self):
        """测试用例详情注释，如简介页信息正确"""
        # 连接手机
        self.imgs = []  # 截图列表
        driver = self.uiHelper._driver
        time.sleep(10)

        driver.find_element_by_xpath("//android.view.View[@text='钻石会测试']").click()
        driver.implicitly_wait(10)
        self.imgs.append(driver.get_screenshot_as_base64())  # 截图


if __name__ == '__main__':
    unittest.main()

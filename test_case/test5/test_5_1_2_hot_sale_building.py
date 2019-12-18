# -*- coding:utf-8 _*-
# 首页-购房服务-热销楼盘
"""
@author:zhangjianlang
@file: test5_1_1_hot_sale_building.py
@time: 2019/8/13 10:16
"""

from test_case.models import myunit
from public.AndrpidScreenshot import Screenshot
from test_case.models import goinMainPage
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class testcase(myunit.MyTest):
    """首页-购房服务-热销楼盘"""
    def test1(self):
        """进入热销楼盘"""
        self.imgs = []  # 截图列表
        driver = self.uiHelper._driver
        # ---------------------------------------------------测试用例------------------------------------------
        goinMainPage.gotoMainPage(self, driver)  # 进入公众号首页

        # 点击菜单 购房服务
        driver.find_element_by_xpath('//*[@id="nav_bar"]/div[1]/div/div[2]/span/img[2]').click()
        print('点击购房服务 ')
        driver.implicitly_wait(20)
        # 检查点
        self.assertEqual(driver.title, '购房服务', '进入页面失败！')
        time.sleep(3)
        # 截图
        self.imgs.append(Screenshot().executeScreenshot())


if __name__ == '__main__':
    unittest.main()


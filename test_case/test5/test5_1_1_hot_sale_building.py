# -*- coding:utf-8 _*-
# 首页-购房服务-热销楼盘
"""
@author:zhangjianlang
@file: test5_1_1_hot_sale_building.py
@time: 2019/8/13 10:16
"""

from test_case.models import myunit
from public.AndrpidScreenshot import Screenshot
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
        # 连接手机
        self.imgs = []  # 截图列表
        driver = self.uiHelper._driver
        time.sleep(10)

        # 聊天界面 点击公众号（事先顶置公众号在第一行，或通过搜索公众号进入）
        driver.find_element_by_xpath("//android.view.View[@text='房产信息化服务']").click()
        driver.implicitly_wait(20)

        # 点击菜单 进入钻石会
        driver.find_element_by_xpath("//android.widget.TextView[@text='进入钻石会']").click()
        driver.implicitly_wait(20)
        time.sleep(10)

        # 切入公众号 webview
        # print(driver.contexts)
        driver.switch_to.context(driver.contexts[1])  # 切入 WEBVIEW_com.tencent.mm:tools
        print('当前context为:', driver.current_context)
        driver.implicitly_wait(20)

        # 切入handles
        self.uiHelper.gotoHandles()
        driver.implicitly_wait(20)

        # 检查点 是否进入钻石会
        try:
            self.assertTrue(u"建发房产钻石会" in driver.page_source)
            print('成功进入公众号！')
        except:
            print('进入公众号失败！')

        # 判断是否有 广告弹窗
        try:
            driver.find_element_by_id("close_ad_mask").click()
            print('关闭广告弹窗')
        except:
            print('不存在广告弹窗')
            pass
        time.sleep(5)

        # ---------------------------------------------------测试用例------------------------------------------
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


# -*- coding:utf-8 _*-
# 测试用例脚本示例：打开公众号->打开简介
"""
@author:zhangjianlang
@file: HomePage.py
@time: 2019/7/29 16:05
"""
from test_case.models import myunit
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class testcase(myunit.MyTest):
    """测试用例说明，如首页"""
    def test1(self):
        """进入简介"""
        # 连接手机
        self.imgs = []  # 截图列表
        driver = self.uiHelper._driver
        time.sleep(10)

        # 滑动函数示例
        '''
        def swipedown(driver, t=500, n=1):
            # 向下滑动屏幕
            l = driver.get_window_size()
            x1 = l['width'] * 0.5  # x坐标
            y1 = l['height'] * 0.25  # 起始y坐标
            y2 = l['height'] * 0.75  # 终点y坐标
            for i in range(n):
                driver.swipe(x1, y1, x1, y2, t)
        '''
        # 向下滑动
        # swipedown(driver)

        # 【定位】方式一：调用自定义UiHelper类 中的 find_element 方法
        # self.uiHelper.find_element('com.tencent.mm:id/qh').click()

        # 【定位】方式二：使用 WebDriver 提供的查找控件方法
        # driver.find_element_id('com.tencent.mm:id/qh').click()
        # driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tencent.mm:id/jb']").click()

        # 输入 中文
        # self.uiHelper.find_element('android.widget.EditText').send_keys('钻石会测试')
        # 输入 回车（其他键位请查看文档）
        # driver.keyevent(4)

        # 等待方式

        # 方式一：强制等待
        # time.sleep(5)
        # 方式二：隐形等待
        driver.implicitly_wait(5)
        # 方式三：显性等待 如每隔0.3秒调用检查元素是否存在或不存在，最长等待10秒
        # locator = (By.ID, "com.tencent.mm:id/rc")
        # WebDriverWait(driver, 10, 0.3).until(EC.presence_of_element_located(locator), "已经超时找不到元素")
        # WebDriverWait(driver, 10, 0.3).until_not(EC.presence_of_all_elements_located(("ID", 'com.tencent.mm:id/lh')))

        #---------------------------------------------------测试用例------------------------------------------

        # 聊天界面 点击公众号（事先顶置公众号在第一行，或通过搜索公众号进入）
        driver.find_element_by_xpath("//android.view.View[@text='钻石会测试']").click()
        driver.implicitly_wait(10)

        # 点击菜单 进入钻石会
        driver.find_element_by_xpath("//android.widget.TextView[@text='进入钻石会']").click()
        driver.implicitly_wait(10)
        time.sleep(5)

        # 此步骤用于调试，请注意打开 debugx5.qq.com设置：信息->TBS setting->打开TBS内核 inspector调试功能
        print(driver.contexts)
        # ['NATIVE_APP', 'WEBVIEW_com.tencent.mm:tools', 'WEBVIEW_com.tencent.mm:toolsmp']  #所有页面的context

        print(driver.current_context)  # 打印当前页面的context,应为NATIVE_APP
        print('第一个页面源文件：%s' % driver.page_source)  # 打印 页面源文件
        time.sleep(5)

        # 切入公众号webview
        driver.switch_to.context('WEBVIEW_com.tencent.mm:toolsmp')  # 切入 webview
        time.sleep(5)

        print(driver.current_context)  # 打印当前页面的context,应为 WEBVIEW_com.tencent.mm:toolsmp
        print('第二个页面源文件：%s' % driver.page_source)  # 打印 页面源文件
        time.sleep(5)

        # 打印页面handles
        handles = driver.window_handles
        print(handles)
        # ['CDwindow-DEEF60AA07EE8BF56FFB15460F6D66F7', 'CDwindow-DFBD71868144287C73C32E6AC4AA399F']

        driver.switch_to.window(handles[1])
        print('handles[1]页面源文件：%s' % driver.page_source)  # 打印 页面源文件
        time.sleep(5)

        # 检查点 是否进入钻石会
        try:
            self.assertTrue("建发房产钻石会" in driver.page_source)
            # self.assertTrue("建发房产钻石会" in driver.page_source)
            print('成功进入公众号！')
        except:
            print('进入公众号失败！')

        # 判断是否有 广告弹窗
        try:
            driver.find_element_by_id("close_ad_mask").click()
            print('关闭广告弹窗')
        except ValueError as e:
            print('不存在广告弹窗,%s' % e)
            pass
        time.sleep(5)

        # 点击 简介
        driver.find_element_by_xpath('//*[@id="nav_detail_list"]/a[1]/span[2]').click()
        driver.implicitly_wait(10)
        print('进入简介')
        time.sleep(5)
        self.imgs.append(driver.get_screenshot_as_base64())  # 截图


if __name__ == '__main__':
    unittest.main()

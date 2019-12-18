# -*- coding:utf-8 _*-
# 读取Desired Capabilities的数据，并与Appium服务器进行连接
"""
@author:zhangjianlang
@file: UiHelper.py
@time: 2019/7/19 15:43
"""

from appium import webdriver
import logging
import time
import sys


class UiHelper():
    # 初始化，读取Desired Capabilities数据
    def __init__(self, configpath):
        self.desire_caps = {}
        self.chromeOptions = {'androidProcess': 'com.tencent.mm:tools'}  # 公众号需要配置chromeOptions
        self.remotehost = None
        self._driver = None
        # if configpath is None:
        #     configpath = 'environment.txt'
        #     print(configpath)
        file_object = open(configpath)
        try:
            for line in file_object:
                # 若前缀为井号
                if line.startswith("#"):
                    continue
                # 去除首尾空格
                line = line.strip()
                # 根据等号，分成两个字符串
                words = line.split("=")
                if len(words) != 2:
                    continue
                if words[0] == 'app':
                    self.desire_caps[words[0]] = self.PATH(words[1])
                elif words[0] == 'remoteHost':
                    self.remotehost = words[1]
                else:
                    self.desire_caps[words[0]] = words[1]

        finally:
            self.desire_caps.update(chromeOptions=self.chromeOptions)
            file_object.close()

    def init_driver(self):
        # 与Appium连接
        # print("配置参数的值为%s " % self.desire_caps)
        print("正在尝试连接Appium，请稍等...")
        self._driver = webdriver.Remote(self.remotehost, self.desire_caps)
        #time.sleep(5)
        self._driver.implicitly_wait(20)
        print("成功连接Appium")
        return self._driver

    def quit_driver(self):
        # 退出，关闭Appium连接
        if self._driver:
            print("正在关闭Appium，请稍等...")
            time.sleep(5)
            self._driver.quit()
            print("成功关闭Appium")

    # 获取手机屏幕大小
    def get_size(self):
        x = self._driver.get_window_size()['width']
        y = self._driver.get_window_size()['height']
        return x, y

    def find_element_uiauto(self,controlinfo):
        element = ""
        element = self._driver.find_element_by_android_uiautomator(controlinfo)
        return element

    def find_element(self, controlinfo):
        # 自定义封装控件查找
        element = ""
        # 若参数时以“//”开始，则使用xpath方式
        if controlinfo.startswith("//"):
            element = self._driver.find_element_by_xpath(controlinfo)
        # 若参数时以":id/"或":string/"，则使用id方式
        elif ":id/" in controlinfo or ":string/" in controlinfo:
            element = self._driver.find_element_by_id(controlinfo)
        else:
            # 若参数没有特点
            try:
                # 先尝试name方式
                element = self._driver.find_element_by_name(controlinfo)
            except:
                # 再尝试class name 方式
                logging.debug("不能通过name定位，尝试class name")
                element = self._driver.find_element_by_class_name(controlinfo)
        #logging.debug("已通过"+controlinfo+"定位到")

        return element
    # 使用示范
    '''
    no1 = UiHelper.find_element("com.android.contacts:id/menu_add_contact")--------通过ID
    no2 = UiHelper.find_element(u"姓名")--------通过控件文本 name
    no3 = UiHelper.find_element("android.widget.EditText")--------通过控件类名class name
    no4 = UiHelper.find_element("//andorid.widget.FrameLayout[0]/android.view.View[0]")--------通过控件绝对路径 xpath 
    '''

    def find_element_in_parent(self, parentelement, childelementinfo):
        element = ''
        if childelementinfo.startswith("//"):
            element = parentelement.find_element_by_xpath(childelementinfo)
        elif ":id/" in childelementinfo:
            element = parentelement.find_element_by_id(childelementinfo)
        else:
            # 若参数没有特点
            try:
                # 先尝试name方式
                element = parentelement.find_element_by_name(childelementinfo)
            except:
                # 再尝试class name 方式
                logging.debug("不能通过name定位，尝试class name")
                element = parentelement.find_element_by_class_name(childelementinfo)

        # logging.debug("已通过" + childElementInfo + "定位到")
        return element
    # 使用示范
    '''
    Parent = UiHelper.find_element("com.XXXX.XX:id/listItem")
    statusText = uiHelper.find_element_in_parent(Parent, "com.XXXX.XX:id:/status")
    '''
# 等待方法的封装
    def wait_for_element(self, elementinfo, period):
        for i in range(0, period):
            time.sleep(1)
            try:
                self.find_element(elementinfo)
                return
            except:
                continue
        raise Exception("已超时%d秒，找不到%s" % (period, elementinfo))

    def gotoHandles(self):
        # 切入handles
        handles = self._driver.window_handles
        for i in range(len(handles)):
            print('正在切入第%s个句柄' % i)
            self._driver.switch_to.window(handles[i])
            if self._driver.title == '建发房产钻石会':
                print('已进入正确句柄')
                break
            else:
                print('进入错误的句柄，请重新选择！')
'''
# 推荐使用WebDriverWait等待方法类
# Until方法在条件得到满足时，就会中断等待
# untiL_not方法在条件不满足时，中断等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#do something then wait for an element shown
WebDriverWait(self._driver,10).until(EC.invisibility_of_element_located(By.ID,"com.android.xx.xx.xx"))

'''




# 调试
# u = UiHelper(configpath='..\data\environment_RedmiNote3.txt')
# u.init_driver()
# time.sleep(3)
# # u.quit_driver()


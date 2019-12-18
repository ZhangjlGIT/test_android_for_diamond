# -*- coding:utf-8 _*-
# 示例：调试脚本
"""
@author:zhangjianlang
@file: OpenWechat.py
@time: 2019/7/25 16:49
"""

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {
    # 操作系统
    'platformName': 'Android',
    # 手机系统版本
    'platformVersion': '7.1.2',
    # 设备名
    # 华为mate10:安卓9，UYT0218206007614
    # 安卓虚拟机：安卓5.1.1，127.0.0.1:62001
    # 红米：安卓6.0.1，3e581162
    # 魅族：安卓7，79BQADSNZ5YGP
    'deviceName': '192.168.1.230:5555',
    # 被测应用程序的包名
    'appPackage': 'com.tencent.mm',
    # 被测应用程序启动的Activity名称
    'appActivity': '.ui.LauncherUI',
    # appium1.7以后的版本支持Uiautomator2
    # 'automationName': 'Uiautomator2',
    'automationName': 'Appium',
    # 需要输入中文时，请配置unicodeKeyboard和resetKeyboard，用于屏蔽软键盘
    # 乱码时，加入编码：#--coding:gb18030--
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    # 在appium中context的切换时，识别webview的时候,
    # 把com.tencent.mm:tools的webview识别成com.tencent.mm的webview. 从而导致context切换失败
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
    # 'androidProcess': 'com.tencent.mm:tools','args': ['--no-sandbox']
    }
# appium服务器地址
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
l = get_size()
x = int(l[0]) # x = 1080
y = int(l[1])


def swipeUp(t):
    x1 = int(x * 0.5)
    y1 = int(y * 0.75)
    y2 = int(y * 0.25)
    print('向上移动')
    driver.swipe(x1, y1, x1,y2, t)




# 聊天界面 点击公众号（事先顶置公众号在第一行，或通过搜索公众号进入）
driver.find_element_by_xpath("//android.view.View[@text='房产信息化服务']").click()
driver.implicitly_wait(10)

# 点击菜单 进入钻石会
driver.find_element_by_xpath("//android.widget.TextView[@text='进入钻石会']").click()
driver.implicitly_wait(10)
time.sleep(5)

# 切入公众号webview
print(driver.contexts)
time.sleep(10)
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')  # 切入 webview
time.sleep(5)
# 打印页面handles
handles = driver.window_handles
driver.switch_to.window(handles[0])
time.sleep(5)

# 判断是否有 广告弹窗
try:
    driver.find_element_by_id("close_ad_mask").click()
    print('关闭广告弹窗')
except:
    print('不存在广告弹窗')
    pass
    time.sleep(5)


swipeUp(1000)


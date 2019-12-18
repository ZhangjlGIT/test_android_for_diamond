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
    'platformVersion': '6.0.1',
    # 设备名
    # 华为mate10:安卓9，UYT0218206007614
    # 安卓虚拟机：安卓5.1.1，127.0.0.1:62001
    # 红米：安卓6.0.1，3e581162
    # 魅族：安卓7，79BQADSNZ5YGP
    'deviceName': '3e581162',
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

def swipedown(driver, t=500, n=1):
    # 向下滑动屏幕
    l = driver.get_window_size()
    x1 = l['width'] * 0.5          # x坐标
    y1 = l['height'] * 0.25        # 起始y坐标
    y2 = l['height'] * 0.75         # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)

# 向下滑动
# swipedown(driver)
driver.implicitly_wait(10)

# 定位搜索框
#driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tencent.mm:id/jb']").click()
#time.sleep(3)

# 显性等待 每隔0.3秒调用，最长等待10秒
# locator = (By.ID, "com.tencent.mm:id/l3")
# WebDriverWait(driver, 10, 0.3).until(EC.presence_of_element_located(locator), "已经超时找不到元素")
#driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tencent.mm:id/l3' and @text='搜索']").send_keys('钻石会测试')
driver.implicitly_wait(10)
# 回车
#driver.keyevent(4)
#driver.implicitly_wait(10)


# 点击 钻石会公众号
# driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/qm' and @text='钻石会测试']").click()
# driver.implicitly_wait(10)

# 聊天界面 点击公众号（事先顶置公众号在第一行）
driver.find_element_by_xpath("//android.view.View[@text='钻石会测试']").click()
driver.implicitly_wait(10)

# 点击菜单 进入钻石会
driver.find_element_by_xpath("//android.widget.TextView[@text='进入钻石会']").click()
driver.implicitly_wait(10)
time.sleep(10)

# 此步骤用于调试，请注意打开debugx5.qq.com设置：信息->TBS setting->打开TBS内核 inspector调试功能
contexts = driver.contexts
print(driver.contexts)
# ['NATIVE_APP', 'WEBVIEW_com.tencent.mm:tools', 'WEBVIEW_com.tencent.mm:toolsmp']  #所有页面的context


print(driver.current_context)  # 打印当前页面的context,应为NATIVE_APP
# print('第一个页面源文件：%s' % driver.page_source)  # 打印 页面源文件
time.sleep(5)

# 切入公众号webview
driver.switch_to.context(contexts[1])# 切入 webview
time.sleep(5)

print(driver.current_context)  # 打印当前页面的context,应为 WEBVIEW_com.tencent.mm:toolsmp
# print('第二个页面源文件：%s' % driver.page_source)  # 打印 页面源文件
time.sleep(5)

# 打印页面handles
handles = driver.window_handles
print(handles)
# ['CDwindow-DEEF60AA07EE8BF56FFB15460F6D66F7', 'CDwindow-DFBD71868144287C73C32E6AC4AA399F']

driver.switch_to.window(handles[1])
print('handles[1]页面源文件：%s' % driver.page_source)  # 打印 页面源文件
time.sleep(5)

# 判断是否有 广告弹窗
# if driver.find_element_by_id('close_ad_mask').is_displayed():
#     driver.find_element_by_id("close_ad_mask").click()
# else:
#     print('不存在广告弹窗')
#     pass
try:
    # driver.find_element_by_id("close_ad_mask").click()
    driver.find_element_by_xpath('//*[@id="close_ad_mask" and @src="/default/Index/img/vip/close_ad.png"]').click()
except:
    print('不存在广告弹窗')
    pass
time.sleep(3)

# 签到
# 点击菜单 购房服务
driver.find_element_by_xpath('//*[@id="nav_bar"]/div[1]/div/div[4]').click()
# driver.find_element_by_xpath("//android.widget.Image[@text='gffw']").click()
print('点击购房服务 ')
driver.implicitly_wait(20)

# 切入 handles
driver.switch_to.window(handles[1])
print('页面源文件：%s' % driver.page_source)  # 打印 页面源文件

# 点击菜单 热销楼盘
# driver.find_element_by_link_text('热销楼盘').click()
# class_text = 'className("android.view.View").text("热销楼盘")'
# driver.find_element_by_android_uiautomator(class_text).click()
class_text = 'className("android.view.View").text("热销楼盘")'
driver.find_element_by_android_uiautomator(class_text).click()
driver.find_element_by_android_uiautomator()
time.sleep(5)
print('pass')




# try:
#      # 点击 关闭
#     driver.find_element_by_xpath("//android.widget.Image[@resource-id='close_ad_mask' and @text='close_ad']").click()
#     print('关闭弹窗')
#     time.sleep(5)
# except:
#     driver.implicitly_wait(10)

# 主页
# 判断是否有 定位弹窗
# if self.uiHelper.find_element('com.tencent.mm:id/dcf'):
#     # 点击 是
#     self.uiHelper.find_element('com.tencent.mm:id/b1v').click()
#     time.sleep(5)
# else:
#     pass
# time.sleep(5)

# 判断是否有 广告弹窗
# if self.uiHelper.find_element('android.view.View'):
#     # 点击 关闭
#     self.uiHelper.find_element('close_ad_mask').click()
#     time.sleep(5)
# else:
#     pass
# driver.implicitly_wait(50)

# driver.find_element_by_accessibility_id('com.tencent.mm:id/qh').click()
# time.sleep(2)
# # 输入
# driver.find_element_by_class_name('com.tencent.mm:id/lh').send_keys('钻石会测试')
# time.sleep(2)
# # 回车
# driver.keyevent(4)
# time.sleep(2)
# # 点击查询结果
# driver.find_element_by_id('com.tencent.mm:id/om').click()
# time.sleep(2)
# # 进入钻石会
# driver.find_element_by_id('com.tencent.mm:id/aiu').click()




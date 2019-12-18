# -*- coding:utf-8 _*-
"""
@author:zhangjianlang
@file: goinMainPage.py
@time: 2019/9/20 17:24
"""
import time


# 进入公众号首页
def gotoMainPage(self, driver):
    # 聊天界面 点击公众号（事先顶置公众号在第一行，或通过搜索公众号进入）
    driver.find_element_by_xpath("//android.view.View[@text='建发房产信息化服务']").click()
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

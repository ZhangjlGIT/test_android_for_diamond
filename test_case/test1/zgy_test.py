# -*- coding:utf-8 _*-
"""
# 功能：打开公众号->打开热销楼盘-->查询
# 作者     :zenggy
# 创建时间 :2019/8/23  16:00
# 文件     :test2_2_1_1_3.PY
# IDE      :PyCharm
"""
from test_case.models import myunit
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import warnings  # 警告


class testcase(myunit.MyTest):
    """热门服务"""
    def test1(self):
        """进入热销楼盘--查询"""
        # 连接手机
        warnings.simplefilter("ignore", ResourceWarning) # 忽略报错
        self.imgs = []  # 截图列表
        driver = self.uiHelper._driver
        time.sleep(10)

        #---------------------------------------------------测试用例------------------------------------------

        # 聊天界面 点击公众号（事先顶置公众号在第一行，或通过搜索公众号进入）
        driver.find_element_by_xpath("//android.view.View[@text='房产信息化服务']").click()
        driver.implicitly_wait(10)
        time.sleep(10)
        #
        # 点击菜单 进入钻石会
        driver.find_element_by_xpath("//android.widget.TextView[@text='进入钻石会']").click()
        driver.implicitly_wait(10)
        time.sleep(5)
        print('test1')
        #
        # 此步骤用于调试，请注意打开 debugx5.qq.com设置：信息->TBS setting->打开TBS内核 inspector调试功能
        print(driver.contexts)
        # ['NATIVE_APP', 'WEBVIEW_com.tencent.mm:tools', 'WEBVIEW_com.tencent.mm:toolsmp']  #所有页面的context

        # 切入公众号webview
        driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')  # 切入 webview
        time.sleep(10)
        print('test3')

        print(driver.current_context)  # 打印当前页面的context,应为 WEBVIEW_com.tencent.mm:toolsmp
        # print('打印页面源文件：%s' % driver.page_source)  # 打印 页面源文件
        time.sleep(15)
        # print('test5')
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
        time.sleep(10)

        driver.find_element_by_link_text('热销楼盘').click()
        time.sleep(15)
        print('进入热销楼盘')
        print(driver.window_handles)
        driver.switch_to.window(driver.window_handles[0])  # 切换到新开页面
        #print(driver.page_source)
        time.sleep(10)

        # driver.switch_to.window(driver.window_handles[1])  # 切换到新开页面
        # print(driver.page_source)
        # time.sleep(10)
        #driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]]').click()
        driver.find_element_by_class('查找我的意向楼盘').click()
        time.sleep(2)
        print('选择输入框')
        driver.find_element_by_class('查找我的意向楼盘').send_keys('中央天成')
        time.sleep(2)
        print('输入中央天成')
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="sou"]/span').click()
        time.sleep(15)
        print('搜索中央天成')
        driver.find_element_by_xpath('//*[@id="datalist"]/ul').click()#点击对应楼盘
        time.sleep(10)

 # 检查点
        result=driver.title# 获取title
        print(result)
        self.assertEqual(result, '中央天成', '查询不到')  # 检查点


if __name__ == '__main__':
    unittest.main()

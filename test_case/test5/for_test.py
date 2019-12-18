# _*_coding:utf-8_*_
"""
#作者：zzl
#创建时间：2019/8/27
#文件：test1_4_slide
"""
from test_case.models import myunit
import time


class testcase(myunit.MyTest):
    """测试用例说明，如首页"""
    def test1(self):
        """进入简介"""
        # 连接手机
        self.imgs = []  # 截图列表
        driver = self.uiHelper._driver
        time.sleep(10)

        # Screen_size = driver.get_size()
        #
        def get_size():
            x = driver.get_window_size()['width']
            y = driver.get_window_size()['height']
            return (x, y)

        l = get_size()
        x = int(l[0])  # x = 1080
        y = int(l[1])

        def swipeUp(t):
            x1 = int(x * 0.5)
            y1 = int(y * 0.75)
            y2 = int(y * 0.25)
            print('向上移动')
            driver.swipe(x1, y1, x1, y2, t)


        #---------------------------------------------------测试用例------------------------------------------

        # 聊天界面 点击公众号（事先顶置公众号在第一行，或通过搜索公众号进入）
        driver.find_element_by_xpath("//android.view.View[@text='房产信息化服务']").click()
        driver.implicitly_wait(10)

        # 点击菜单 进入钻石会
        driver.find_element_by_xpath("//android.widget.TextView[@text='进入钻石会']").click()
        driver.implicitly_wait(10)
        time.sleep(5)

        # 切入公众号webview
        driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')  # 切入 webview
        time.sleep(5)

        # print(driver.current_context)  # 打印当前页面的context,应为 WEBVIEW_com.tencent.mm:toolsmp
        # print('第二个页面源文件：%s' % driver.page_source)  # 打印 页面源文件
        # time.sleep(5)

        # 打印页面handles
        handles = driver.window_handles
        #print(handles)
        # ['CDwindow-DEEF60AA07EE8BF56FFB15460F6D66F7', 'CDwindow-DFBD71868144287C73C32E6AC4AA399F']

        driver.switch_to.window(handles[0])
        #print('handles[1]页面源文件：%s' % driver.page_source)  # 打印 页面源文件
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

import time
import os
from selenium import webdriver


def openReport(path):# path 为路径
    # 浏览器打开报告test_report.html
    # base_url = "http://localhost:1024/test_report.html"
    base_url = path + "/report/test_report.html"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    time.sleep(3)
    # 生成历史截图
    now = time.strftime("%Y%m%d%H%M%S")
    history_png = path + '/report/picture/' + now + '.png'
    driver.get_screenshot_as_file(history_png)

    # 判断是否已存在 test_report.png ，若存在则删除，保持test_report.png 为最新
    if os.path.exists(path + '/report/picture/test_report.png'):
        os.remove(path + '/report/picture/test_report.png')
        # print("test_report.png已删除")
    else:
        # print("test_report.png不存在")
        pass

    # 生成最新截图
    time.sleep(3)
    new_png = path + '/report/picture/test_report.png'
    driver.get_screenshot_as_file(new_png)


if __name__ == '__main__':
    openReport(r'D:\project\test_android_for_diamond')

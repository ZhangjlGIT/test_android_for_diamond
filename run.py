#-*-coding:utf-8-*-

# data 存放测试相关的数据
# report 存放html测试报告，底下image目录 存放测试过程中截图
# test_case 测试用例目录
# test_case/models 存放一些公共函数级公共类
# test_case/models 存放以“*Page.py”命名的测试用例的封装页面对象文件

from public.HTMLTestRunner_cn import HTMLTestRunner
from public.OpenNewReport import openReport
from public.send_email import sendEmail
from public.StartReportServer import startserver
import unittest
import os

current_path = os.path.dirname(__file__)  # 脚本目录
test_dir = "./test_case"
# 定义测试报告的目录
test_report = "./report"
# 测试用例
# 执行顺序 根据ASCII 码，0~9,A~Z,a~z
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test5*.py')

if __name__ == "__main__":
    # 定义报告存放路径
    filename = test_report + '/' + 'test_report.html'
    # retry，指定重试次数，
    # save_last_try 为True ，一个用例仅显示最后一次测试的结果
    # save_last_try 为False，则显示所有重试的结果
    runer = HTMLTestRunner(title="移动端（钻石会）自动化测试报告",
                           description="用例执行情况",
                           stream=open(filename, "wb"),
                           retry=3,
                           verbosity=2,
                           save_last_try=True)

    runer.run(discover)

    # 打开报告
    openReport(current_path)
    # 发送报告
    sendEmail(current_path, receivers=None)
    # 打开服务
    startserver(current_path)



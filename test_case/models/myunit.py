#自定义测试框架类1
#统一设置 setUp() 与 tearDown() 的实现

from public import UiHelper
from public import Adb_devices
import unittest
import traceback
import logging
import time
import os


# 路径
d = os.path.dirname(__file__)# 当前运行文件的目录
parent_path = os.path.dirname(d) # d 的父级目录
parent_path = os.path.dirname(parent_path)# parent_path 的父级目录
# configpath = parent_path + '\data\environment_RedmiNote3.txt'
configpath = parent_path + '\data\environment_xiaomi.txt'
# configpath = parent_path + '\data\environment_huaweimate10.txt'


class MyTest(unittest.TestCase):
    # 日志配置
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    # 创建实例
    # uiHelper = UiHelper.UiHelper('..\data\environment_huaweimate10.txt')
    # uiHelper = UiHelper.UiHelper('..\data\environment_RedmiNote3.txt')
    # uiHelper = UiHelper.UiHelper('..\data\environment.txt')
    uiHelper = UiHelper.UiHelper(configpath)

    def setUp(self):
        # 执行用例前，初始化
        print('{:*^40}'.format('开始运行'))
        Adb_devices.lookforDevices()  # 检查手机是否连接
        try:
            # 连接appium
            # 调用 UiHelper类 中 init_driver（连接appium）的方法
            self.uiHelper.init_driver()
            # uiHelper.enableWifiOnly()
        except:
            # 调用 UiHelper类 中 quit_driver（关闭连接appium）的方法
            self.uiHelper.quit_driver()
            # 异常栈以字符串的形式返回
            exstr = traceback.format_exc()
            self.logger.log(self, exstr)
            self.logger.log(self, "初始化失败")
            self.fail("")

    def tearDown(self):
        # 执行完用例，还原环境
        try:
            self.uiHelper.quit_driver()
            print('{:*^40}'.format('运行完成'))
        except:
            pass



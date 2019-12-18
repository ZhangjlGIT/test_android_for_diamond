# -*- coding:utf-8 _*-
"""
@author:zhangjianlang
@file: AndrpidScreenshot.py
@time: 2019/8/27 11:31
"""

import subprocess
from public.ChangeToBs64 import picToBs64
import os

current_path = os.path.dirname(__file__)
parent_path = os.path.dirname(current_path)
picture_path = parent_path + r"/report/picture"  # 保存图片的目录

class Screenshot():  # 截取手机屏幕并保存到电脑
    # def __init__(self):
        # 查看连接的手机
        # connect = subprocess.Popen("adb devices", stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        # stdout, stderr = connect.communicate()  # 获取返回命令
        # # 输出执行命令结果结果
        # stdout = stdout.decode("utf-8")
        # stderr = stderr.decode("utf-8")
        # print(stdout)
        # print(stderr)

    def screen(self):  # 在手机上截图
        cmd = r"adb shell /system/bin/screencap -p /sdcard/test.png" # 命令1：在手机上截图 test.png为图片名
        screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screenExecute.communicate()
        # 输出执行命令结果结果
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        # print(stdout)
        # print(stderr)

    def saveComputer(self):  # 将截图保存到电脑

        # 命令2：将图片保存到电脑 /report/picture
        cmd = r"adb pull /sdcard/test.png " + picture_path
        screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = screenExecute.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        # 输出执行命令结果结果
        stdout = stdout.encode("utf-8")
        stderr = stderr.encode("utf-8")
        # print(stdout)
        # print(stderr)

    def executeScreenshot(self):   # 调用 screen saveComputer
        screen = Screenshot()
        screen.screen()
        screen.saveComputer()
        # 将图片png 转换成bs4格式，便于显示在报告中
        dir = picture_path
        bs64Code = picToBs64(dir, "test.png", 'memory_pic')
        print('{:#^20}'.format('截图成功'))

        return bs64Code


if __name__ == '__main__':
    screen = Screenshot()
    screen.executeScreenshot()


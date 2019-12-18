# -*- coding:utf-8 _*-
"""
@author:zhangjianlang
@file: test.py
@time: 2019/9/16 20:20
"""

import os

# popen返回文件对象，跟open操作一样
f = os.popen(r"adb devices", "r")
out = f.read()
f.close()

# print(out)  # cmd输出结果

# 输出结果字符串处理
s = out.split("\n")   # 切割换行
new = [x for x in s if x != '']  # 去掉空''
# print(new)

# 可能有多个手机设备
devices = []  # 获取设备名称
for i in new:
    dev = i.split('\tdevice')
    if len(dev) >= 2:
        devices.append(dev[0])

if not devices:
    print("没有手机连上")
else:
    print("当前手机设备:%s"%str(devices))

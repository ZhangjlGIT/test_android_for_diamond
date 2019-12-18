# -*- coding:utf-8 _*-
"""
@author:zhangjianlang
@file: StartReportServer.py
@time: 2019/9/19 11:12
"""

import os

def startserver(parent_path):
    # current_path = os.path.dirname(__file__)  # 脚本目录
    # parent_path = os.path.dirname(current_path)  # 上级目录，即项目根目录
    goto_report = 'cd ' + parent_path + r"/report"  # 报告目录
    # 打开服务
    cmd = 'd:' + '&&' + goto_report + '&&' + 'python -m http.server 1024'
    os.system(cmd)
    # os.system('d: && cd D:/project/test_android_for_diamond/report && python -m http.server 1024')


if __name__ == "__main__":
    startserver()

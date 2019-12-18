# -*- coding:utf-8 _*-
"""
@author:zhangjianlang
@file: ChangeToBs4.py
@time: 2019/9/18 16:16
"""

import os
import base64


def picToBs64(dir, picture_name, py_name):
    # current_path = os.path.realpath(__file__)
    # current_dir = os.path.split(current_path)[0]
    # 最后的文件名
    # filename = picture_name.replace('.', '_')
    write_data = []
    with open('{}/{}'.format(dir, picture_name), 'rb') as f:
        b64str = base64.b64encode(f.read())
        s = b64str.decode()
        # 注意这边b64str一定要加上.decode()
        # write_data.append('%s = "%s"\n' % (filename, b64str.decode()))
        write_data.append('%s' % s)
    write_data = write_data[0]
    # print(write_data)

    # # 写入 xxx.py 文件,用于保存
    # f = open('{}.py'.format(py_name), 'w+')
    # for data in write_data:
    #     f.write(data)
    # f.close()
    return write_data


if __name__ == '__main__':
    pics = "test.png"
    picToBs64(pics, 'memory_pic')
    print("转换成功")

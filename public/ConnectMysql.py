# -*- coding:utf-8 _*-
"""
@author:zhangjianlang
@file: ConnectMysql.py
@time: 2019/9/20 11:14
"""

import pymysql
import traceback
from time import sleep


class PyMySQL(object):
    def __init__(self, host, user, pwd, db):
        # 创建连接
        self.conn = pymysql.connect(host, user, pwd, db)
        # 使用cursor() 创建游标，用于获取结果
        self.cursor = self.conn.cursor()
    # 建表
    def create_table_func(self, create_table):
        self.cursor.execute(create_table)
        print('数据表创建完毕')

    # 插入
    def insert_date(self, insert):
        try:
            self.cursor.execute(insert)
            self.conn.commit()
        except:
            print(traceback.format_exc())
            self.conn.rollback()

    # 更新
    def update_data(self, update):
        try:
            self.cursor.execute(update)
            self.cursor.commit()
        except:
            print(traceback.format_exc())
            self.conn.rollback()

    # 删除
    def delete_data(self, delete):
        try:
            self.cursor.execute(delete)
            self.conn.commit()
        except:
            print(traceback.format_exc())
            self.conn.rollback()

    # 查询
    def select_data(self, select):
        self.cursor.execute(select)

        all_data = self.cursor.fetchall()
        for i in all_data:
            print('查询结果为：{}'.format(i))

    # 执行sql
    def execute_yoursql(self, yoursql):
        try:
            self.cursor.execute(yoursql)
            self.conn.commit()
        except:
            print(traceback.format_exc())
            self.conn.rollback()


if __name__ == '__main__':
    my = PyMySQL('172.22.242.20', 'root', 'softcnd123456', 'witeye_dev')
    # my.create_table_func()
    # my.insert_date()
    # my.update_data()
    # my.delete_data()
    # my.select_data()
    my.execute_yoursql('select * from tb_person')


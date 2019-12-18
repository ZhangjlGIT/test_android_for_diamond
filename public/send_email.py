#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.multipart import MIMEMultipart

def sendEmail(path, receivers):
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "245704787@qq.com"  # 用户名
    mail_pass = "aetrnbottkfqcaee"  # 口令

    sender = '245704787@qq.com'
    if receivers is None:
        receivers = '<15305022312@163.com>;<245704787@qq.com>'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    msgRoot = MIMEMultipart()
    msgRoot['From'] = Header("自动化测试系统", 'utf-8')
    msgRoot['To'] = receivers
    # 主题
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    subject = now + '自动化测试报告'
    content = now + '<html><h1>钻石会自动化测试报告</h1><h2>' \
                    '</h2><h3>点击下图跳转至报告详情</h3><h4>(或下载附件html和json，再通过本地浏览器打开)</h4></html>'
    msgRoot['Subject'] = Header(subject, 'utf-8')

    # html
    # content  = '<a href="http://172.22.12.194:1024/test_report.html">点击查看报告详情</a>'
    # 启动本地服务
    # os.system(r"cd C:\Users\Administrator\PycharmProjects\test_menber\report &python -m http.server 1024")
    msgText = MIMEText(content, 'html', 'utf-8')
    msgRoot.attach(msgText)
    # 显示图片
    content = '<a href="http://172.22.12.194:1024/test_report.html"><img src="cid:0" alt="test_report" /></a><br>'
    msgText = MIMEText(content, 'html', 'utf-8')
    msgRoot.attach(msgText)


    # 构造附件
    att1_path = path + '/report/test_report.html'
    att1 = MIMEText(open(att1_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msgRoot.attach(att1)

    json_path = path + '/report/test_report.json'
    att2 = MIMEText(open(json_path, 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="test_report.json"'
    msgRoot.attach(att2)

    # 附件图片
    pic_path = path + "/report/picture/test_report.png"
    img = MIMEImage(open(pic_path, 'rb').read(), _subtype='octet-stream')
    img.add_header('Content-Disposition', 'attachment', filename=pic_path)
    img.add_header('Content-ID', '<0>')  # 增加编号，HTML中通过引用 src="cid:0",可以引用附件
    img.add_header('X-Attachment-Id', '0')
    msgRoot.attach(img)

    try:
        smtp = smtplib.SMTP_SSL(mail_host)
        smtp.connect(mail_host, port=465)
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(sender, receivers, msgRoot.as_string())
        print(subject+'>>>>>>邮件发送成功')
        smtp.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误


if __name__ == "__main__":
    sendEmail(path=r'D:\project\test_android_for_diamond', receivers=None)

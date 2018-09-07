#!/usr/bin/python3
# -*- coding: utf-8 -*-

import smtplib
import traceback
import time,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# def sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password):
   
    # @subject:邮件主题
    # @msg:邮件内容
    # @toaddrs:收信人的邮箱地址
    # @fromaddr:发信人的邮箱地址
    # @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    # @password:发信人的邮箱密码
    
    # mail_msg = MIMEMultipart()
    # if not isinstance(subject,unicode): #过滤或者不过滤貌似没啥影响
    #     subject = unicode(subject, 'utf-8')
    # mail_msg['Subject'] = subject
    # mail_msg['From'] =fromaddr
    # mail_msg['To'] = ','.join(toaddrs)
    # # mail_msg.attach(MIMEText(msg, 'plain', 'utf-8')) #f发送文本文件
    # mail_msg.attach(MIMEText(msg, 'html', 'utf-8')) #发送html格式邮件
    # try:
    #     s = smtplib.SMTP()
    #     s.connect(smtpaddr)  #连接smtp服务器
    #     s.login(fromaddr,password)  #登录邮箱
    #     s.sendmail(fromaddr, toaddrs, mail_msg.as_string()) #发送邮件
    #     s.quit()
    #     print ("邮件发送成功！")
    # except Exception as e:
    #    print ("Error: unable to send email",traceback.format_exc())
       

def send_mail_html():
	#sendaddr
	sender = '156064710@qq.com'

	#receiver
	receiver = 'maijh@sectc.cn'

	#subject
	t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	subject = '自动化测试结果_' + t

	smtpserver = 'smtp.qq.com'

	username = '156064710@qq.com'
	password = 'ebavjkbpiqfxbjjj'

	msg = MIMEMultipart()
# ..\\Runner\\result.html'

	# filecwd = os.path.dirname(os.getcwd())
	filecwd = (os.path.dirname(os.getcwd())+'\\reports\\result.html')
	f = open(filecwd,'rb')
	mail_body = f.read()
	# print(mail_body)
	f.close()

	# 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
	att1 = MIMEText(mail_body, _subtype='base64', _charset='gb2312')
	att1["Content-Type"] = 'application/octet-stream'
	att1["Content-Disposition"] = 'attachment; filename="report.html"'
	msg.attach(att1)


	msg['Subject'] = Header(subject, 'utf-8')
	msg['From'] = sender
	msg['To'] = receiver

	try:
		smtp = smtplib.SMTP()
		smtp.connect(smtpserver)
		smtp.login(username, password)
		smtp.sendmail(sender, receiver, msg.as_string())
	except:
		print("邮件发送失败！")
	else:
		print("邮件发送成功！")
	finally:
		smtp.quit()

# if __name__ == '__main__':
# 	# filecwd = os.path.dirname(os.getcwd())
# 	send_mail_html()
	
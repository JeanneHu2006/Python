import smtplib
from email.mime.text import MIMEText  # 文本类型的邮件，用来构造邮件
from email.header import Header  # 用来构造邮件的头部
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart  # 用来构造附件

s = smtplib.SMTP()
host = 'smtp.163.com'
port = 25
s.connect(host, port)
mail_user =input('请输入发件人邮箱：')            #'BigHu2006@163.com'
mail_pass =input('请输入授权码：')  #'AKAEUNCQSDLTPLDL'
s.login(user=mail_user, password=mail_pass)

content = '测试发送邮件'
mail_receiver =input('请输入收信人邮箱：')
textcontent = MIMEText(content, _charset='utf-8')
msg = MIMEMultipart()
msg.attach(textcontent)
msg['From'] = mail_user
msg['To'] = mail_receiver


s.sendmail(from_addr=mail_user, to_addrs=mail_receiver, msg=msg.as_string())
"""发送报告至邮箱"""
import smtplib, datetime
from email.mime.text import MIMEText
from email.header import Header


class Mail:
    def __init__(self):
        self.smtp_server = "smtp.qq.com"         # SMTP服务器地址
        self.smtp_port = 465                     # SMTP服务器端口
        self.account = "1051910384@qq.com"         # 发送邮件的邮箱地址
        self.password = "mpeskxpfvgphbbdi"          # 邮箱授权码
        self.recipient = '2439409285@qq.com'    # 收件人邮箱地址

    def send(self, text):
        subject = '银证测试日报{}'.format(datetime.time)  # 邮箱主题
        content = str(text)  # 邮箱内容
        message = MIMEText(content, 'plain', 'utf-8')
        # 发送邮箱标题
        message['From'] = self.account
        message['To'] = self.recipient
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpobj = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            smtpobj.login(self.account, self.password)  # 登录邮箱
            smtpobj.sendmail(self.account, self.recipient, message.as_string())  # 发送内容
            smtpobj.quit()
            print('发送邮箱成功！！')
        except smtplib.SMTPException as E:
            print(E.__traceback__.tb_lineno, E)
            print('邮件发送失败！！')


# if __name__ == 'main':
#     Mail = Mail(
#     Mail.send('邮箱发送验证')
print(Mail().send("邮箱发送验证"))

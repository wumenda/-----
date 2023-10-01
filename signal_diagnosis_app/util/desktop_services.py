from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

class DesktopServices:
    @staticmethod
    def open_file(file_path):
        # 打开文件
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

    @staticmethod
    def open_url(url):
        # 打开网页
        QDesktopServices.openUrl(QUrl(url))

    @staticmethod
    def open_directory(dir_path):
        # 打开文件夹
        QDesktopServices.openUrl(QUrl.fromLocalFile(dir_path))

    @staticmethod
    def open_email(email_address, subject="", body=""):
        # 打开默认邮件客户端发送邮件
        url = f"mailto:{email_address}?subject={subject}&body={body}"
        QDesktopServices.openUrl(QUrl(url))
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 创建菜单项处理类

        self.menu_handler = MenuHandler()

        # 设置菜单栏和菜单项
        self.setup_menu_bar()

    def setup_menu_bar(self):
        menu_bar = self.menuBar()

        # 创建文件菜单
        file_menu = menu_bar.addMenu("文件")

        # 创建打开菜单项
        open_action = QAction("打开", self)
        file_menu.addAction(open_action)

        # 创建保存菜单项
        save_action = QAction("保存", self)
        file_menu.addAction(save_action)

        # 创建菜单项处理类
        

        # 将菜单项的 triggered 信号连接到处理类的槽函数
        open_action.triggered.connect(self.menu_handler.open_file)
        save_action.triggered.connect(self.menu_handler.save_file)

class MenuHandler(QObject):
    @pyqtSlot()
    def open_file(self):
        # 打开文件逻辑
        print("执行打开文件操作")

    @pyqtSlot()
    def save_file(self):
        # 保存文件逻辑
        print("执行保存文件操作")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QGridLayout, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt

from signal_diagnosis_app.components.common_items import CommonItems
from signal_diagnosis_app.components.feature_box import FeatureBox
from signal_diagnosis_app.components.signal_window import SignalPlotWidget
from signal_diagnosis_app.components.work_space import WorkSpace
from .file_browser import FileBrowser, FileWindow
from PyQt5 import QtGui
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from . import resource_rc
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("故障诊断工具箱")
        self.resize(900, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/svg/favicon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.setWindowIcon(icon)
        # 创建菜单项处理类
        self.menu_handler = MenuHandler()
        self.feature_box = FeatureBox(self)
        self.work_space = WorkSpace()
        self.setup_ui()

    def setup_ui(self):
        # 创建主窗口的中心部件，并设置布局
        central_widget = QWidget()
        layout = QHBoxLayout(central_widget)
        layout.addWidget(self.feature_box)
        layout.addWidget(self.work_space)
        # layout.setContentsMargins(0, 0, 0, 0)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 设置主窗口的菜单栏和工具栏
        self.setup_menu_bar()
        self.setup_tool_bar()

    def setup_menu_bar(self):
        menu_bar = self.menuBar()

        # 创建文件菜单
        file_menu = menu_bar.addMenu("文件")
        open_action = QAction("打开", self)
        file_menu.addAction(open_action)
        save_action = QAction("保存", self)
        file_menu.addAction(save_action)

        # 创建编辑菜单
        edit_menu = menu_bar.addMenu("编辑")
        cut_action = QAction("剪切", self)
        edit_menu.addAction(cut_action)
        copy_action = QAction("复制", self)
        edit_menu.addAction(copy_action)
        paste_action = QAction("粘贴", self)
        edit_menu.addAction(paste_action)

        # 创建选择菜单
        select_menu = menu_bar.addMenu("选择")
        select_all_action = QAction("全选", self)
        select_menu.addAction(select_all_action)
        clear_action = QAction("清除选择", self)
        select_menu.addAction(clear_action)

        # 创建查看菜单
        view_menu = menu_bar.addMenu("查看")
        zoom_in_action = QAction("放大", self)
        view_menu.addAction(zoom_in_action)
        zoom_out_action = QAction("缩小", self)
        view_menu.addAction(zoom_out_action)

        # 将菜单项的 triggered 信号连接到处理类的槽函数
        open_action.triggered.connect(self.menu_handler.open_file)
        save_action.triggered.connect(self.menu_handler.save_file)

    def setup_tool_bar(self):
        # 创建工具栏
        tool_bar = self.addToolBar("工具栏")

        # 创建工具栏按钮
        open_button = tool_bar.addAction("打开")
        save_button = tool_bar.addAction("保存")
        tool_bar.addSeparator()
        copy_button = tool_bar.addAction("复制")
        cut_button = tool_bar.addAction("剪切")
        paste_button = tool_bar.addAction("粘贴")

        tool_bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

class MenuHandler(QObject):
    @pyqtSlot()
    def open_file(self):
        # 打开文件逻辑
        print("执行打开文件操作")

    @pyqtSlot()
    def save_file(self):
        # 保存文件逻辑
        print("执行保存文件操作")
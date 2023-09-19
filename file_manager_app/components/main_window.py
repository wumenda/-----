from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from .file_browser import FileBrowser
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文件资源管理器")
        self.resize(800, 600)
        # 创建菜单项处理类
        self.menu_handler = MenuHandler()

        self.setup_ui()

    def setup_ui(self):
        # 创建文件浏览器
        file_browser = FileBrowser()

        # 创建主窗口的中心部件，并设置布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(file_browser)
        layout.setContentsMargins(0, 0, 0, 0)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # # 设置主窗口的菜单栏和工具栏
        # self.setup_menu_bar()
        # self.setup_tool_bar()

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
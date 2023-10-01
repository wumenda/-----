from PyQt5.QtWidgets import QMenu

class PopupMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_ui()

    def setup_ui(self):
        # 添加菜单项
        self.addAction("菜单项1")
        self.addAction("菜单项2")
        self.addSeparator()
        self.addAction("菜单项3")

        # 设置菜单项的信号槽连接
        self.triggered.connect(self.handle_action)

    def handle_action(self, action):
        # 处理菜单项的触发事件
        if action.text() == "菜单项1":
            print("菜单项1被触发")
        elif action.text() == "菜单项2":
            print("菜单项2被触发")
        elif action.text() == "菜单项3":
            print("菜单项3被触发")
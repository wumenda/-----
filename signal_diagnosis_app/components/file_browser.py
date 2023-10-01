import os
import shutil
from PyQt5.QtWidgets import QTreeView, QFileSystemModel, QHeaderView
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtCore import QObject, pyqtSlot
import sys
import subprocess
from PyQt5.QtWidgets import QTreeView, QMenu, QAction, QApplication, QGroupBox
from PyQt5.QtCore import QDir, QMimeData, Qt
from PyQt5.QtCore import QMimeData, QUrl
from PyQt5.QtCore import QModelIndex

class FileBrowser(QTreeView):
    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.setup_context_menu()

    def setup_ui(self):
        # 设置根目录
        root_path = ""

        # 创建文件系统模型
        self.model = QFileSystemModel()
        self.model.setRootPath(root_path)

        # 设置文件浏览器的模型和根索引
        self.setModel(self.model)
        self.setRootIndex(self.model.index(root_path))

        # # 设置文件浏览器的列宽自适应内容
        # self.header().setSectionResizeMode(QHeaderView.ResizeToContents)

        # 展开根节点
        self.expand(self.rootIndex())

        # 连接双击信号到槽函数
        self.doubleClicked.connect(self.open_file)

    def setup_context_menu(self):
        # 创建上下文菜单
        self.context_menu = QMenu(self)
        
        # 创建菜单项
        copy_action = QAction("复制", self)
        paste_action = QAction("粘贴", self)

        # 连接菜单项的信号到槽函数
        copy_action.triggered.connect(self.copy)
        paste_action.triggered.connect(self.paste)

        # 将菜单项添加到上下文菜单
        self.context_menu.addAction(copy_action)
        self.context_menu.addAction(paste_action)

    def contextMenuEvent(self, event):
        # 重写上下文菜单事件处理函数
        if self.indexAt(event.pos()).isValid():
            # 如果点击的位置有效（在项上），则显示上下文菜单
            self.context_menu.exec_(event.globalPos())

    def current_path(self):
        # 获取当前选择项的路径
        selected_index = self.selectionModel().currentIndex()
        return self.model.filePath(selected_index)

    def set_current_path(self, path):
        # 设置当前选择项的路径
        index = self.model.index(path)
        self.setCurrentIndex(index)
        self.scrollTo(index)
        self.expand(index)

    @pyqtSlot(QModelIndex)
    def open_file(self, index):
        # 获取双击的项的路径
        file_path = self.model.filePath(index)
        print("打开文件:", file_path)
        # 根据当前平台执行对应的命令
        if sys.platform == 'darwin':  # macOS
            subprocess.Popen(['open', file_path])
        elif sys.platform.startswith('linux'):  # Linux
            subprocess.Popen(['xdg-open', file_path])
        elif sys.platform == 'win32':  # Windows
            subprocess.Popen(['start', '', file_path], shell=True)
        else:
            print("不支持的操作系统平台")

    @pyqtSlot()
    def save_file(self):
        # 保存文件逻辑
        print("执行保存文件操作")

    @pyqtSlot()    
    def copy(self):
        # 实现复制功能
        source_path = self.current_path()

        # 创建剪贴板对象
        clipboard = QApplication.clipboard()

        # 创建 MIME 数据对象
        mime_data = QMimeData()

        # 将文件路径添加到 MIME 数据对象中
        url = QUrl.fromLocalFile(source_path)
        mime_data.setUrls([url])

        # 将 MIME 数据对象设置到剪贴板
        clipboard.setMimeData(mime_data)

    def paste(self):
        # 实现粘贴功能
        destination_path = self.current_path()

        # 创建剪贴板对象
        clipboard = QApplication.clipboard()

        # 从剪贴板中获取 MIME 数据对象
        mime_data = clipboard.mimeData()

        # 检查是否包含 URL 列表
        if mime_data.hasUrls():
            # 遍历 URL 列表
            for url in mime_data.urls():
                # 检查 URL 是否表示本地文件
                if url.isLocalFile():
                    # 获取文件路径
                    source_path = url.toLocalFile()
                    # 粘贴文件到目标位置
                    self.paste_file(source_path, destination_path)

    @pyqtSlot(str, str)
    def paste_file(self, source_path, destination_path):
        # 获取源文件名和目标文件名
        source_file_name = os.path.basename(source_path)
        destination_file_path = os.path.join(destination_path, source_file_name)

        # 检查目标文件是否已存在
        if os.path.exists(destination_file_path):
            print("目标文件已存在:", destination_file_path)
            return

        try:
            # 执行文件粘贴操作
            shutil.copy2(source_path, destination_file_path)
            print("粘贴文件:", destination_file_path)
        except Exception as e:
            print("粘贴文件时出现错误:", str(e))

class FileWindow(QGroupBox):
    def __init__(self, title):
        super().__init__(title)
        self.file_browser = FileBrowser()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.file_browser)
        

# 示例用法
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    file_browser = FileBrowser()
    file_browser.show()

    sys.exit(app.exec_())
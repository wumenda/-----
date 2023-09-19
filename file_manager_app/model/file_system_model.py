from PyQt5.QtWidgets import QFileSystemModel
from PyQt5.QtCore import QDir, Qt

class FileSystemModel(QFileSystemModel):
    def __init__(self):
        super().__init__()

        self.setFilter(QDir.AllEntries | QDir.NoDotAndDotDot)
        self.setRootPath(QDir.rootPath())
        self.setReadOnly(False)

    def flags(self, index):
        # 获取索引对应项的标志
        default_flags = super().flags(index)

        # 如果是文件夹，则添加可复制和可剪切的标志
        if self.isDir(index):
            return default_flags | Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsTristate

        return default_flags | Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled

    def setData(self, index, value, role=Qt.EditRole):
        # 设置索引对应项的数据
        if role == Qt.EditRole:
            return super().setData(index, value, role)

        return False
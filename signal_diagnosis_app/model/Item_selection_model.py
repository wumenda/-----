from PyQt5.QtCore import QItemSelectionModel

class ItemSelectionModel(QItemSelectionModel):
    def __init__(self, model):
        super().__init__(model)

    def select(self, index, command):
        # 选择项
        if command == QItemSelectionModel.Select:
            # 处理选择操作
            if index.isValid():
                # 设置索引为选中状态
                self.model().setData(index, True, Qt.CheckStateRole)
        elif command == QItemSelectionModel.Deselect:
            # 处理取消选择操作
            if index.isValid():
                # 设置索引为未选中状态
                self.model().setData(index, False, Qt.CheckStateRole)
        else:
            super().select(index, command)
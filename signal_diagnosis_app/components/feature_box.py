import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolBox, QVBoxLayout, QPushButton, QLabel, QStackedWidget


class FeatureBox(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.setMaximumWidth(300)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        tool_box = QToolBox()
    
        layout.addWidget(tool_box)

        page1 = QWidget()
        layout1 = QVBoxLayout()
        button1 = QPushButton("Button 1")
        layout1.addWidget(button1)

        button2 = QPushButton("Button 2")
        layout1.addWidget(button2)

        button3 = QPushButton("Button 3")
        layout1.addWidget(button3)
        page1.setLayout(layout1)
        tool_box.addItem(page1, "信号分析")

        page2 = QWidget()
        layout2 = QVBoxLayout()
        button1 = QPushButton("Button 1")
        layout2.addWidget(button1)

        button2 = QPushButton("Button 2")
        layout2.addWidget(button2)

        button3 = QPushButton("Button 3")
        layout2.addWidget(button3)
        page2.setLayout(layout2)
        tool_box.addItem(page2, "机器学习")

        page3 = QWidget()
        layout3 = QVBoxLayout()
        button1 = QPushButton("Button 1")
        layout3.addWidget(button1)

        button2 = QPushButton("Button 2")
        layout3.addWidget(button2)

        button3 = QPushButton("Button 3")
        layout3.addWidget(button3)
        page3.setLayout(layout3)
        tool_box.addItem(page3, "深度学习")

        # Add more pages...
        tool_box.currentChanged.connect(self.onPageChanged)

    def onPageChanged(self):
        index = self.sender().currentIndex()  # 获取当前选中页面的索引
        print(f"Page changed: {index}")
        self.ui.work_space.setCurrentIndex(index)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    feature_box = FeatureBox()
    feature_box.show()

    sys.exit(app.exec_())
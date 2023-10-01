from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QTextEdit, QStackedWidget,QWidget, QVBoxLayout,QLabel

from signal_diagnosis_app.components.signal_window import SignalPlotWidget

class WorkSpace(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("工作空间")  # 设置窗口标题
        # self.setGeometry(100, 100, 800, 600)  # 设置窗口位置和大小
        # self.setWindowOpacity(0.9)
        # 创建页面
        self.page1 = QWidget()
        layout1 = QVBoxLayout(self.page1)
        self.page1.setLayout(layout1)
        layout1.addWidget(SignalPlotWidget())
        self.addWidget(self.page1)

        self.page2 = QWidget()
        layout2 = QVBoxLayout(self.page2)
        label2 = QLabel("Page 2")
        layout2.addWidget(label2)
        self.page2.setLayout(layout2)
        self.addWidget(self.page2)

        self.page3 = QWidget()
        layout3 = QVBoxLayout(self.page2)
        label3 = QLabel("Page 2sssssssssssssssss")
        layout3.addWidget(label3)
        self.page3.setLayout(layout3)
        self.addWidget(self.page3)

        

if __name__ == "__main__":
    app = QApplication([])
    window = WorkSpace()
    window.show()
    app.exec_()
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from pyqtgraph.Qt import QtCore
import pyqtgraph as pg
import numpy as np

class SignalPlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: yellow;")
        # 创建pyqtgraph绘图部件
        self.plotWidget = pg.PlotWidget()
        # 设置绘图部件的背景颜色
        self.plotWidget.setBackground('w')  # 'w'代表白色，你可以使用其他颜色值
        # 创建布局，并将绘图部件添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.plotWidget)
        self.setLayout(layout)
        # 生成示例信号数据
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # 在绘图部件中绘制信号
        self.plot = self.plotWidget.plot(x, y)



        # 禁用鼠标滚轮缩放和移动功能
        self.plotWidget.setMouseEnabled(x=False, y=False)

if __name__ == "__main__":
    # 创建应用程序和主窗口
    app = QApplication(sys.argv)
    window = QWidget()

    # 创建信号展示部件并添加到主窗口中
    signalWidget = SignalPlotWidget()
    layout = QVBoxLayout()
    layout.addWidget(signalWidget)
    window.setLayout(layout)

    # 显示窗口
    window.show()

    # 运行应用程序主循环
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication
from signal_diagnosis_app import build_main_window

class FileManagerApp(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.main_window = build_main_window()
        self.main_window.show()

def main():
    app = FileManagerApp(sys.argv)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

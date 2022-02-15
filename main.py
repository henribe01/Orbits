import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from matplotlibwidget import MatplotlibWidget
from uis.python_files.test import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)
        self.mplWidget = self.findChild(MatplotlibWidget)

    def start(self):
        self.mplWidget.start_animation()

    def stop(self):
        self.mplWidget.stop_animation()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    window = MyApp()
    window.show()
    app.exec_()

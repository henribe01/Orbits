import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from uis.python_files.mainwindow import Ui_MainWindow
from widgets import MatplotAnimationWidget, MatplotOptionsWidget


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.AnimationWidget = MatplotAnimationWidget(self)
        self.OptionWidget = MatplotOptionsWidget(self)
        self.stackedWidget.addWidget(self.AnimationWidget)
        self.stackedWidget.addWidget(self.OptionWidget)
        self.showAnimationWidget()

    def showAnimationWidget(self):
        self.stackedWidget.setCurrentWidget(self.AnimationWidget)

    def showOptionsWidget(self):
        self.stackedWidget.setCurrentWidget(self.OptionWidget)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    window = MyApp()
    window.show()
    app.exec_()

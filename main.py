import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from uis.python_files.mainwindow import Ui_MainWindow
from widgets import AnimationWidget, OptionsWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.animation_widget = AnimationWidget(self)
        self.options_widget = OptionsWidget(self)
        self.stackedWidget.addWidget(self.animation_widget)
        self.stackedWidget.addWidget(self.options_widget)

        self.show_animation_widget()

    def show_animation_widget(self):
        self.stackedWidget.setCurrentWidget(self.animation_widget)

    def show_options_widget(self):
        self.stackedWidget.setCurrentWidget(self.options_widget)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    main_window = MainWindow()
    main_window.show()
    app.exec_()

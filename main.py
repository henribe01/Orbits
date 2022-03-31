import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

import planets
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


all_planets = {'Earth': [5.972 * 10 ** 24, [0, 0], [0, 0]],
                     'Moon': [7.347 * 10 ** 22, [0, 384400000], [1022, 0]],
                     'Mars': [8.753 * 10 ** 20, [300000000, 0], [0, 1000]]}

if __name__ == '__main__':
    planets.Planet.init_planets(all_planets)
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    main_window = MainWindow()
    main_window.show()
    app.exec_()

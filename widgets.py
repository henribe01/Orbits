from PyQt5.QtWidgets import QWidget

from uis.python_files.animation_widget import Ui_animation_widget
from uis.python_files.options_widget import Ui_options_widget


class AnimationWidget(QWidget, Ui_animation_widget):
    def __init__(self, parent: QWidget):
        super(AnimationWidget, self).__init__(parent)
        self.setupUi(self)
        self.connect_events()

    def connect_events(self):
        self.option_pushButton.clicked.connect(
            self.parentWidget().show_options_widget)


class OptionsWidget(QWidget, Ui_options_widget):
    def __init__(self, parent: QWidget):
        super(OptionsWidget, self).__init__(parent)
        self.setupUi(self)
        self.connect_events()

    def connect_events(self):
        self.exit_pushButton.clicked.connect(
            self.parentWidget().show_animation_widget)

from PyQt5.QtWidgets import QWidget

import planets
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
        self.start_pushButton.clicked.connect(
            self.canvas_widget.start_animation)
        self.stop_pushButton.clicked.connect(self.canvas_widget.stop_animation)
        self.reset_pushButton.clicked.connect(self.reset_canvas)

    def reset_canvas(self):
        """Resets Canvas to saved state"""
        planets.Planet.reset_planets()
        self.canvas_widget.reload_lines()


class OptionsWidget(QWidget, Ui_options_widget):
    def __init__(self, parent: QWidget):
        super(OptionsWidget, self).__init__(parent)
        self.setupUi(self)
        self.connect_events()

    def connect_events(self):
        self.exit_pushButton.clicked.connect(
            self.parentWidget().show_animation_widget)
        self.save_pushButton.clicked.connect(self.save)
        self.reset_pushButton.clicked.connect(self.reset_canvas)

    def save(self):
        self.canvas_widget.save()
        self.nativeParentWidget().show_animation_widget()

    def reset_canvas(self):
        """Resets Canvas to saved state"""
        planets.Planet.reset_planets()
        self.canvas_widget.reload_lines()
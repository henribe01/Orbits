import copy

import numpy as np
from PyQt5.QtWidgets import QWidget

import planets
from config import all_planets, save_planets
from uis.python_files.matplotlib_animation import Ui_matplotlib_animation
from uis.python_files.matplotlib_options import Ui_matplot_options


class MatplotAnimationWidget(QWidget, Ui_matplotlib_animation):
    def __init__(self, parent=None):
        super(MatplotAnimationWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        # ---- Buttons ----
        self.option_pushButton.clicked.connect(self.showOptions)
        self.start_pushButton.clicked.connect(self.start)
        self.stop_pushButton.clicked.connect(self.stop)
        self.reset_pushButton.clicked.connect(self.reset)

    def showOptions(self):
        self.parent.showOptionsWidget()

    def start(self):
        self.canvas_widget.start_animation()

    def stop(self):
        self.canvas_widget.stop_animation()

    def reset(self):
        self.canvas_widget.reset()


class MatplotOptionsWidget(QWidget, Ui_matplot_options):
    def __init__(self, parent=None):
        super(MatplotOptionsWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        # Buttons
        self.save_pushButton.clicked.connect(self.save)

    def save(self):
        """Saves the changed Planets and shows the AnimationWidget"""
        for name, line in self.canvas_widget.all_lines.items():
            all_planets[name].pos = np.array(*line[0].get_xydata())
        save_planets()
        self.parent.showAnimationWidget()

    def select(self, Planet: planets.Planet):
        """Changes the Texts to the selected Planet"""
        self.velx_lineEdit.setText(str(Planet.vel[0]))
        self.vely_lineEdit.setText(str(Planet.vel[1]))


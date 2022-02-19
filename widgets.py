from PyQt5.QtWidgets import QWidget

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

    def showOptions(self):
        self.parent.showOptionsWidget()

    def start(self):
        self.canvas_widget.start_animation()

    def stop(self):
        self.canvas_widget.stop_animation()


class MatplotOptionsWidget(QWidget, Ui_matplot_options):
    def __init__(self, parent=None):
        super(MatplotOptionsWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        # Buttons
        self.save_pushButton.clicked.connect(self.save)

    def save(self):
        self.parent.showAnimationWidget()

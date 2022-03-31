from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure


class CanvasWidget(Canvas, QWidget):
    def __init__(self, parent: QWidget):
        self.figure = Figure()
        self.axes = self.figure.add_subplot()
        self.axes.set_xlim(-100, 100)
        self.axes.set_ylim(-100, 100)

        super(CanvasWidget, self).__init__(self.figure)
        self.setParent(parent)
        super(CanvasWidget, self).setSizePolicy(QSizePolicy.Preferred,
                                                QSizePolicy.Preferred)
        super(CanvasWidget, self).updateGeometry()

    def sizeHint(self):
        return QSize(*self.get_width_height())

    def minimumSizeHint(self):
        return QSize(10, 10)
import math

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy
from matplotlib import rcParams
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

rcParams['font.size'] = 9
import matplotlib.pyplot as plt


class MatplotlibWidget(Canvas, FuncAnimation):
    def __init__(self, parent=None, title='', xlabel='', ylabel='',
                 xlim=None, ylim=None, xscale='linear', yscale='linear',
                 width=4, height=3, dpi=100):
        self.figure = Figure()
        self.axes = self.figure.add_subplot()  # type:plt.Axes

        self.lin, = self.axes.plot([], [])  # type: plt.Line2D
        self.all_x = []
        self.all_y = []
        self.axes.set_xlim(0, 10)
        self.axes.set_ylim(-1.5, 1.5)
        self.running = False

        super(MatplotlibWidget, self).__init__(self.figure)
        self.setParent(parent)
        super(MatplotlibWidget, self).setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        super(MatplotlibWidget, self).updateGeometry()
        ani = FuncAnimation.__init__(self, self.figure, self.update_ani, interval=10, blit=True)



    def update_ani(self, frames):
        if not self.running:
            self.event_source.stop()
        i = frames / 100
        self.all_x.append(i)
        self.all_y.append(math.sin(i))
        self.lin.set_data(self.all_x, self.all_y)
        return self.lin,

    def stop_animation(self):
        self.running = False

    def start_animation(self):
        self.event_source.start()
        self.running = True

    def sizeHint(self):
        return QSize(*self.get_width_height())

    def minimumSizeHint(self):
        return QSize(10, 10)

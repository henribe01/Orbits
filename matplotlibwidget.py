from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy
from matplotlib import rcParams
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

rcParams['font.size'] = 9
import matplotlib.pyplot as plt
from config import WIDTH, all_planets


class MatplotlibWidget(Canvas, FuncAnimation):
    def __init__(self, parent=None, title='', xlabel='', ylabel='',
                 xlim=None, ylim=None, xscale='linear', yscale='linear',
                 width=4, height=3, dpi=100):
        self.figure = Figure()
        self.axes = self.figure.add_subplot()  # type:plt.Axes

        # Plot Settings
        self.line, = self.axes.plot([], [], 'ro')  # type: plt.Line2D
        self.axes.set_xlim(-WIDTH, WIDTH)
        self.axes.set_ylim(-WIDTH, WIDTH)

        # Planets
        self.all_lines = list()  # List with trails for each planet and their former coordinates
        for _ in all_planets:
            line, = self.axes.plot([], [])
            self.all_lines.append((line, [], []))

        # Variable to check if animation is running
        self.running = False

        super(MatplotlibWidget, self).__init__(self.figure)
        self.setParent(parent)
        super(MatplotlibWidget, self).setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        super(MatplotlibWidget, self).updateGeometry()
        ani = FuncAnimation.__init__(self, self.figure, self.update_ani, interval=10, blit=True)

    def update_ani(self, frames):
        if not self.running:
            self.stop_animation()
            return [self.line] + [line[0] for line in self.all_lines]
        all_x_pos = list()
        all_y_pos = list()
        for index, planet in enumerate(all_planets):
            planet.update_pos()
            planet_x_pos = planet.pos[0]
            planet_y_pos = planet.pos[1]

            all_x_pos.append(planet_x_pos)
            all_y_pos.append(planet_y_pos)

            # Updat trail
            line_lst = self.all_lines[index]
            line_lst[1].append(planet_x_pos)
            line_lst[2].append(planet_y_pos)
            line_lst[0].set_data(line_lst[1], line_lst[2])

        self.line.set_data(all_x_pos, all_y_pos)
        return [self.line] + [line[0] for line in self.all_lines]

    def stop_animation(self):
        self.running = False
        self.pause()

    def start_animation(self):
        self.running = True
        self.resume()

    def sizeHint(self):
        return QSize(*self.get_width_height())

    def minimumSizeHint(self):
        return QSize(10, 10)

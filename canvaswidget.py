from typing import Iterable

import matplotlib.pyplot as plt
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy, QWidget
from matplotlib import rcParams
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

from Draggable import DraggableRectangle
from config import WIDTH, all_planets

rcParams['font.size'] = 9


class CanvasWidget(Canvas, QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        self.figure = Figure()
        self.axes = self.figure.add_subplot()  # type: plt.Axes
        self.axes.set_xlim(-WIDTH, WIDTH)
        self.axes.set_ylim(-WIDTH, WIDTH)

        self.all_lines = dict()
        self.init_lines()

        super(CanvasWidget, self).__init__(self.figure)
        self.setParent(parent)
        super(CanvasWidget, self).setSizePolicy(QSizePolicy.Preferred,
                                                QSizePolicy.Preferred)
        super(CanvasWidget, self).updateGeometry()

    def sizeHint(self):
        return QSize(*self.get_width_height())

    def minumumSizeHint(self):
        return QSize(10, 10)

    def clear(self):
        if len(self.all_lines) != 0:
            for line in self.all_lines.values():
                self.axes.lines.remove(line[0])
                self.axes.lines.remove(line[1])
            print(self.axes.lines)

    def init_lines(self):
        self.all_lines = dict()
        # Contains the Line of the planet, the line of
        # the trail and a list for the last positions
        for name, planet in all_planets.items():
            planet_line, = self.axes.plot(*planet.pos, 'ro',
                                          zorder=10)  # type:plt.Line2D
            trail_line, = self.axes.plot(*planet.pos,
                                         zorder=1)  # type:plt.Line2D
            self.all_lines[name] = [planet_line, trail_line,
                                    [[], []]]



class AnimationCanvasWidget(CanvasWidget, FuncAnimation):
    def __init__(self, parent: object = None) -> None:
        super(AnimationCanvasWidget, self).__init__()

        self.running = False
        ani = FuncAnimation.__init__(self, self.figure, self._update_ani,
                                     interval=10, blit=True)

    def _update_ani(self, frames) -> Iterable[plt.Artist]:
        if not self.running:
            self.stop_animation()
            return [line for lines in self.all_lines.values() for line in
                    lines[:2]]
        for name, planet in all_planets.items():
            planet.update_pos()

            lines = self.all_lines[name]
            lines[2][0].append(planet.pos[0])
            lines[2][1].append(planet.pos[1])
            lines[1].set_data(*lines[2])
            lines[0].set_data(*planet.pos)
        return [line for lines in self.all_lines.values() for line in
                lines[:2]]

    def stop_animation(self):
        self.running = False
        self.pause()

    def start_animation(self):
        self.running = True
        self.resume()

    def reset(self):
        self.clear()
        self.init_lines()
        self.draw()


class OptionCanvasWidget(CanvasWidget):
    def __init__(self, parent: object = None) -> None:
        super(OptionCanvasWidget, self).__init__()
        self.all_draggable_planets = list()
        for name, line in self.all_lines.items():
            planet_line = line[0]
            dr = DraggableRectangle(planet_line, name)
            dr.connect()
            self.all_draggable_planets.append(dr)

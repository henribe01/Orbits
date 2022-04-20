from typing import Iterable

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QSizePolicy
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

import planets
from lines import PlanetLines, DraggablePlanetLines
from planets import Planet


class CanvasWidget(Canvas, QWidget):
    def __init__(self, parent: QWidget):
        self.figure = Figure()
        self.axes = self.figure.add_subplot() #type: plt.Axes
        self.axes.set_xlim(-1000000000, 1000000000)
        self.axes.set_ylim(-1000000000, 1000000000)

        super(CanvasWidget, self).__init__(self.figure)
        self.setParent(parent)
        super(CanvasWidget, self).setSizePolicy(QSizePolicy.Preferred,
                                                QSizePolicy.Preferred)
        super(CanvasWidget, self).updateGeometry()

    def sizeHint(self):
        return QSize(*self.get_width_height())

    def minimumSizeHint(self):
        return QSize(10, 10)

    def plot_planets(self, line_class, planet_dict=Planet.get_all_planets()):
        all_lines = list()
        for name in planet_dict.keys():
            planet_lines = line_class(self.axes, name)
            all_lines.append(planet_lines)
        return all_lines

    def clear(self):
        for line in self.all_lines:
            line: PlanetLines
            line.clear()


class AnimationCanvasWidget(CanvasWidget, FuncAnimation):
    def __init__(self, parent):
        super(AnimationCanvasWidget, self).__init__(parent)
        self.running = False
        FuncAnimation.__init__(self, self.figure, self._update_ani,
                                     interval=10, blit=True)
        self.all_lines = self.plot_planets(PlanetLines)

    def _update_ani(self, frame) -> Iterable[plt.Artist]:
        if self.running:
            for planet_line in self.all_lines:
                planet_line.update()
        return [line for planet_line in self.all_lines for line in
                planet_line.get_lines()]

    def start_animation(self):
        self.running = True
        self.resume()

    def stop_animation(self):
        self.running = False
        self.pause()

    def reload_lines(self):
        self.clear()
        self.all_lines = self.plot_planets(PlanetLines)
        self.draw()


class OptionCanvasWidget(CanvasWidget):
    def __init__(self, parent):
        super(OptionCanvasWidget, self).__init__(parent)
        self.all_lines = self.plot_planets(DraggablePlanetLines)

    def calc_path(self):
        """Calculates the path for each planet"""
        for _ in range(500):
            for line in self.all_lines:
                line: DraggablePlanetLines
                line.update()

    def reload_lines(self):
        """Loads the current state of the planets into the OptionsCanvas"""
        for line in self.all_lines:
            line: DraggablePlanetLines
            self.axes.lines.remove(line.trail_line)
            self.axes.lines.remove(line.planet_dot)
        self.all_lines = self.plot_planets(DraggablePlanetLines)
        self.calc_path()
        self.draw()

    def save(self):
        all_planets = dict()
        for line in self.all_lines:
            line: DraggablePlanetLines
            name, planet = line.save()
            all_planets[name] = planet
        Planet.override_planets(all_planets)
        Planet.save_planet_state()

    def create_new_line(self, planet):
        line = DraggablePlanetLines(self.axes, planet)
        self.all_lines.append(line)

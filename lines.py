import copy
from typing import Tuple

import matplotlib.pyplot as plt

import planets


class PlanetLines:
    """Class with Lines that plot the Planet itself and the trailing line"""

    def __init__(self, axes: plt.Axes, name):
        self.planet = planets.Planet.get_planet(name)
        self.axes = axes

        self.all_x_pos, self.all_y_pos = [], []

        self.planet_dot, = self.axes.plot(*self.planet.pos,
                                          'ro', zorder=10)  # type:plt.Line2D
        self.trail_line, = self.axes.plot(*self.planet.pos,
                                          zorder=1)  # type:plt.Line2D

    def add_x_y_data(self, data: Tuple):
        """Adds data to the last positions of the planet"""
        self.all_x_pos.append(data[0])
        self.all_y_pos.append(data[1])

    def update(self):
        """Updates the planets position and plots the new position"""
        self.planet.update_pos()
        self.add_x_y_data(self.planet.pos)
        self.planet_dot.set_data(*self.planet.pos)
        self.trail_line.set_data(self.all_x_pos, self.all_y_pos)

    def get_lines(self):
        """Returns both line objects"""
        return self.planet_dot, self.trail_line

    def clear(self):
        self.axes.lines.remove(self.planet_dot)
        self.axes.lines.remove(self.trail_line)


class DraggablePlanetLines(PlanetLines):
    def __init__(self, axes: plt.Axes, planet):
        super(DraggablePlanetLines, self).__init__(axes, planet)
        self.press = None
        self.test_planet = copy.deepcopy(self.planet)  # type: planets.Planet
        self.connect()
        self.trail_planet = planets.TrailPlanet(
            *self.planet.get_attributes())  # type: planets.Planet
        self.canvas = self.planet_dot.figure.canvas

    def connect(self):
        """Connect to all the events we need."""
        self.cidpress = self.planet_dot.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.planet_dot.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.planet_dot.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        """Check wether mouse is over us; if so store som data"""
        if event.inaxes != self.planet_dot.axes:
            return
        contains, attrd = self.planet_dot.contains(event)
        if not contains:
            return
        self.press = *self.planet_dot.get_xydata(), (event.xdata, event.ydata)
        self.canvas.parentWidget().set_selected_line(self)

    def on_motion(self, event):
        """Move the planet if the mouse is over us."""
        if self.press is None or event.inaxes != self.planet_dot.axes:
            return
        (x0, y0), (xpress, ypress) = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.planet_dot.set_xdata(x0 + dx)
        self.planet_dot.set_ydata(y0 + dy)

        self.trail_planet.set_pos(*self.planet_dot.get_xydata())
        self.canvas.clear()
        self.canvas.calc_path()
        self.canvas.draw()

    def on_release(self, event):
        """Clear button press information"""
        self.press = None
        self.test_planet.set_pos(*self.planet_dot.get_xydata())
        self.planet_dot.figure.canvas.draw()

    def update(self):
        self.trail_planet.update_pos()
        self.add_x_y_data(self.trail_planet.pos)
        self.trail_line.set_data(self.all_x_pos, self.all_y_pos)

    def clear(self):
        self.all_x_pos, self.all_y_pos = [], []
        self.trail_line.set_data(*self.planet_dot.get_xydata())
        vel = self.test_planet.vel
        mass = self.test_planet.mass
        self.trail_planet = planets.TrailPlanet(self.test_planet.name, mass,
                                                *self.planet_dot.get_xydata(),
                                                vel)  # type: planets.Planet

    def save(self):
        return self.test_planet.name, self.test_planet

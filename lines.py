from typing import Tuple

import matplotlib.pyplot as plt


class PlanetLine:
    def __init__(self, axes: plt.Axes, planet):
        self.planet = planet
        self.axes = axes

        self.all_x_pos, self.all_y_pos = [], []

        self.planet_dot, = self.axes.plot(self.planet.pos,
                                          'ro')  # type:plt.Line2D
        self.trail_line, = self.axes.plot(self.planet.pos)  # type:plt.Line2D

    def add_x_y_data(self, data: Tuple):
        self.all_x_pos.append(data[0])
        self.all_y_pos.append(data[1])

    def plot(self):
        self.planet.update_pos()
        self.add_x_y_data(self.planet.pos)
        self.planet_dot.set_data(*self.planet.pos)
        self.trail_line.set_data(self.all_x_pos, self.all_y_pos)

    def get_lines(self):
        return self.planet_dot, self.trail_line

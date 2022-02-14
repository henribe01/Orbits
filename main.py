from __future__ import annotations

from typing import List

import matplotlib;

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
from config import INTERVALL, PLANETS, WIDTH

import numpy as np

from config import TIME, GRAV_CONST





def init():
    for planet in PLANETS.values():
        all_planets.append(Planet(*planet))
        line, = ax.plot([], [])
        all_lines.append((line, [], []))
    ax.set_xlim(-WIDTH, WIDTH)
    ax.set_ylim(-WIDTH, WIDTH)
    return ln,


def update(frame):
    all_x_pos = list()
    all_y_pos = list()
    for index, planet in enumerate(all_planets):
        planet.update_pos()
        all_x_pos.append(planet.pos[0])
        all_y_pos.append(planet.pos[1])

        line_lst = all_lines[index]
        line_lst[1].append(planet.pos[0])
        line_lst[2].append(planet.pos[1])
        line_lst[0].set_data(line_lst[1], line_lst[2])
    ln.set_data(all_x_pos, all_y_pos)
    return [ln] + [line[0] for line in all_lines]


if __name__ == '__main__':
    fig, ax = plt.subplots()  # type: plt.Figure, plt.Axes
    ln, = plt.plot([], [], 'ro')  # type:plt.Line2D

    all_planets = []  # type:List[Planet]
    all_lines = []
    init()

    ani = FuncAnimation(fig, update, blit=True, interval=INTERVALL)
    plt.show()

from typing import Dict, Any

GRAV_CONST = 6.674 * 10 ** -11
INTERVALL = 10
SPEED_UP = 1000000
TIME = (INTERVALL / 1000) * SPEED_UP

WIDTH = 1000000000
HEIGHT = 10 ** 25

all_planets = dict()
saved_all_planets = {'Earth': [5.972 * 10 ** 24, [0, 0], [0, 0]],
                     'Moon': [7.347 * 10 ** 22, [0, 384400000], [1022, 0]],
                     'Mars': [8.753 * 10 ** 20, [300000000, 0], [0, 1000]]}


def init_planets():
    from planets import Planet
    global all_planets, saved_all_planets

    for name, planet in saved_all_planets.items():
        all_planets[name] = (Planet(*planet))


def reset_planets():
    global all_planets
    for planet in all_planets.values():
        del planet
    init_planets()
    return all_planets


def save_planets():
    global saved_all_planets
    for name, planet in all_planets.items():
        saved_all_planets[name] = [planet.mass, [*planet.pos], [*planet.vel]]

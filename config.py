GRAV_CONST = 6.674 * 10 ** -11
INTERVALL = 10
SPEED_UP = 1000000
TIME = (INTERVALL / 1000) * SPEED_UP

WIDTH = 1000000000
HEIGHT = 10 ** 25

PLANETS = {'Earth': [5.972 * 10 ** 24, [0, 0], [0, 0]], 'Moon': [7.347 * 10 ** 22, [0, 384400000], [1022, 0]],
           'Mars': [8.753 * 10 ** 20, [300000000, 0], [0, 1000]]}

all_planets = dict()


def init_planets():
    from planets import Planet
    global all_planets

    for name, planet in PLANETS.items():
        all_planets[name]= (Planet(*planet))

from __future__ import annotations

import matplotlib;

matplotlib.use("TkAgg")

import numpy as np

from config import TIME, GRAV_CONST, all_planets


class Planet:
    def __init__(self, mass, pos: list, vel: list):
        self.mass = mass
        self.pos = np.array(pos, dtype=np.float64)
        self.vel = np.array(vel, dtype=np.float64)

    def update_pos(self):
        self.pos += self.vel * TIME
        self.vel += self.calc_acceleration() * TIME

    def calc_acceleration(self):
        total_force = np.array([0, 0], dtype=np.float64)
        for other_planet in all_planets.values():
            if other_planet != self:
                vector_planets = self.pos - other_planet.pos
                norm_vector = np.linalg.norm(self.pos - other_planet.pos)

                force = -(
                            GRAV_CONST * self.mass * other_planet.mass) / norm_vector ** 2
                direction_vector = vector_planets / norm_vector
                total_force += force * direction_vector
        return total_force / self.mass

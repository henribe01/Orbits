import numpy as np

from config import TIME, GRAV_CONST
from typing import Dict, List, Tuple

class Planet:
    all_planets = dict()

    def __init__(self, name, mass, pos: tuple, vel: tuple):
        self.name = name
        self.mass = mass
        self.pos = np.array(pos, dtype=np.float64)
        self.vel = np.array(vel, dtype=np.float64)
        Planet.all_planets[name] = self

    def update_pos(self):
        self.pos += self.vel * TIME
        self.vel += self.calc_acceleration() * TIME

    def calc_acceleration(self):
        """Calculates acceleration for planet"""
        total_force = np.array([0, 0], dtype=np.float64)
        for other_planet in Planet.all_planets.values():
            if other_planet != self:
                vector_planets = self.pos - other_planet.pos
                norm_vector = np.linalg.norm(vector_planets)
                force = -(
                            GRAV_CONST * self.mass * other_planet.mass) / norm_vector ** 2
                direction_vector = vector_planets / norm_vector
                total_force += force * direction_vector
        return total_force / self.mass

    @classmethod
    def init_planets(cls, planets: Dict[str, List[float, Tuple[float, float], Tuple[float, float]]]):
        """
        Creates multiple planets
        :param planets: Takes a Dict with the Planetsname as Key and as a
        Value a List consisting of mass, (pos_x, pos_y), (vel_x, vel_y)
        :return: None
        """
        for name, planet_data in planets.items():
            cls(name, *planet_data)
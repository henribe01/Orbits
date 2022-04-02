from typing import List

import numpy as np

from config import TIME, GRAV_CONST
from lines import DraggablePlanetLines


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

    def get_attributes(self):
        return self.name, self.mass, [*self.pos], [*self.vel]

    def set_pos(self, data):
        self.pos[0] = float(data[0])
        self.pos[1] = float(data[1])

    @classmethod
    def init_planets(cls, planets):
        """
        Creates multiple planets
        :param planets: Takes a Dict with the Planetname as Key and as a
        Value a List consisting of mass, (pos_x, pos_y), (vel_x, vel_y)
        :return: None
        """
        for name, planet_data in planets.items():
            planet = cls(name, *planet_data)

    @classmethod
    def __index__(cls, name):
        return cls.all_planets[name]

    @classmethod
    def get_all_planets(cls):
        return cls.all_planets

    @classmethod
    def precalc_path(cls, lines: List[DraggablePlanetLines]):
        """Calculates the first 500 Steps of each planet"""
        for _ in range(500):
            for line in lines:
                line: DraggablePlanetLines
                planet = line.planet
                planet.update_pos()
                line.add_x_y_data(tuple(planet.pos))


class TrailPlanet(Planet):
    all_planets = dict()

    def __init__(self, name, mass, pos: tuple, vel: tuple):
        super(TrailPlanet, self).__init__(name, mass, pos, vel)
        TrailPlanet.all_planets[name] = self

    def update_pos(self):
        self.pos += self.vel * TIME
        self.vel += self.calc_acceleration() * TIME

    def calc_acceleration(self):
        """Calculates acceleration for planet"""
        total_force = np.array([0, 0], dtype=np.float64)
        for other_planet in TrailPlanet.all_planets.values():
            if other_planet != self:
                vector_planets = self.pos - other_planet.pos
                norm_vector = np.linalg.norm(vector_planets)
                force = -(
                        GRAV_CONST * self.mass * other_planet.mass) / norm_vector ** 2
                direction_vector = vector_planets / norm_vector
                total_force += force * direction_vector
        return total_force / self.mass

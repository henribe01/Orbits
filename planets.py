import copy

import numpy as np

from config import TIME, GRAV_CONST


class Planet:
    all_planets = dict()
    save_state_planets = dict()

    def __init__(self, name, mass, pos: tuple, vel: tuple):
        self.name = name
        self.mass = mass
        self.pos = np.array(pos, dtype=np.float64)
        self.vel = np.array(vel, dtype=np.float64)

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

    def set_vel(self, data):
        self.vel[0] = float(data[0])
        self.vel[1] = float(data[1])

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
            cls.all_planets[name] = planet

    @classmethod
    def get_planet(cls, name):
        return cls.all_planets[name]

    @classmethod
    def get_all_planets(cls):
        return cls.all_planets

    @classmethod
    def override_planets(cls, planet_dct):
        cls.all_planets = planet_dct

    @classmethod
    def save_planet_state(cls):
        cls.save_state_planets = copy.deepcopy(cls.all_planets)

    @classmethod
    def reset_planets(cls):
        cls.all_planets = copy.deepcopy(cls.save_state_planets)


class TrailPlanet(Planet):
    all_trail_planets = dict()

    def __init__(self, name, mass, pos: tuple, vel: tuple):
        super(TrailPlanet, self).__init__(name, mass, pos, vel)
        TrailPlanet.all_trail_planets[name] = self

    def update_pos(self):
        self.pos += self.vel * TIME
        self.vel += self.calc_acceleration() * TIME

    def calc_acceleration(self):
        """Calculates acceleration for planet"""
        total_force = np.array([0, 0], dtype=np.float64)
        for other_planet in TrailPlanet.all_trail_planets.values():
            if other_planet != self:
                vector_planets = self.pos - other_planet.pos
                norm_vector = np.linalg.norm(vector_planets)
                force = -(
                        GRAV_CONST * self.mass * other_planet.mass) / norm_vector ** 2
                direction_vector = vector_planets / norm_vector
                total_force += force * direction_vector
        return total_force / self.mass

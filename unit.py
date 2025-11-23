import math
from abc import ABC, abstractmethod

import pygame

from bullet import Bullet  # import the class

class Unit(ABC):

    def __init__(self, color, x, y, fps, hp=100, speed=1, unit_range=500, fire_rate=1, cost=100, bullet=None, radius=30):
        self._shooting_cooldown = 0

        self._color = color
        self._x = x
        self._y = y
        self._hp = hp
        self._speed = speed * 180 / fps
        self._unit_range = unit_range
        self._fire_rate = fire_rate * 180 / fps
        self._cost = cost
        self._bullet = bullet
        self._radius = radius



        if color == 0: #blue
            self._direction = 0
        else:
            self._direction = math.radians(180)


    def take_damage(self, damage):

        self._hp -= damage


    def perform_action(self, enemies): #only find closest enemy and moving toward it/shooting it (no vision yet)

        if len(enemies) == 0:
            return

        closest_enemy = None
        closest_distance = 10000



        for enemy in enemies:
            distance = math.dist((self._x, self._y), (enemy.get_x(), enemy.get_y())) - self._radius - enemy.get_radius()
            if closest_distance > distance:
                closest_distance = distance
                closest_enemy = enemy

        angle = math.atan2(closest_enemy.get_y() - self._y, closest_enemy.get_x() - self._x)

        if closest_distance <= self._unit_range:
            return self.attack(angle)
        else:
            self._shooting_cooldown -= 1
            self.move(angle)





    def attack(self, angle):

        if self._shooting_cooldown > 0:
            self._shooting_cooldown -= 1

            return

        self._direction = angle
        self._shooting_cooldown = self._fire_rate

        target_x = (math.cos(angle) * self._radius * 2) + self._x
        target_y = (math.sin(angle) * self._radius * 2) + self._y


        return Bullet(self._color, target_x, target_y, self._bullet.get_fps(), self._bullet.get_radius(), angle, self._bullet.get_damage(), self._bullet.get_speed())



    def move(self, angle): #rads

        target_x = (math.cos(angle) * self._speed) + self._x
        target_y = (math.sin(angle) * self._speed) + self._y

        self._x = target_x
        self._y = target_y
        self._direction = angle

    @abstractmethod
    def draw(self, screen):
        pass


    def get_color(self):
        return self._color
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def get_hp(self):
        return self._hp
    def get_speed(self):
        return self._speed
    def get_unit_range(self):
        return self._unit_range
    def get_fire_rate(self):
        return self._fire_rate
    def get_cost(self):
        return self._cost
    def get_bullet(self):
        return self._bullet
    def get_radius(self):
        return self._radius

    def get_direction(self):
        return self._direction


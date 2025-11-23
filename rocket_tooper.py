import math

import pygame

from bullet import Bullet
from rocket import Rocket
from unit import Unit


class RocketTrooper(Unit):

    def __init__(self, color, x, y, fps):
        super().__init__(color=color, x=x, y=y, fps=fps)

        self._cost = 200
        self._speed = 0.5 * 180 / fps
        self._unit_range = 300
        self._fire_rate = 180 * 180 / fps
        self._radius = 35
        self._hp = 150

        self._bullet = Rocket(color, 0, 0, fps, 15, 0, 30, 1.3, 100, 20)


    def attack(self, angle):

        if self._shooting_cooldown > 0:
            self._shooting_cooldown -= 1

            return

        self._direction = angle
        self._shooting_cooldown = self._fire_rate

        target_x = (math.cos(angle) * self._radius * 2) + self._x
        target_y = (math.sin(angle) * self._radius * 2) + self._y


        return Rocket(self._color, target_x, target_y, self._bullet.get_fps(), self._bullet.get_radius(), angle, self._bullet.get_damage(), self._bullet.get_speed(), self._bullet.get_explosion_radius(), self._bullet.get_explosion_damage())


    def draw(self, screen):

        target_x1 = (math.cos(self.get_direction() - 0.4) * self.get_radius()) * 1.8 + self.get_x()
        target_x2 = (math.cos(self.get_direction() + 0.4) * self.get_radius()) * 1.8 + self.get_x()

        target_y1 = (math.sin(self.get_direction() - 0.4) * self.get_radius()) * 1.8 + self.get_y()
        target_y2 = (math.sin(self.get_direction() + 0.4) * self.get_radius()) * 1.8 + self.get_y()


        pygame.draw.polygon(screen, (0, 0, 0),
                         [(self.get_x(), self.get_y()),
                          (target_x1, target_y1),  (target_x2, target_y2)], 0)

        if self._color == 0:
            pygame.draw.circle(screen, (0, 0, 255),
                               [self.get_x(), self.get_y()], self.get_radius(), 0)
        else:
            pygame.draw.circle(screen, (255, 0, 0),
                               [self.get_x(), self.get_y()], self.get_radius(), 0)
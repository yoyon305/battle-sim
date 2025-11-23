import math

import pygame

from bullet import Bullet
from unit import Unit


class Gunner(Unit):

    def __init__(self, color, x, y, fps):
        super().__init__(color=color, x=x, y=y, fps=fps)

        self._cost = 100
        self._speed = 1 * 180 / fps
        self._unit_range = 250
        self._fire_rate = 100 * 180 / fps
        self._radius = 30
        self._hp = 100



        self._bullet = Bullet(color, 0, 0, fps, 5, 0, 20, 1.8)

    def draw(self, screen):

        target_x = (math.cos(self.get_direction()) * self.get_radius()) * 2 + self.get_x()
        target_y = (math.sin(self.get_direction()) * self.get_radius()) * 2 + self.get_y()


        pygame.draw.line(screen, (0, 0, 0),
                         [self.get_x(), self.get_y()],
                         [target_x, target_y], 8)

        if self._color == 0:
            pygame.draw.circle(screen, (0, 0, 255),
                               [self.get_x(), self.get_y()], self.get_radius(), 0)
        else:
            pygame.draw.circle(screen, (255, 0, 0),
                               [self.get_x(), self.get_y()], self.get_radius(), 0)



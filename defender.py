import math

import pygame

from unit import Unit


class Defender(Unit):

    def __init__(self, color, x, y, fps):
        super().__init__(color=color, x=x, y=y, fps=fps)



        self._cost = 300
        self._speed = 0.35
        self._unit_range = 1
        self._fire_rate = 9999
        self._radius = 45
        self._hp = 500

        self._bullet = None



    def attack(self, angle):
        return



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

        if closest_distance > 75:
            self.move(angle)






    def draw(self, screen):

        target_x1 = (math.cos(self.get_direction() - 0.6) * self.get_radius()) * 1.5 + self.get_x()
        target_x2 = (math.cos(self.get_direction() + 0.6) * self.get_radius()) * 1.5 + self.get_x()

        target_y1 = (math.sin(self.get_direction() - 0.6) * self.get_radius()) * 1.5 + self.get_y()
        target_y2 = (math.sin(self.get_direction() + 0.6) * self.get_radius()) * 1.5 + self.get_y()


        pygame.draw.line(screen, (0, 0, 0),
                         (target_x1, target_y1),  (target_x2, target_y2), 10)

        if self._color == 0:
            pygame.draw.circle(screen, (0, 0, 255),
                               [self.get_x(), self.get_y()], self.get_radius(), 0)
        else:
            pygame.draw.circle(screen, (255, 0, 0),
                               [self.get_x(), self.get_y()], self.get_radius(), 0)


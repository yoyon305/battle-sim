import math

from bullet import Bullet


class Rocket(Bullet):

    def __init__(self, color, x, y, fps, radius=15, direction=0, damage=25, speed=1.3, explosion_radius=100, explosion_damage=15):
        super().__init__(color, x, y, fps, radius, direction, damage, speed)
        self._explosion_radius = explosion_radius
        self._explosion_damage = explosion_damage



    def on_hit(self, closest_enemy, enemies = None):

        for enemy in enemies:
            if enemy == closest_enemy:

                enemy.take_damage(self._damage)
            elif math.dist((self._x, self._y), (enemy.get_x(), enemy.get_y())) - self._radius - enemy.get_radius() <= self._explosion_radius:
                enemy.take_damage(self._explosion_damage)



    def update(self, enemies):

        closest_enemy = None
        closest_distance = 10000

        for enemy in enemies:
            distance = math.dist((self._x, self._y), (enemy.get_x(), enemy.get_y())) - self._radius - enemy.get_radius()
            if closest_distance > distance:
                closest_distance = distance
                closest_enemy = enemy

        if closest_distance <= 0:
            self.on_hit(closest_enemy, enemies)
            self._is_active = False
            return

        target_x = (math.cos(self._direction) * self._speed) + self._x
        target_y = (math.sin(self._direction) * self._speed) + self._y

        self._x = target_x
        self._y = target_y




    def get_explosion_radius(self):
        return self._explosion_radius

    def get_explosion_damage(self):
        return self._explosion_damage

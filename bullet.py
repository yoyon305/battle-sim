import math


class Bullet:

    def __init__(self, color, x, y, fps, radius=5, direction=0, damage=20, speed=1.8):
        self._color = color
        self._x = x
        self._y = y
        self._radius = radius
        self._direction = direction
        self._damage = damage
        self._speed = speed * 180 / fps

        self._is_active = True
        self._fps = fps


    def update(self, enemies):

        closest_enemy = None
        closest_distance = 10000

        for enemy in enemies:
            distance = math.dist((self._x, self._y), (enemy.get_x(), enemy.get_y())) - self._radius - enemy.get_radius()
            if closest_distance > distance:
                closest_distance = distance
                closest_enemy = enemy

        if closest_distance <= 0:
            self.on_hit(closest_enemy)
            self._is_active = False
            return

        target_x = (math.cos(self._direction) * self._speed) + self._x
        target_y = (math.sin(self._direction) * self._speed) + self._y

        self._x = target_x
        self._y = target_y

    def on_hit(self, closest_enemy):

        closest_enemy.take_damage(self._damage)

    def get_color(self):
        return self._color

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_radius(self):
        return self._radius


    def get_direction(self):
        return self._direction

    def get_damage(self):
        return self._damage

    def get_speed(self):
        return self._speed

    def get_fps(self):
        return self._fps

    def is_active(self):
        return self._is_active







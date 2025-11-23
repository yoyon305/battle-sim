from defender import Defender
from gunner import Gunner
from rocket_tooper import RocketTrooper


class Battlefield:



    def __init__(self, width, height):
        self._blue_units = []
        self._red_units = []
        self._bullets = []
        self._width = width
        self._height = height


    def simulate(self):

        for unit in self._blue_units:
            if unit.get_hp() > 0:
                blue_bullet = unit.perform_action(self._red_units)
                if blue_bullet:
                        self._bullets.append(blue_bullet)

        for unit in self._red_units:
            if unit.get_hp() > 0:

                red_bullet = unit.perform_action(self._blue_units)
                if red_bullet:
                    self._bullets.append(red_bullet)


        for bullet in self._bullets:
            if bullet.get_color() == 0:
                bullet.update(self._red_units)

            else:
                bullet.update(self._blue_units)



        if min(len(self._blue_units), len(self._red_units)) <= 0:
            return True

    def summon_unit(self, color, x, y, type, fps):

        unit = None

        if type == 0:
            #gunner
            unit = Gunner(color, x, y, fps)


        elif type == 1:
            #gunner
            unit = RocketTrooper(color, x, y, fps)

        elif type == 2:
            #gunner
            unit = Defender(color, x, y, fps)

        else:
            print(type)
            return

        if unit.get_color() == 0:
            self._blue_units.append(unit)
        else:
            self._red_units.append(unit)
        return unit.get_cost()

    def clear_objects(self):
        remove_list = []
        for unit in self._blue_units:

            if unit.get_hp() <= 0:
                remove_list.append(unit)

        for unit in remove_list:
            self._blue_units.remove(unit)

        remove_list = []

        for unit in self._red_units:

            if unit.get_hp() <= 0:
                remove_list.append(unit)


        for unit in remove_list:
            self._red_units.remove(unit)
        remove_list = []

        for bullet in self._bullets:

            if not bullet.is_active():
                remove_list.append(bullet)

            if bullet not in remove_list:
                if bullet.get_x() < 0 or bullet.get_x() > self._width:
                    remove_list.append(bullet)
                elif bullet.get_y() < 0 or bullet.get_y() > self._height:
                    remove_list.append(bullet)



        for bullet in remove_list:
            self._bullets.remove(bullet)

    # Getter methods
    def get_blue_units(self):
        return self._blue_units

    def get_red_units(self):
        return self._red_units

    def get_bullets(self):
        return self._bullets

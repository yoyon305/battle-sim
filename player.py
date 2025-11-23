class Player:

    def __init__(self, color, starting_money):
        self._color = color
        self._money = starting_money


    def summon_unit(self, unit_cost):

        self._money -= unit_cost


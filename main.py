import math

import pygame

from battlefield import Battlefield
from player import Player
from rocket import Rocket

FPS = 180
WIDTH = 1000
HEIGHT = 600
STARTING_MONEY = 500
NUM_OF_UNIT_TYPES = 3

p1 = Player(0, STARTING_MONEY)
p2 = Player(1, STARTING_MONEY)

selected_key = 0

battle_ended = False
start_sim = False

rocket_explosions = {}

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle Sim")

battlefield = Battlefield(WIDTH, HEIGHT)
clock = pygame.time.Clock()


# Game loop
running = True
while running:

    screen.fill((70, 70, 70))


    if start_sim:
        battle_ended = battlefield.simulate()

    for bullet in battlefield.get_bullets():

        if type(bullet) == Rocket and not bullet.is_active():

            if (bullet.get_x(), bullet.get_y(), bullet.get_explosion_radius()) not in rocket_explosions:
                rocket_explosions[(bullet.get_x(), bullet.get_y(), bullet.get_explosion_radius())] = FPS / 6

        else:

            pygame.draw.circle(screen, (255, 255, 0),
                           [bullet.get_x(), bullet.get_y()], bullet.get_radius(), 0)
    del_list = []
    for rocket in rocket_explosions:
        pygame.draw.circle(screen, (190, 120, 10),
                            [rocket[0], rocket[1]], rocket[2], 0)
        rocket_explosions[rocket] -= 1
        if rocket_explosions[rocket] <= 0:
            del_list.append(rocket)

    for rocket in del_list:
        del rocket_explosions[rocket]


    for unit in battlefield.get_blue_units():


        unit.draw(screen)
        #target_x = (math.cos(unit.get_direction()) * unit.get_radius()) * 2 + unit.get_x()
        #target_y = (math.sin(unit.get_direction()) * unit.get_radius()) * 2 + unit.get_y()


        #pygame.draw.line(screen, (0, 0, 0),
        #                 [unit.get_x(), unit.get_y()],
        #                 [target_x, target_y], 8)
        #pygame.draw.circle(screen, (0, 0, 255),
        #                   [unit.get_x(), unit.get_y()], unit.get_radius(), 0)



    for unit in battlefield.get_red_units():
        unit.draw(screen)

        #target_x = (math.cos(unit.get_direction()) * unit.get_radius()) * 2 + unit.get_x()
        #target_y = (math.sin(unit.get_direction()) * unit.get_radius()) * 2 + unit.get_y()

        #pygame.draw.line(screen, (0, 0, 0),
        #                 [unit.get_x(), unit.get_y()],
        #                 [target_x, target_y], 8)

        #pygame.draw.circle(screen, (255, 0, 0),
        #                   [unit.get_x(), unit.get_y()], unit.get_radius(), 0)


    if start_sim:
        battlefield.clear_objects()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if x <= WIDTH / 2:
                    #p1

                    p1.summon_unit(battlefield.summon_unit(0, x, y, selected_key, FPS))
                else:
                    #p2
                    p2.summon_unit(battlefield.summon_unit(1, x, y, selected_key, FPS))

        elif event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                selected_key = ((event.key - pygame.K_1) % NUM_OF_UNIT_TYPES)
            elif pygame.K_SPACE:
                start_sim = True
    clock.tick(FPS)


# Quit Pygame
pygame.quit()
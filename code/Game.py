#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Level import Level
from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPT[0], MENU_OPT[1], MENU_OPT[2]]:
                player_score = [0, 0] # [Player1, Player2]
                level = Level(self.window, "Level1", menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                   level = Level(self.window, "Level2", menu_return, player_score)
                   level_return = level.run(player_score)
            elif menu_return == MENU_OPT[4]:
                pygame.quit()  # close window
                quit()  # end pygame
            else:
                pass

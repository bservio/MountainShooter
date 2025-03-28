# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (0, 255, 255)

# E
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 50,
    'Enemy2': 60,
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 1,
    'Enemy2': 1,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
}

EVENT_ENEMY = pygame.USEREVENT + 1


# M
MENU_OPT = ('NEW GAME 1P',
            'NEW GAME 2P - COOPERATIVE',
            'NEW GAME 2P - COMPETITIVE',
            'SCORE',
            'EXIT')


# P
PLAYER_KEY_UP = {
    'Player1': pygame.K_w,
    'Player2': pygame.K_i
}
PLAYER_KEY_DOWN = {
    'Player1': pygame.K_s,
    'Player2': pygame.K_k
}
PLAYER_KEY_LEFT = {
    'Player1': pygame.K_a,
    'Player2': pygame.K_j
}
PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_d,
    'Player2': pygame.K_l
}
PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_SPACE,
    'Player2': pygame.K_RCTRL
}

# S

SPAWN_TIME = 5000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

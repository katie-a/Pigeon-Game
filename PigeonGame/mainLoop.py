import pygame
import time
import random
import keepVariables as kv
import keepObjects as ko
import keepClasses as kc
import keepFunctions as kf


pygame.init()
run = True

while run:

    while kv.home_screen:
        kf.home_screen_window()
        kf.mouse_checked()
        kf.check_true_homepage()
        pygame.display.update()

    while kv.main_game:
        kf.main_game_window()
        kf.mouse_checked()
        pygame.display.update()

    while kv.instructions:
        kf.inst_window()
        kf.mouse_checked()
        pygame.display.update()



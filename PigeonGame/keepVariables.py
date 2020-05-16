import pygame
pygame.init()

# creates a window with the home screen as a background
win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Pigeon")

# global variables
# global home_screen
# global main_game
# global mouse_x
# global mouse_y
# global money
# global instructions
# global sleepScreen
# global totalComfort
# global timePassed

instructions = False
main_game = False
lose_level = False
money = 500
sleep_screen = False
total_comfort = 0
time_passed = 0
home_screen = True
run = True

pos_list = [0, 0, False]


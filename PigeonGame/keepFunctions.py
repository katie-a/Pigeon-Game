import pygame
import keepVariables as kv
import keepObjects as ko
import keepClasses as kc
import keepImages as ki

pygame.init()
win = kv.win

def drawMoney():
    pass

def drawDirt():
    pass


def checkDirt():
    pass


def drawComfort():
    pass

def sleepShopCheck():
    pass

# the first time you click on the sleep column, you customise the nest
# pigeons eat seeds
# in toilet, might have to attach pigeon pants


# functions for drawing all the game screens
def home_screen_window():
    win.blit(ki.homeImage, (0,0))
    ko.playButton.draw_self()
    ko.instButton.draw_self()
    ko.playButton.check_self()
    ko.instButton.check_self()


def main_game_window():
    win.blit(ki.mainImage, (0, 0))
    ko.hungerButton.lose_level()
    ko.hungerButton.draw_level()


def inst_window():
    win.blit(ki.instImage, (0, 0))


def food_shop_window():
    pass


def hygiene_window():
    pass


def sleep_shop_window():
    pass


def sleep_time_window():
    pass


def all_lose_level():
    pass


def mouse_checked():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kv.run = False
            pygame.display.quit()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            mouse_x = position[0]
            mouse_y = position[1]
            kv.pos_list[0] = mouse_x
            kv.pos_list[1] = mouse_y
            kv.pos_list[2] = True


def save():
    pass


def load():
    pass


def check_true_homepage():
    if ko.playButton.clicked:
        ko.playButton.clicked = False
        kv.home_screen = False
        kv.main_game = True
    if ko.instButton.clicked:
        ko.instButton.clicked = False
        kv.home_screen = False
        kv.instructions = True






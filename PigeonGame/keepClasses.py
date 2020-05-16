import pygame
import time
import keepVariables as kv
import keepFunctions as kf

pygame.init()
win = kv.win

class RectButton:

    def __init__(self, colour, size, word, font_size=30):
        self.r = colour[0]
        self.g = colour[1]
        self.b = colour[2]
        self.x = size[0]
        self.y = size[1]
        self.width = size[2]
        self.height = size[3]
        self.word = word
        self.font = pygame.font.SysFont("comicsans", font_size)
        self.text = self.font.render(self.word, 1, (255, 255, 255))
        self.clicked = False
        self.tw = self.text.get_width()
        self.th = self.text.get_height()
        self.x_pos = ((self.width - self.tw) / 2) + self.x
        self.y_pos = ((self.height - self.th) / 2) + self.y

    def draw_self(self):
        pygame.draw.rect(win, (self.r, self.g, self.b), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)
        win.blit(self.text, (self.x_pos, self.y_pos))

    def check_self(self):
        mouse_check = kv.pos_list
        if mouse_check[2] == True and mouse_check[0] >= self.x and mouse_check[0] <= self.x + self.width \
                and mouse_check[1] >= self.y and mouse_check[1] <= self.y + self.height:
            self.clicked = True


class CareLevel(RectButton):

    def __init__(self, size, word, font_size, timer):
        self.x = size[0]
        self.y = size[1]
        self.width = size[2]
        self.height = size[3]
        self.word = word
        self.font = pygame.font.SysFont("comicsans", font_size)
        self.text = self.font.render(self.word, 1, (255, 255, 255))
        self.clicked = False
        self.tw = self.text.get_width()
        self.th = self.text.get_height()
        self.x_pos = ((self.width - self.tw) / 2) + self.x
        self.y_pos = ((self.height - self.th) / 2) + self.y
        self.level = 100
        self.timer = timer

    def lose_level(self):
        time.sleep(self.timer / 1000)
        self.level -= 0.1

    def draw_level(self):
        rect_width = self.width / 100
        rect_width *= self.level
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, rect_width, self.height))
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)
        win.blit(self.text, (self.x_pos, self.y_pos))

    def check_shop(self):
        pass

    def draw_shop(self):
        pass

    def main_game_check(self):
        pass


class ExitButton(CareLevel):
    def __init__(self):
        pass

    def draw_self(self):
        pass

    def check_self(self):
        pass


class ShopItem:
    def __init__(self):
        pass

    def draw_self(self):
        pass


class FoodItem(ShopItem):

    def __init__(self):
        pass

    def check_self(self):
        pass

    def draw_self(self):
        pass


class Pigeon:

    def __init__(self):
        pass

    def draw_self(self):
        pass


class Dirt:
    dirtsClicked = []

    def __init__(self):
        pass

    def draw_self(self):
        pass

    def check_self(self):
        pass


class NewNest:

    def __init__(self):
        pass

    def draw_self(self):
        pass

    def check_self(self):
        pass


class SleepItem:

    def __init__(self):
        pass

    def draw_self(self):
        pass

    def check_self(self):
        pass



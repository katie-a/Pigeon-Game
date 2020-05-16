import pygame
import time 
import random

#global variables
global checkIt
global homescreen
global maingame
global mousex
global mousey
global money
global instructions
global sleepScreen
global totalComfort

instructions = False
checkIt = False
homescreen = False
maingame = False
loseLevel = False
money = 500
sleepScreen = False
totalComfort = 0

#creates a window with the homescreen as a background
win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Pigeon")
bg = [pygame.image.load("pigeon_home_screen.png"), pygame.image.load("pigeonmainscreen.png")]

def drawMoney(x = 900,y = 30, fontsize = 40):
    global money
    font = pygame.font.SysFont("comicsans",30)
    text = font.render(str(money) ,1, (0,0,0))
    coin = pygame.image.load("coin.png")
    textwidth = text.get_width()
    coinwidth = coin.get_width()
    totalx = 1000 - (32 + coinwidth + textwidth)
    totalwidth = coinwidth + textwidth + 12
    pygame.draw.rect(win, (255,255,255), (totalx, 20, totalwidth, 30))
    pygame.draw.rect(win, (0,0,0), (totalx, 20, totalwidth, 30), 3)
    win.blit(coin, (totalx + 5, 24))
    win.blit(text,(totalx + 7 + coinwidth, 26))
   

class rectButton():

    def __init__(self, text, x, y, width, height, r = 255 , g = 165, b = 0, fontsize = 45, fontr = 255, fontg = 255, fontb = 255):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.r = r
        self.g = g
        self.b = b
        self.clicked = False #make a function outside this class for each individual button what to do when clicked is true
        self.fontsize = fontsize
        self.fontr = fontr
        self.fontb = fontb
        self.fontg = fontg
        self.halfrectx = self.x + (self.width // 2)
        self.halfrecty = self.y + (self.height // 2)
        

    def drawSelf(self):
        pygame.draw.rect(win, (self.r, self.g, self.b), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)

    def drawText(self):
        
        font = pygame.font.SysFont("comicsans", self.fontsize)
        text = font.render(self.text, 1, (self.fontr, self.fontg, self.fontb))
        textwidth = text.get_width() // 2
        textheight = text.get_height() // 2
        areay = self.halfrecty - textheight
        areax = self.halfrectx - textwidth
        win.blit(text, (areax, areay))

    def checkSelf(self):
        global mousex
        global mousey
        global checkIt
        if checkIt == True:
            if mousex >= self.x and mousex <= self.x + self.width and mousey >= self.y and mousey <= self.y + self.height:
                self.clicked = True
                #print("oof")
                checkIt = False
       
class careLevel(rectButton):

    def __init__(self, text, x, y, height, width, timeStays, shopPic, r = 255, g = 0, b = 0):
        self.level = 100.0
        self.timeStays = timeStays
        self.shopScreen = False
        self.shopPic = shopPic
        self.clicked = False
        super().__init__(text, x, y, height, width, r, g, b)
        

    def loseLevel(self):
        if self.level - self.timeStays / 10000.0 >= 0:
            time.sleep(0.1)
            self.level -= self.timeStays / 10000.0
        else:
            print("you died")
        
        
    def drawLevel(self):
        #draws the level of the health, sleep etc
        if self.level <= 100:
            self.drawAmount = int((self.width / 100) * self.level)
            pygame.draw.rect(win, (0, 230, 0), (self.x, self.y, self.drawAmount, self.height))
            pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)
        if self.level > 100:
            pygame.draw.rect(win, (0, 230, 0), (self.x, self.y, 280, self.height))
            pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)
        



    def checkShop(self):
        global maingame
        
        if self.clicked == True:
            
            self.shopScreen = True
            self.clicked = False
            maingame = False


    def drawShop(self):
        coin = pygame.image.load("coin.png")
        win.blit(self.shopPic, (0,0))
        po.drawMoney(905,35,27)


    def mainGameCheck(self):
        self.drawSelf()
        self.drawLevel()
        self.drawText()
        #self.checkSelf()
        self.checkShop()








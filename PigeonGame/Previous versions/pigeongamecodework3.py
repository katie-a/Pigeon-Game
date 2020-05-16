import pygame
import time 
import random

pygame.init()

#global variables
global checkIt
global homescreen
global maingame
global mousex
global mousey
global money
global instructions

instructions = False
checkIt = False
homescreen = False
maingame = False
loseLevel = False
money = 500



def drawMoney(x = 900,y = 30):
    global money
    font = pygame.font.SysFont("comicsans", 40)
    text = font.render(str(money), 1, (0, 0, 0))
    win.blit(text, (x, y))



#creates a window with the homescreen as a background
win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Pigeon")
bg = [pygame.image.load("pigeon_home_screen.png"), pygame.image.load("pigeonmainscreen.png")]

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
            

#rectangular buttons
playButton = rectButton('Play!',400, 350, 209, 60)
instButton = rectButton('Instructions', 400, 420, 209, 60)



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
        win.blit(self.shopPic, (0,0))
        drawMoney(900, 30)


    def mainGameCheck(self):
        self.drawSelf()
        self.drawLevel()
        self.drawText()
        #self.checkSelf()
        self.checkShop()

#care level buttons
hungerButton = careLevel('Hunger', 37, 320, 280, 60, random.uniform(1000.0, 1010.0), pygame.image.load("foodShop.png"))
hygieneButton = careLevel('Hygiene', 37, 395, 280, 60, 1000.0, pygame.image.load("whitebg.png"))
        
class exitButton(careLevel):
    def __init__(self, x = 45, y = 45, radius = 30, thickness = 5):
        self.clicked = False
        self.x = x
        self.y = y
        self.radius = radius
        self.thickness = thickness
        self.linex = int(self.x - (self.radius / 3))
        self.liney = int(self.y - (self.radius / 3))
        self.linexa = int(self.x + (self.radius / 3))
        self.lineya = int(self.y + (self.radius / 3))


    def drawSelf(self):
        pygame.draw.circle(win, (254,165,165), (self.x, self.y), self.radius)
        pygame.draw.circle(win, (230,0,0), (self.x, self.y), self.radius, self.thickness)
        pygame.draw.line(win, (230, 0, 0), (self.linex, self.liney), (self.linexa , self.lineya) , 1)
        pygame.draw.line(win, (230, 0, 0), (self.linex, self.lineya), (self.linexa, self.liney) , 1)

    def checkSelf(self):
        global mousex
        global mousey
        global checkIt
        if checkIt == True:
            if mousex >= self.x - self.radius and mousex <= self.x + self.radius and mousey >= self.y  - self.radius and mousey <= self.y + self.radius:
                self.clicked = True
        
#exit buttons
foodExit = exitButton()
instExit = exitButton()
mainExit = exitButton(10,10, 10, 1)
hygieneExit = exitButton()



class shopItem():
    def __init__(self, x, y, picture, cost):#make an inventory to store stuff that's bought that isn't used right away
        self.x = x
        self.y = y
        self.picture = pygame.image.load(picture)
        self.cost = cost
        

    def drawSelf(self):
        win.blit(self.picture, (self.x,self.y))
        



class foodItem(shopItem):

    def __init__(self,x,y, cost,hunger):
        self.picture = pygame.image.load("foodBagFinal.png")
        self.x = x
        self.y = y
        self.cost = cost
        self.hunger = hunger

    def checkSelf(self):
        global checkIt
        global money
        
        if checkIt == True and mousex >= self.x and mousex <= self.x + 125 and mousey >= self.y and mousey <= self.y + 150:
            checkIt = False
            if money - self.cost >= 0:
                money -= self.cost
                hungerButton.level += self.hunger

    def drawSelf(self):
        win.blit(self.picture, (self.x,self.y))
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render("£" + str(self.cost) + " Hunger +" + str(self.hunger), 1, (0,0,0))
        win.blit(text, (self.x, self.y + 160))
        

#food shop items
food1 = foodItem(330,127, 25, 10)
food2 = foodItem(520,127, 50, 20)
food3 = foodItem(330,302, 100, 40)
food4 = foodItem(520,302, 200, 100)            

        
        
class pigeon():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.picture = pygame.image.load("pigeonpic.png")
        self.clean1 = False
        
            

    def drawSelf(self):
        win.blit(self.picture, (self.x, self.y))
        
        

   

pigeon1 = pigeon(375,50) 

dirtsClicked = []
class dirt():

    def __init__(self, x, y, picture = "dirt2.png"):
        self.x = x + pigeon1.x
        self.y = y + pigeon1.y
        self.picture = pygame.image.load(picture)
        self.size = self.picture.get_size()
        self.height = self.size[1]
        self.width = self.size[0]
        self.clicked = False

    def drawSelf(self):
        win.blit(self.picture, (self.x, self.y))

    def checkSelf(self):
        global dirtsClicked
        global checkIt
        global mousex
        global mousey
        
        if checkIt == True and mousex >= self.x and mousex <= self.x + self.width and mousey >= self.y and mousey <= self.y + self.width:
            self.clicked = True
            dirtsClicked.append(self)
            hygieneButton.level += 20
            checkIt = False


#to make the bird look dirtier    
dirt1 = dirt(150,148,"dirt1.png")
dirt2 = dirt(64,151, "dirt2.png")
dirt3 = dirt(105,77, "dirt3.png")
dirt4 = dirt(36,65, "dirt4.png")

dirts = [dirt1, dirt2, dirt3, dirt4]   
        


def drawDirt():
    
    toDraw = 4 - int(hygieneButton.level / 20)
    a = 0
    i = 0
    for x in range(len(dirts)):
        if dirts[i].clicked == False:
           if a < toDraw:
               #print("e")
               dirts[i].drawSelf()
               a += 1
        else:
           #dirts[i].clicked = False
            pass


        i += 1
    b = len(dirtsClicked)
    c = 0
    for m in range(b):
        if a < toDraw:
            dirtsClicked[c].drawSelf()
            dirtsClicked[c].clicked = False
            del dirtsClicked[c]
            a += 1
        c += 1
        
           
def checkDirt():
    dirt1.checkSelf()
    dirt2.checkSelf()
    dirt3.checkSelf()
    dirt4.checkSelf()


#the first time you click on the sleep column, you customise the nest
#pigeons eat seeds
#in toilet, might have to attach pigeon pants

#functions for drawing all the game screens
def homescreenWindow(): 
    win.blit(bg[0], (0,0))
    playButton.drawSelf()
    instButton.drawSelf()
    playButton.drawText()
    instButton.drawText()

def maingameWindow():
    win.blit(bg[1], (0,0))
    hungerButton.mainGameCheck()
    hygieneButton.mainGameCheck()
    hungerButton.checkSelf()
    hygieneButton.checkSelf()
    mainExit.drawSelf()
    pigeon1.drawSelf()
    drawMoney()
    drawDirt()

def foodShopWindow():
    win.fill([255,255,255])
    hungerButton.drawShop()
    food1.drawSelf()
    food2.drawSelf()
    food3.drawSelf()
    food4.drawSelf()
    foodExit.drawSelf()

def hygieneWindow():
    win.fill([255,255,255])
    hygieneButton.drawShop()
    hygieneExit.drawSelf()
    pigeon1.drawSelf()
    drawDirt()
    checkDirt()
        
def allLoseLevel():
    hungerButton.loseLevel()
    hygieneButton.loseLevel()
    
def instWindow():
    win.fill([0,0,0])
    font = pygame.font.SysFont("comicsans", 50)
    text = font.render("Work in progress :-)", 1, (255,255,255))
    textwidth = text.get_width() // 2
    textheight = text.get_height() // 2 #1000, 500
    areay = 250 - textheight
    areax = 500 - textwidth
    win.blit(text, (areax, areay))
    instExit.drawSelf()

def mouseChecked():
    global mousex
    global mousey
    global checkIt
    
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
        #check if the play button has been clicked
            position = pygame.mouse.get_pos()
            mousex = position[0]
            mousey = position[1]
            checkIt = True
                    

        if event.type == pygame.QUIT:
            save()
            pygame.display.quit()
            pygame.quit()
            

def save():
	f = open("save.txt","w+")
	f.write(str(money))
	f.write("\n")
	f.write(str(int(hungerButton.level)))
	f.write("\n")
	f.write(str(int(hygieneButton.level)))
	f.close()    
    

def load():
    global money
    f = open("save.txt","r")
    info = f.read()
    info = info.split("\n")
    money = int(info[0])
    hungerButton.level = int(info[1])
    hygieneButton.level = int(info[2])


    
    
load()
homescreen = True    
run = True

while run:

    while homescreen:

        mouseChecked()

        playButton.checkSelf()
        instButton.checkSelf()
        if playButton.clicked == True:
            playButton.clicked = False
            homescreen = False
            maingame = True
            pygame.display.update()

        if instButton.clicked == True:
            instButton.clicked = False
            homescreen = False
            instructions = True
            pygame.display.update()

        
        homescreenWindow()
        pygame.display.update()


    while instructions:

        mouseChecked()

        instExit.checkSelf()
        if instExit.clicked == True:
            homescreen = True
            pygame.display.update()
            instructions = False
            instExit.clicked = False

        else:
            instWindow()
            pygame.display.update()


    while maingame:


        mouseChecked()
        
        allLoseLevel()

        mainExit.checkSelf()

        if mainExit.clicked == True:
            homescreen = True
            maingame = False
            mainExit.clicked = False
            pygame.display.update()

        maingameWindow()
            
        pygame.display.update()
        


    while hungerButton.shopScreen:

        mouseChecked()

        food1.checkSelf()
        food2.checkSelf()
        food3.checkSelf()
        food4.checkSelf()

        foodExit.checkSelf()

        if foodExit.clicked == True:
            maingame = True
            hungerButton.shopScreen = False
            foodExit.clicked = False
            pygame.display.update()
        else:
            win.fill([255,255,255])
            foodShopWindow()
            pygame.display.update()
       
        allLoseLevel()


    while hygieneButton.shopScreen:

        mouseChecked()

        hygieneExit.checkSelf()
        

        if hygieneExit.clicked == True:
            maingame = True
            hygieneButton.shopScreen = False
            hygieneExit.clicked = False
            pygame.display.update()
        else:
            win.fill([255,255,255])
            hygieneWindow()
            pygame.display.update()

        allLoseLevel()
        

    


        
        

        


        
        
    
              
    





    





    
    





    
    
       


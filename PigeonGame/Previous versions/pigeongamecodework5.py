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
                #print("oof")
                checkIt = False
            

#rectangular buttons
playButton = rectButton('Play!',400, 350, 209, 60)
instButton = rectButton('Instructions', 400, 420, 209, 60)
sleepTimeButton = rectButton('Go to sleep', 400, 435, 209, 60, fontsize = 27)
sleepShopButton = rectButton('Upgrade your nest', 400, 435, 209, 60, fontsize = 27)




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
        drawMoney(905,35,27)


    def mainGameCheck(self):
        self.drawSelf()
        self.drawLevel()
        self.drawText()
        #self.checkSelf()
        self.checkShop()

#care level buttons
hungerButton = careLevel('Hunger', 37, 320, 280, 60, random.uniform(1000.0, 1010.0), pygame.image.load("foodShop.png"))
hygieneButton = careLevel('Hygiene', 37, 395, 280, 60, 1000.0, pygame.image.load("hygieneScreen.png"))
sleepButton = careLevel('Sleep', 347, 320, 280, 60, 1000.0, pygame.image.load("sleepShop1.png"))
        
class exitButton(careLevel):
    def __init__(self, x = 45, y = 45, radius = 20, thickness = 3):
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
                checkIt = False
        
#exit buttons
foodExit = exitButton()
instExit = exitButton()
mainExit = exitButton()
hygieneExit = exitButton()
sleepShopExit = exitButton()
sleepTimeExit = exitButton()





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


global timePassed
timePassed = 0       
        
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

    def __init__(self, x, y, picture):
        self.x = x + pigeon1.x
        self.y = y + pigeon1.y
        self.picture = pygame.image.load(picture)
        self.size = self.picture.get_size()
        self.height = self.size[1]
        self.width = self.size[0]
        self.clicked = False

    def drawSelf(self):
        if maingame:
            win.blit(self.picture, (self.x, self.y))
        if hygieneButton.shopScreen:
            win.blit(self.picture, (self.x, self.y))

    def checkSelf(self):
        global dirtsClicked
        global checkIt
        global mousex
        global mousey
        
        if checkIt == True and mousex >= self.x and mousex <= self.x + self.width and mousey >= self.y and mousey <= self.y + self.height:
            self.clicked = True
            dirtsClicked.append(self)
            hygieneButton.level += 20
            checkIt = False


#to make the bird look dirtier    
dirt1 = dirt(150,148 ,"dirt1.png")
dirt2 = dirt(64,151,"dirt2.png")
dirt3 = dirt(105,77, "dirt3.png")
dirt4 = dirt(36,65,"dirt4.png")

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




class newNest():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.picture = pygame.image.load("nest1actual.png")
        self.width = self.picture.get_width()
        self.height = self.picture.get_height()
        self.nestLevel = 0
        self.cost = 20
        self.clicked = False
        self.maxLevel = 4

    def drawSelf(self):
        win.blit(self.picture, (self.x, self.y))
        font = pygame.font.SysFont("comicsans", 23)
        if self.nestLevel < self.maxLevel:
            text = font.render("A new nest £" + str(self.cost), 1, (0,0,0))
            win.blit(text, (self.x, self.y + self.height))
        else:
            text = font.render("Fully upgraded :-)", 1, (0,0,0))
            win.blit(text, (self.x, self.y + self.height))

    def checkSelf(self):
        global checkIt
        global mousex
        global mousey
        global money
        global totalComfort
        if checkIt == True:
            if mousex >= self.x and mousex <= self.x + self.width and mousey >= self.y and mousey <= mousey + self.height:
                if self.nestLevel < self.maxLevel and money - self.cost >= 0:
                    
                    
                    self.nestLevel += 1
                    money -= self.cost
                    self.cost += 20
                    checkIt = False



nest = newNest(520, 300)



class sleepItem():

    def __init__(self, x, y, name, picture1, picture2, picture3, picture4):
        self.x = x
        self.y = y
        self.picture = [pygame.image.load(picture1), pygame.image.load(picture2), pygame.image.load(picture3), pygame.image.load(picture4)]
        self.itemLevel = 0
        self.cost = 10
        self.clicked = False
        self.maxLevel = 4
        self.width = self.picture[0].get_width()
        self.height = self.picture[0].get_height()
        self.name = name
        self.comfort = 10

    def drawSelf(self):
        if self.itemLevel < self.maxLevel:
            win.blit(self.picture[self.itemLevel], (self.x, self.y))
        else:
            win.blit(self.picture[self.itemLevel - 1], (self.x, self.y))
        font = pygame.font.SysFont("comicsans", 23, False)
        if self.itemLevel < self.maxLevel and self.itemLevel < nest.nestLevel:
            text = font.render(self.name + " £" + str(self.cost) + " +" + str(self.comfort) + " comfort", 1, (0,0,0))
            win.blit(text, (self.x, self.y + self.height))
        elif self.itemLevel < self.maxLevel and self.itemLevel >= nest.nestLevel:
            text = font.render("Buy a new nest first", 1, (0,0,0))
            win.blit(text, (self.x, self.y + self.height))
        else:
            text = font.render("Fully upgraded :-)", 1, (0,0,0))
            win.blit(text, (self.x, self.y + self.height))

    def checkSelf(self):
        global checkIt
        global mousex
        global mousey
        global money
        global totalComfort
        if checkIt == True:
            if mousex >= self.x and mousex <= self.x + self.width and mousey >= self.y and mousey <= self.y + self.height:
                if self.itemLevel < nest.nestLevel and money - self.cost >= 0 and self.itemLevel < self.maxLevel:
                    totalComfort += self.comfort
                    money -= self.cost
                    self.itemLevel += 1
                    self.cost += 10
                    self.comfort += 10
                    checkIt = False
                    

blanket = sleepItem(280,120, 'Blanket', 'blanket1.png', 'blanket2.png', 'blanket3.png', 'blanket4.png')
insulation = sleepItem(510,127, 'Insulation', 'fluff1.png', 'fluff1.png', 'fluff1.png', 'fluff1.png')
toy = sleepItem(300, 310, 'Toy', 'toy1.png', 'toy2.png', 'toy3.png', 'toy4.png')

def drawComfort():
    global totalComfort
    font = pygame.font.SysFont("comicsans", 60)
    text = font.render("Comfort: " + str(totalComfort), 1, (0,0,0))
    textwidth = text.get_width() 
    textheight = text.get_height() 
    halfrectx = int((textwidth + 10) / 2)
    halfrecty = int((textheight + 10) / 2)
    pygame.draw.rect(win, (135,206,235), (500 - halfrectx, 60, textwidth + 10, textheight  + 10))
    pygame.draw.rect(win, (65,105,225), (500 - halfrectx, 60, textwidth + 10, textheight + 10), 6)
    win.blit(text, (500 - halfrectx + 5, 65))
    

def sleepShopCheck():
    nest.checkSelf()
    blanket.checkSelf()
    insulation.checkSelf()
    toy.checkSelf()

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
    sleepButton.mainGameCheck()
    hungerButton.checkSelf()
    hygieneButton.checkSelf()
    sleepButton.checkSelf()
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
    win.fill([0,0,0,0])
    hygieneButton.drawShop()
    hygieneExit.drawSelf()
    pigeon1.drawSelf()
    drawDirt()
    checkDirt()

def sleepShopWin():
    win.fill([255,255,255])
    sleepButton.drawShop()
    sleepShopExit.drawSelf()
    sleepTimeButton.drawSelf()
    sleepTimeButton.drawText()
    nest.drawSelf()
    blanket.drawSelf()
    insulation.drawSelf()
    toy.drawSelf()
    drawComfort()


def sleepTimeWin():
    sleepBg = pygame.image.load('whitebg.png')
    win.fill([255,255,255])
    win.blit(sleepBg, (0,0))
    sleepTimeExit.drawSelf()
    sleepShopButton.drawSelf()
    sleepShopButton.drawText()
    


def allLoseLevel():
    hungerButton.loseLevel()
    hygieneButton.loseLevel()
    sleepButton.loseLevel()
    
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
    global money
    global totalComfort
    f = open("save.txt","w+")
    f.write(str(money))
    f.write("\n")
    f.write(str(int(hungerButton.level)))
    f.write("\n")
    f.write(str(int(hygieneButton.level)))
    f.write("\n")
    f.write(str(int(sleepButton.level)))
    f.write("\n")
    f.write(str(int(totalComfort)))
    f.write("\n")
    f.write(str(int(blanket.itemLevel)))
    f.write("\n")
    f.write(str(int(blanket.cost)))
    f.write("\n")
    f.write(str(int(blanket.comfort)))
    f.write("\n")
    f.write(str(int(insulation.itemLevel)))
    f.write("\n")
    f.write(str(int(insulation.cost)))
    f.write("\n")
    f.write(str(int(insulation.comfort)))
    f.write("\n")
    f.write(str(int(toy.itemLevel)))
    f.write("\n")
    f.write(str(int(toy.cost)))
    f.write("\n")
    f.write(str(int(toy.comfort)))
    f.write("\n")
    f.write(str(int(nest.nestLevel)))
    f.write("\n")
    f.write(str(int(nest.cost)))
    
    
    
    
    f.close()    
    

def load():
    global money
    global totalComfort
    f = open("save.txt","r")
    info = f.read()
    info = info.split("\n")
    money = int(info[0])
    hungerButton.level = int(info[1])
    hygieneButton.level = int(info[2])
    sleepButton.level = int(info[3])
    totalComfort = int(info[4])
    blanket.itemLevel = int(info[5])
    blanket.cost = int(info[6])
    blanket.comfort = int(info[7])
    insulation.itemLevel = int(info[8])
    insulation.cost = int(info[9])
    insulation.comfort = int(info[10])
    toy.itemLevel = int(info[11])
    toy.cost = int(info[12])
    toy.comfort = int(info[13])
    nest.nestLevel = int(info[14])
    nest.cost = int(info[15])



    
    
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


    while sleepButton.shopScreen:

        mouseChecked()
        sleepShopExit.checkSelf()
        sleepTimeButton.checkSelf()
        sleepShopCheck()
        

        if sleepShopExit.clicked:
            maingame = True
            sleepButton.shopScreen = False
            sleepScreen = False
            sleepShopExit.clicked = False
            pygame.display.update()

        elif sleepTimeButton.clicked:
            maingame = False
            sleepButton.shopScreen = False
            sleepScreen = True
            sleepTimeButton.clicked = False
            pygame.display.update()

        else:
            win.fill([255,255,255])
            sleepShopWin()
            pygame.display.update()

        allLoseLevel()


    while sleepScreen:
        mouseChecked()

        sleepTimeExit.checkSelf()

        sleepShopButton.checkSelf()

        if sleepTimeExit.clicked:
            sleepTimeExit.clicked = False
            sleepScreen = False
            maingame = True
            sleepButton.shopScreen = False
            pygame.display.update()
        elif sleepShopButton.clicked:
            sleepShopButton.clicked = False
            sleepScreen = False
            maingame = False
            sleepButton.shopScreen = True
            pygame.display.update()
        else:
            win.fill([255,255,255])
            sleepTimeWin()
            pygame.display.update()

        allLoseLevel()



        
        
        

    


        
        

        


        
        
    
              
    





    





    
    





    
    
       


import pygame
import time 
import random
pygame.init()


#global variables
global checkIt
global homescreen
global maingame
checkIt = False
homescreen = False
maingame = False
global mousex
global mousey
loseLevel = False
global money
money = 500


def drawMoney(x = 900,y = 30):
    global money
    
    font = pygame.font.SysFont("comicsans", 40)
    text = font.render(str(money), 1, (0, 0, 0))
    #win.f
    win.blit(text, (x, y))
    #pygame.display.update()




#creates a window with the homescreen as a background
win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Pigeon")
bg = [pygame.image.load("pigeon_home_screen.png"), pygame.image.load("pigeonmainscreenmockup.png")]

class rectButton():

    def __init__(self, text, x, y, width, height, r = 255 , g = 165, b = 0, fontsize = 55, fontr = 255, fontg = 255, fontb = 255):
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

    def drawSelf(self):
        pygame.draw.rect(win, (self.r, self.g, self.b), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)

    def drawText(self):
        font = pygame.font.SysFont("comicsans", self.fontsize)
        text = font.render(self.text, 1, (self.fontr, self.fontg, self.fontb))
        win.blit(text, (self.x + int(self.width / 4), self.y + int(self.height / 4)))

    def checkSelf(self):
        global mousex
        global mousey
        global checkIt
        if checkIt == True:
            if mousex >= self.x and mousex <= self.x + self.width and mousey >= self.y and mousey <= self.y + self.height:
                self.clicked = True
            





   
class careLevel(rectButton):

    def __init__(self, text, x, y, height, width, timeStays, shopPic, r = 255, g = 0, b = 0):
        self.level = 100.0
        self.timeStays = timeStays
        self.shopScreen = False
        self.shopPic = shopPic
        self.clicked = False
        super().__init__(text, x, y, height, width, r, g, b)
        

    def loseLevel(self):
        #global addLevel
        time.sleep(0.1)
        self.level -= self.timeStays / 10000.0
        
        #pygame.display.update()

    def drawLevel(self):
        #draws the level of the health, sleep etc
        if self.level <= 100:
            self.drawAmount = int((self.width / 100) * self.level)
            pygame.draw.rect(win, (0, 230, 0), (self.x, self.y, self.drawAmount, self.height))
            pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)
        if self.level > 100:
            pygame.draw.rect(win, (0, 230, 0), (self.x, self.y, 280, self.height))
            pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)
        

        
            
        
            
        #pygame.display.update()
        

    def checkShop(self):
        global maingame
        
        if self.clicked == True:
            
            self.shopScreen = True
            self.clicked = False
            maingame = False


    def drawShop(self):
        global maingame
        if self.shopScreen == True:
            win.blit(self.shopPic, (0,0))
            drawMoney(900, 30)
            #pygame.display.update()


    

    def mainGameCheck(self):
        self.drawSelf()
        self.drawLevel()
        self.drawText()
        self.checkShop()




        
class exitButton(careLevel):
    def __init__(self):
        self.clicked = False


    def drawSelf(self):
        pygame.draw.circle(win, (254,165,165), (45, 45), 30)
        pygame.draw.circle(win, (230,0,0), (45, 45), 30, 5)
        pygame.draw.line(win, (230, 0, 0), (35, 35), (55,55), 1)
        pygame.draw.line(win, (230, 0, 0), (35, 55), (55,35), 1)
        #pygame.display.update()

    def checkSelf(self):
        global mousex
        global mousey
        global checkIt
        if checkIt == True:
            if mousex >= 30 and mousex <= 60 and mousey >= 30 and mousey <= 60:
                self.clicked = True
        
#homescreen stuff        
playButton = rectButton('Play!',400, 350, 209, 60)
hungerButton = careLevel('Hunger', 37, 315, 280, 60, random.uniform(1000.0, 1010.0), pygame.image.load("foodShop.png"))
        


class shopItem():
    def __init__(self, x, y, picture, cost):#make an inventory to store stuff that's bought that isn't used right away
        self.x = x
        self.y = y
        self.picture = pygame.image.load(picture)
        self.cost = cost
        




    def drawSelf(self):
        
        
        win.blit(self.picture, (self.x,self.y))
        
        #pygame.draw.rect(win, (0,0,0), (self.x, self.y, 125, 150), 1 )




class foodItem(shopItem):

    def __init__(self,x,y, cost,hunger):#add a variable for how much hunger it solves
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
        
        
            


    

    
        
        


    
        
    
    
        
    






        
                


#the first time you click on the sleep column, you customise the nest
#pigeons eat seeds
#in toilet, might have to attach pigeon pants

#exit buttons
foodExit = exitButton()



#food shop items

food1 = foodItem(330,127, 25, 10)
food2 = foodItem(520,127, 50, 20)
food3 = foodItem(330,302, 100, 40)
food4 = foodItem(520,302, 200, 100)

    

            
def homescreenWindow(): 
    win.blit(bg[0], (0,0))
    playButton.drawSelf()
    playButton.drawText()
    playButton.checkSelf()
    #pygame.display.update()

def maingameWindow():
    win.blit(bg[1], (0,0))

    hungerButton.mainGameCheck()
    drawMoney()
    
    
    #pygame.display.update()



def foodShopWindow():

    
    win.fill([255,255,255])
    hungerButton.drawShop()
    #drawMoney()
    food1.drawSelf()
    food2.drawSelf()
    food3.drawSelf()
    food4.drawSelf()
    foodExit.drawSelf()
    
    
def allLoseLevel():
    hungerButton.loseLevel()
    
    
    











homescreen = True    
run = True
while run:
        
    
    while homescreen:



        #checks if mouse has been clicked
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #check if the play button has been clicked
                position = pygame.mouse.get_pos()
                mousex = position[0]
                mousey = position[1]
                checkIt = True
                

            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                

        if playButton.clicked == True:
            playButton.clicked = False
            homescreen = False
            maingame = True
            pygame.display.update()

        
        homescreenWindow()
        pygame.display.update()








    while maingame:


       

        #checks if mouse has been clicked
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                mousex = position[0]
                mousey = position[1]
                checkIt = True
                
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
        

        
        
        maingameWindow()
        allLoseLevel()
        hungerButton.checkSelf()
        pygame.display.update()
        









    while hungerButton.shopScreen:
        



        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                mousex = position[0]
                mousey = position[1]
                checkIt = True
                
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()


        food1.checkSelf()
        food2.checkSelf()
        food3.checkSelf()
        food4.checkSelf()
        

        foodExit.checkSelf()
        if foodExit.clicked == False:
            win.fill([255,255,255])
            foodShopWindow()
            pygame.display.update()
        else:
            hungerButton.shopScreen = False
            maingame = True
            foodExit.clicked = False
            pygame.display.update()

        allLoseLevel()


        #pygame.display.update()


        
        

        


        
        
    
              
    





    





    
    





    
    
       


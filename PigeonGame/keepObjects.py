import keepClasses as kc
import pygame
pygame.init()

# rectangular buttons
playButton = kc.RectButton((255, 140, 0), (400, 350, 209, 60), "Play!", 50)
instButton = kc.RectButton((255, 140, 0), (400, 420, 209, 60), "Instructions", 46)
# sleepTimeButton = kc.rectButton(
# sleepShopButton = kc.rectButton(

# care level buttons
hungerButton = kc.CareLevel((37, 320, 280, 60), "Hunger", 50, 300)
# hygieneButton = kc.CareLevel()
# sleepButton = kc.CareLevel()

# exit buttons
foodExit = kc.ExitButton()
instExit = kc.ExitButton()
mainExit = kc.ExitButton()
hygieneExit = kc.ExitButton()
sleepShopExit = kc.ExitButton()
sleepTimeExit = kc.ExitButton()

# food shop items
food1 = kc.FoodItem()
food2 = kc.FoodItem()
food3 = kc.FoodItem()
food4 = kc.FoodItem()

# the pigeon
pigeon1 = kc.Pigeon()

# to make the bird look dirtier
dirt1 = kc.Dirt()
dirt2 = kc.Dirt()
dirt3 = kc.Dirt()
dirt4 = kc.Dirt()


# the nest
nest = kc.NewNest()

# the nest items
blanket = kc.SleepItem()
insulation = kc.SleepItem()
toy = kc.SleepItem()

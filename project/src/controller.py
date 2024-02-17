# Matt: Following what I learned in CS110, we should be following MVC (model, view, controller).
# In this case the models are the structure of the game (sprites, buttons, etc.), the view is pygame, and the controller is this file which initializes and works with the two.

# import necessary files and modules
import pygame
import json
from src.upgrades import Upgrades

class Controller:
    # init
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode([960, 540])
        self.screen.fill("white")
        self.width, self.length = pygame.display.get_window_size()
        pygame.display.set_caption("HackBU clicker game")
        self.framerate = 60
        self.timer = pygame.time.Clock()

        self.data = {
            "score": 0,
            "upgrades": 0,
            "items": {
                "item1": 0,
                "item2": 0,
                "item3": 0,
                # ...
            },
            "robot": {
                "leg1": False,
                "leg2": False,
                "body": False,
                "arm1": False,
                "arm2": False,
                "head": False,
            },
            "platformer": False,
        }

        # self.saveload()
        
        increaseRate = 1
        self.score_increase = Upgrades(increaseRate)
        self.state = "MAIN"


    # the gameloop manages game state
    def gameloop(self):
        if self.state == "MAIN":
            self.mainloop()
        elif self.state == "PLACEHOLDER":
            self.placeholder()



    # mainloop is the main game (not the start, or end, etc.)
    def mainloop(self):


        running = True
        score = 0
        upgrade_price = 25
        multiplier = 1
        while running:
            # timer.tick(framerate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        #Clicker part
                        score = self.score_increase.scoreIncrease(score, multiplier)
                        print("Score: ", score)
                        print("multiplier1: ", multiplier)
                        print("Upgrade Cost: ", upgrade_price)
                    if event.key == pygame.K_LSHIFT:
                        #upgrades
                        print("run")
                        print("Score2: ", score)
                        if score >= upgrade_price:
                            score -= upgrade_price
                            multiplier = self.score_increase.multiplier(multiplier)
                            print("Multplier: ", multiplier)
                            upgrade_price = 25 * multiplier
                            print("Upgrade price: ", upgrade_price)
            pygame.display.flip()
        pygame.quit()

    

    def placeholder(self):
        pass
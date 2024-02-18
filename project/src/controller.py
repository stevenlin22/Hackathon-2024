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
        increaseRate = 1
        self.score_increase = Upgrades(increaseRate)

        self.data = {
            "score": 0,
            "upgrades": 0,
            "items": {
                "gear": 0,
                "wd40": 0,
                "cpu": 0,
                "thingy": 0,
                "wires": 0,
                "sheets": 0
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

        self.saveload()

        self.state = "MAIN"



    # the gameloop manages game state
    def gameloop(self):
        if self.state == "MAIN":
            self.mainloop()
        elif self.state == "PLACEHOLDER":
            self.placeholder()




    # mainloop is the main game (not the start, or end, etc.)
    def mainloop(self):

        score = self.data["score"]

        running = True
        upgrade_price = 25
        multiplier = 1
        parts = [1000, 2500, 10000, 50000, 100000, 1000000]
        while running:
            # timer.tick(framerate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open("data.txt", "w") as f:
                        json.dump(self.data, f)
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        #Clicker part
                        score = self.score_increase.scoreIncrease(score, multiplier)
                        self.data["score"] = score
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
                        print(score)
                    elif event.key == pygame.K_z: # add score requirement for below
                        if score >= parts[0]:
                            score -= parts[0]
                            self.data["robot"]["leg1"] = True
                    elif event.key == pygame.K_x:
                        if score >= parts[1]:
                            score -= parts[1]
                            self.data["robot"]["leg2"] = True
                    elif event.key == pygame.K_c:
                        if score >= parts[2]:
                            score -= parts[2]
                            self.data["robot"]["body"] = True
                    elif event.key == pygame.K_v:
                        if score >= parts[3]:
                            score -= parts[3]
                            self.data["robot"]["arm1"] = True
                    elif event.key == pygame.K_b:
                        if score >= parts[4]:
                            score -= parts[4]
                            self.data["robot"]["arm2"] = True
                    elif event.key == pygame.K_n:
                        if score >= parts[5]:
                            score -= parts[5]
                            self.data["robot"]["head"] = True
            pygame.display.flip()
        pygame.quit()

    

    def placeholder(self):
        pass

    def saveload(self):
        try:
            with open("data.txt") as f:
                self.data = json.load(f)
        except:
            with open("data.txt", "w") as f:
                json.dump(self.data, f)
# Matt: Following what I learned in CS110, we should be following MVC (model, view, controller).
# In this case the models are the structure of the game (sprites, buttons, etc.), the view is pygame, and the controller is this file which initializes and works with the two.

# import necessary files and modules
import pygame
import json

class Controller:
    # init
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode([300, 400])
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


        running = True
        while running:
            self.timer.tick(self.framerate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

        pygame.quit()

    

    def saveload(self):
        try:
            with open("data.txt") as f:
                self.data = json.load(f)
        except:
            with open("data.txt", "w") as f:
                json.dump(self.data, f)
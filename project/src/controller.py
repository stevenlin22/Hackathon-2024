# Matt: Following what I learned in CS110, we should be following MVC (model, view, controller).
# In this case the models are the structure of the game (sprites, buttons, etc.), the view is pygame, and the controller is this file which initializes and works with the two.

# import necessary files and modules
import pygame
from src.upgrades import Upgrades

class Controller:
    # init
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode([300, 400])
        self.screen.fill("white")
        self.width, self.length = pygame.display.get_window_size()
        pygame.display.set_caption("HackBU clicker game")
        self.framerate = 60
        self.timer = pygame.time.Clock()
        multiplier = 1
        increaseRate = 1
        self.score_increase = Upgrades(multiplier, increaseRate)
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
        while running:
            # timer.tick(framerate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score = self.score_increase.scoreIncrease(score)
                        print(score)
            pygame.display.flip()
        pygame.quit()

    def placeholder(self):
        pass
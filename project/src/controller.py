# Matt: Following what I learned in CS110, we should be following MVC (model, view, controller).
# In this case the models are the structure of the game (sprites, buttons, etc.), the view is pygame, and the controller is this file which initializes and works with the two.

# import necessary files and modules
import pygame

class Controller:
    # init
    def __init__(self):
        pygame.init()

        screen = pygame.display.set_mode([300, 400])
        pygame.display.set_caption("HackBU clicker game")

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False



        pygame.quit()
    
    # the gameloop manages game state
    def gameloop(self):
        pass
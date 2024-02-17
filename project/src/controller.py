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
        framerate = 60
        timer = pygame.time.Clock()

        self.state = "MAIN"


    # the gameloop manages game state
    def gameloop(self):
        
        if self.state = "MAIN":
            mainloop()
        elif self.state = "PLACEHOLDER":
            placeholder()


    

    # mainloop is the main game (not the start, or end, etc.)
    def mainloop(self):

        running = True
        while running:
            timer.tick(framerate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

        pygame.quit()

    

    def placeholder(self):
        pass
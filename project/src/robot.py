import pygame

class Robot:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
    def up(self):
        image = pygame.image.load("project/assets/robot_up.png")
        return image
    def down(self):
        image = pygame.image.load("project/assets/robot_down.png")
        return image
    def left(self):
        image = pygame.image.load("project/assets/robot_left.png")
        return image
    def right(self):
        image = pygame.image.load("project/assets/robot_right.png")
        return image
    def draw(self,screen, image):
        screen.blit(image, (self.x, self.y))
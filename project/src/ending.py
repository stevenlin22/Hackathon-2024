import pygame

class Background:
    def __init__(self, xpos, ypos, width, length):
        self.x = xpos
        self.y = ypos
        self.speed = 25
        self.width = width
        self.length = length
        self.bg_stretch = 1000
        self.image = pygame.image.load('project/assets/Flower_field.png')
        self.image = pygame.transform.scale(self.image, (self.width,self.length))

    def up(self):
        self.y += self.speed
        if self.y >= 0:
            self.y = -self.length + self.speed

    def down(self):
        self.y -= self.speed
        if self.y <= -self.length:
            self.y = -self.speed

    def right(self):
        self.x -= self.speed
        if self.x <= -self.width:
            self.x = -self.speed

    def left(self):
        self.x += self.speed
        if self.x >= 0:
            self.x = -self.width + self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x + self.width, self.y))
        screen.blit(self.image, (self.x + self.width, self.y + self.length))
        screen.blit(self.image, (self.x, self.y + self.length))
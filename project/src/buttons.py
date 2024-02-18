import pygame

class Button:

    def __init__(self, x, y, w, h, screen, cost, font, text, textsize, color="gray"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
        self.rect = pygame.Rect(x, y, w, h)
        self.center = self.rect.center
        self.font = pygame.font.Font(font, textsize)
        self.text = self.font.render(text, True, "black")
        self.cost = cost
        self.color = color

    def draw(self, score):
        if self.cost < score:
            self.color = "gray"
        else:
            self.color = "green"
            
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.center
        self.screen.blit(self.text, self.textRect)
        

    


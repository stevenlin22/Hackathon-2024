# main
import pygame
pygame.init()

screen = pygame.display.set_mode([300, 400])
pygame.display.set_caption("HackBU clicker game")

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



pygame.quit()
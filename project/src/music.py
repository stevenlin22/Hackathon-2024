import pygame

class Sound:
    def __init__(self):
        pass
    
    def play_music(self):
        pygame.mixer.music.load('project/assets/clicker_music.mp3')
        pygame.mixer.music.play()
    
    def tap_sound(self):
        tap_sound = pygame.mixer.Sound("project/assets/tap_sound.mp3")
        pygame.mixer.Sound.play(tap_sound)
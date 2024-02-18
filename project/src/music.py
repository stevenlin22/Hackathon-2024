import pygame

class Sound:
    def __init__(self):
        pass
    
    def play_music(self):
        pygame.mixer.music.load('project/assets/clicker_music.mp3')
        pygame.mixer.music.play()
    
    def tap_sound(self):
        tap_sound = pygame.mixer.Sound("project/assets/tap_sound.wav")
        pygame.mixer.Sound.play(tap_sound)
    def upgrade_sound(self):
        upgrade_sound = pygame.mixer.Sound("project/assets/upgrade_sound.wav")
        pygame.mixer.Sound.play(upgrade_sound)
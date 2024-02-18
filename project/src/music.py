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
    def part_sound(self):
        parts_sound = pygame.mixer.Sound("project/assets/Robot-parts.wav")
        pygame.mixer.Sound.play(parts_sound)
    def mute_key(self):
        is_playing = pygame.mixer.music.get_busy()
        if is_playing is True:
            pygame.mixer.music.pause()
        elif is_playing is False:
            pygame.mixer.music.play()
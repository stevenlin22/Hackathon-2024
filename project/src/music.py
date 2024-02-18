import pygame

class Sound:
    def __init__(self):
        pass
    
    def play_music(self):
        pygame.mixer.music.load('project/assets/clicker_music.mp3')
        pygame.mixer.music.play()
    def stop_music(self):
        pygame.mixer.music.unload()
    def ending_music(self):
        pygame.mixer.music.load('project/assets/ending.mp3')
        pygame.mixer.music.play()
    def tap_sound(self):
        tap_sound = pygame.mixer.Sound("project/assets/tap_sound.wav")
        pygame.mixer.Sound.play(tap_sound)
    def error_sound(self):
        error = pygame.mixer.Sound("project/assets/error.mp3")
        pygame.mixer.Sound.play(error)
    def upgrade_sound(self):
        upgrade_sound = pygame.mixer.Sound("project/assets/upgrade_sound.wav")
        pygame.mixer.Sound.play(upgrade_sound)
    def part_sound(self):
        parts_sound = pygame.mixer.Sound("project/assets/Robot-parts.wav")
        pygame.mixer.Sound.play(parts_sound)
    def boo_sound(self):
        boo_sound = pygame.mixer.Sound("project/assets/boo.mp3")
        pygame.mixer.Sound.play(boo_sound)
    def win_sound(self):
        win = pygame.mixer.Sound("project/assets/win.mp3")
        pygame.mixer.Sound.play(win)
    def mute_key(self):
        is_playing = pygame.mixer.music.get_busy()
        if is_playing is True:
            pygame.mixer.music.pause()
        elif is_playing is False:
            pygame.mixer.music.play()
    def mute_image(self):
        is_playing = pygame.mixer.music.get_busy()
        if is_playing is True:
            image = pygame.image.load("project/assets/sound_on.png")
        if is_playing is False:
            image = pygame.image.load("project/assets/mute.png")
        return image
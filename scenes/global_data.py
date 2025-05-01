import pygame
correct_answers_total = 0
trivia_completed = False
click_sound = None

def play_audio():
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(r"assets/audio/haptic.wav"))
        pygame.mixer.Channel(1).set_volume(0.05)
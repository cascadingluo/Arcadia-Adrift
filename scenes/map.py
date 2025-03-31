import pygame

class MapScene:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 40)

    def handle_event(self, event):
        pass  # handle clicks or transitions

    def update(self):
        pass

    def render(self, screen):
        screen.fill((100, 180, 255))  # ocean blue
        text = self.font.render("map screen", True, (0, 0, 0))
        screen.blit(text, (400, 300))

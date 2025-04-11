import pygame
from scenes.log import Log

class MapScene:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 40)
        self.button_rect = pygame.Rect(540, 475, 200, 80) #button for the log
        self.map_font = pygame.font.SysFont("Arial", 60)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: #check for click
            if self.button_rect.collidepoint(event.pos): #if the click is inside the button
                return Log()

    def update(self):
        pass

    def render(self, screen):
        screen.fill((100, 180, 255))  # ocean blue
        text = self.font.render("map screen", True, (0, 0, 0))
        screen.blit(text, (400, 300))

        pygame.draw.rect(screen, (230, 230, 230), self.button_rect, border_radius=20) #draws the start button
        start = self.font.render("log", True, (0, 0, 0)) #draws a text image that says start
        text_rect = start.get_rect(center=(screen.get_width() // 2, (screen.get_height() // 2) + 110))
        screen.blit(start, text_rect)


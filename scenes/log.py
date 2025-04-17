import pygame

class Log:
    def __init__(self, player_pos):
        self.player_pos = player_pos
        self.font = pygame.font.SysFont("Comic Sans MS", 60)
        self.button_rect = pygame.Rect(540, 540, 200, 80)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                from scenes.map import MapScene
                return MapScene(self.player_pos)  # just return to the map

    def update(self):
        pass

    def render(self, screen):
        screen.fill((150, 200, 255))
        pygame.draw.rect(screen, (230, 230, 230), self.button_rect, border_radius=20)
        text = self.font.render("Back to Map", True, (0, 0, 0))
        text_rect = text.get_rect(center=self.button_rect.center)
        screen.blit(text, text_rect)

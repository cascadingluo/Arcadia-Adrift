import pygame

class Trivia:

    def __init__(self, player_pos):
        self.player_pos = player_pos
        self.image = pygame.transform.scale(pygame.image.load(r"assets/images/oceanbg.png").convert(), (1280, 800))
        self.font = pygame.font.SysFont("Comic Sans MS", 25)
        self.button_rect = pygame.Rect(540, 400, 200, 80) #posistion and size of the map button

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                from scenes.map import MapScene
                return MapScene(self.player_pos)  # just return to the map
            
    def update(self): #runs every frame, will update accrodingly 
        pass
            
    def render(self, screen):

        screen.blit(self.image, (0,0))

        #button to go back to the screen
        pygame.draw.rect(screen, (230, 230, 230), self.button_rect, border_radius=20)
        text = self.font.render("skip", True, (0, 0, 0))
        text_rect = text.get_rect(center=self.button_rect.center)
        screen.blit(text, text_rect)
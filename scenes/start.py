import pygame
from scenes.map import MapScene

class StartScene:
    def __init__(self):
        self.font = pygame.font.SysFont("Comic Sans MS", 60)
        self.button_rect = pygame.Rect(540, 400, 200, 80) #posistion and size of the start button

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: #check for click
            if self.button_rect.collidepoint(event.pos): #if the click is inside the button
                return MapScene()

    def update(self): #runs every frame, will update accrodingly 
        pass

    def render(self, screen):
        screen.fill((150, 200, 255))  # ocean color
        pygame.draw.rect(screen, (230, 230, 230), self.button_rect, border_radius=20) #draws the start button
        text = self.font.render("Start", True, (0, 0, 0)) #draws a text image that says start
        screen.blit(text, (self.button_rect.x + 50, self.button_rect.y + 10)) #draws the text on top of the button 

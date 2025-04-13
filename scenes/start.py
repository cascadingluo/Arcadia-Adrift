import pygame
from scenes.map import MapScene

class StartScene:
    
    def __init__(self):
        
        self.font = pygame.font.SysFont("Comic Sans MS", 60)
        self.button_rect = pygame.Rect(540, 475, 200, 80) #posistion of the start button, the size
        self.title_font = pygame.font.SysFont("Comic Sana MS", 150) #create the title

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: #check for click
            if self.button_rect.collidepoint(event.pos): #if the click is inside the button
                return MapScene()

    def update(self): #runs every frame, will update accrodingly 
        pass

    def render(self, screen):
        screen.fill((150, 200, 255))  # fill the screen with the ocean color RGB 150, 200, 255

        pygame.draw.rect(screen, (230, 230, 230), self.button_rect, border_radius=20) #draws the start button
        start = self.font.render("Start", True, (0, 0, 0)) #draws a text image that says start
        text_rect = start.get_rect(center=(screen.get_width() // 2, (screen.get_height() // 2) + 110))
        screen.blit(start, text_rect)

        title_text = self.title_font.render("Arcadia Adrift", True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(screen.get_width() // 2, (screen.get_height() // 2) - 100))
        screen.blit(title_text, title_rect)
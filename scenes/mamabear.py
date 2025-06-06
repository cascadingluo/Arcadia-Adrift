import pygame
from scenes import global_data
class mamaBearScene:
    def __init__(self, player_pos):
        self.player_pos = player_pos
        self.image = pygame.transform.scale(pygame.image.load(r"assets/images/oceanbg.png").convert(), (1280, 800))
        self.font = pygame.font.SysFont("Comic Sans MS", 25)
        self.inst_font = pygame.font.SysFont("Comic Sans MS", 20)
        self.button_rect = pygame.Rect(1050, 30, 200, 80) #posistion and size of the map button
        self.character_name = "mama bear"
        self.haptic = pygame.mixer.music.load(r"assets/audio/haptic.wav")
        self.dialogue_box = pygame.Rect(300, 600, 950, 160)  
        self.name_font = pygame.font.SysFont("Comic Sans MS", 35)
        self.dialogue = [
            "My child… my child and I were separated because of the ice caps… ",
            "They have been melting from the temperatures over the last few years…",
            "My husband died a few days ago after being seperated from us on a hunt.",
            "Could you help us?",
            "To help us is easy… I found these riddles in a frozen cave a while back.",
            "I believe by being able to solve them… everything will return to as it once was…"
        ]
        self.dialogue_index = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                global_data.play_audio()
                if self.dialogue_index < len(self.dialogue) - 1:
                    self.dialogue_index += 1
                else:
                    from scenes.quiz import QuizScene
                    return QuizScene(self.player_pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            global_data.play_audio()
            if self.button_rect.collidepoint(event.pos):
                from scenes.map import MapScene
                return MapScene(self.player_pos)  # just return to the map
            else:
                if self.dialogue_index < len(self.dialogue) - 1:
                    self.dialogue_index += 1
                else:
                    from scenes.quiz import QuizScene
                    return QuizScene(self.player_pos)  # just return to the map after the dialgoue ends

    def update(self): #runs every frame, will update accrodingly 
        pass

    def render(self, screen):

        screen.blit(self.image, (0,0))

        #button to go back to the screen
        pygame.draw.rect(screen, (230, 230, 230), self.button_rect, border_radius=20)
        text = self.font.render("Back to Map", True, (0, 0, 0))
        text_rect = text.get_rect(center=self.button_rect.center)
        screen.blit(text, text_rect)
        
        #rendering the dialogue_box and dialogue
        pygame.draw.rect(screen, (200, 220, 255), self.dialogue_box, border_radius=20) #the box
        pygame.draw.rect(screen, (100, 100, 150), self.dialogue_box, 4, border_radius=20) #lining
        name_surface = self.name_font.render(self.character_name, True, (0, 0, 0))
        screen.blit(name_surface, (self.dialogue_box.x + 20, self.dialogue_box.y + 10))
        text_surface = self.font.render(self.dialogue[self.dialogue_index], True, (0, 0, 0))
        screen.blit(text_surface, (self.dialogue_box.x + 20, self.dialogue_box.y + 60))

        #render mama bear portrait
        mama_portrait  = pygame.transform.scale(pygame.image.load(r"assets/images/mama-bear-portrait.png").convert(), (266, 355))
        screen.blit(mama_portrait, (25, 400))
        
        #rendering the instructions 
        text = self.inst_font.render("click anywhere or press enter to continue the dialogue", True, (0, 0, 0))
        screen.blit(text, (735, 725))
import pygame
from scenes.bear import BearScene

class MapScene:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 14)
        self.player_pos = [600, 720]
        self.speed = 5
        self.image = pygame.transform.scale(pygame.image.load(r"assets\images\oceanbg.png").convert(), (1280, 800))
        self.player = pygame.image.load(r"assets\images\boat.jpg").convert_alpha()
        self.player = pygame.transform.scale(self.player, (20, 60))
        self.interact = False
        # right border
        self.b_rect1 = pygame.Rect(1200, 330, 380, 500)
        self.b_rect2 = pygame.Rect(780, 730, 200, 350)
        self.b_rect3 = pygame.Rect(1080, 400, 180, 500)
        self.b_rect4 = pygame.Rect(980, 500, 180, 500)
        self.b_rect5 = pygame.Rect(870, 570, 180, 500)
        # upper border
        self.b_rect_upper1 = pygame.Rect(800, 0, 1280, 235)
        self.b_rect_upper2 = pygame.Rect(0, 0, 1280, 170)
        #screen border
        self.b_rect_bottom = pygame.Rect(0, 799, 1080, 1)
        self.b_rect_east = pygame.Rect(1279, 0, 1, 800)
        #left border
        self.b_rect_left1 = pygame.Rect(0, 0, 350, 800)
        self.b_rect_left2 = pygame.Rect(0, 0, 450, 350)
        self.b_rect_left3 = pygame.Rect(0, 780, 400, 350)
        self.border_list = [self.b_rect1, self.b_rect2, self.b_rect3, self.b_rect4, self.b_rect5, self.b_rect_upper1, self.b_rect_upper2, 
                            self.b_rect_left1, self.b_rect_left2, self.b_rect_left3, self.b_rect_east, self.b_rect_bottom]
        #interaction
        self.interact_rect = pygame.Rect(700, 0, 300, 300)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: #check for click
            if self.interact_rect.collidepoint(event.pos) and self.interact: #if the click is on (!) && while in range
                return BearScene()

    def is_collision(self, p_rect):
        for border in self.border_list:
            if p_rect.colliderect(border):
                return True
    
    def update(self):
        keys = pygame.key.get_pressed()
        x = self.player_pos[0]
        y = self.player_pos[1]

        if keys[pygame.K_LEFT]:
            x -= self.speed
        if keys[pygame.K_RIGHT]:
            x += self.speed
        if keys[pygame.K_UP]:
            y -= self.speed
        if keys[pygame.K_DOWN]:
            y += self.speed

        p_rect = pygame.Rect(x, y, *self.player.get_size())

        # check for boundary before changing pos
        if not self.is_collision(p_rect):
            self.player_pos = [x, y]

        if p_rect.colliderect(self.interact_rect):
            self.interact = True
        else:
            self.interact = False

    def render(self, screen):
        screen.blit(self.image, (0,0))
        screen.blit(self.player, (self.player_pos[0], self.player_pos[1]))
        if self.interact: 
            text = self.font.render("Click (!) to interact", True, (0, 0, 0))
            screen.blit(text, (1000, 750))

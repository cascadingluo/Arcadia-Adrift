import pygame
from scenes import global_data
from scenes.log import Log
from scenes.mamabear import mamaBearScene
from scenes.babybear import babyBearScene
from scenes.success import successful

class MapScene:
    def __init__(self, player_pos=None):
        self.player_pos = player_pos if player_pos else [600, 720] #perserves the position of the boat from scene to scene
        self.notif_font = pygame.font.SysFont("Arial", 14)
        self.notif_font.set_bold(True)
        self.font = pygame.font.SysFont("Arial", 40)
        self.map_font = pygame.font.SysFont("Arial", 60)
        # self.player_pos = [600, 720] commented this out
        self.speed = 5
        if global_data.trivia_completed:
            self.image = pygame.transform.scale(pygame.image.load(r"assets/images/oceanbg-complete.png").convert(), (1280, 800))
        else:
            self.image = pygame.transform.scale(pygame.image.load(r"assets/images/oceanbg.png").convert(), (1280, 800))
        self.player = pygame.image.load(r"assets/images/boat.png").convert_alpha()
        self.player = pygame.transform.scale(self.player, (20, 60))
        self.interact = False
        self.baby_interact = False
        self.log_rect = pygame.Rect(1150, 30, 100, 80) #button for the log
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
        self.baby_interact_rect = pygame.Rect(150, 300, 300, 300)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.interact: #if enter is pressed && while in range
                global_data.play_audio()
                if not global_data.trivia_completed:
                    return mamaBearScene(self.player_pos)
                else: 
                    return successful(self.player_pos)
            elif event.key == pygame.K_RETURN and self.baby_interact and not global_data.trivia_completed: #if enter is pressed && while in range for the baby
                global_data.play_audio()
                return babyBearScene(self.player_pos)
        if event.type == pygame.MOUSEBUTTONDOWN: #check for click
            if self.interact_rect.collidepoint(event.pos) and self.interact: #if the click is on (!) && while in range
                global_data.play_audio()
                if not global_data.trivia_completed:
                    return mamaBearScene(self.player_pos)
                else:
                    return successful(self.player_pos)
            elif self.baby_interact_rect.collidepoint(event.pos) and self.baby_interact and not global_data.trivia_completed: 
                global_data.play_audio()
                return babyBearScene(self.player_pos)
            # elif self.log_rect.collidepoint(event.pos): #if the click is inside the button
            #     self.play_audio()
            #     return Log(self.player_pos)


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

        if p_rect.colliderect(self.baby_interact_rect):
            self.baby_interact = True
        else:
            self.baby_interact = False

    def render(self, screen):
        screen.blit(self.image, (0,0))
        screen.blit(self.player, (self.player_pos[0], self.player_pos[1]))
        
        # pygame.draw.rect(screen, (230, 230, 230), self.log_rect, border_radius=20) #draws the log button
        # start = self.font.render("log", True, (0, 0, 0)) #draws a text image that says log
        # text_rect = start.get_rect(center=self.log_rect.center)
        # screen.blit(start, text_rect)
        
        if self.interact and not global_data.trivia_completed: 
            text = self.notif_font.render("Click (!) or press enter to interact", True, (59, 101, 255))
            screen.blit(text, (800, 100))
        elif self.baby_interact and not global_data.trivia_completed:
            text = self.notif_font.render("Click (!) or press enter to interact", True, (59, 101, 255))
            screen.blit(text, (210, 450))
        elif self.interact and global_data.trivia_completed:
            notif = self.notif_font.render("You've completed the trivia challenge!", True, (59, 101, 255))
            screen.blit(notif, (800, 100))
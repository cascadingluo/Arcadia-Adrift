import pygame
from scenes.start import StartScene
from scenes.map import MapScene

pygame.init()
#initalize a window/screen for display
screen = pygame.display.set_mode((1280, 800)) #1280px by 800px
#track the in game clock between frames
clock = pygame.time.Clock()

current_scene = StartScene() 
#creates an instance of the start screen and handles whats shown and reactions when buttons are clicked

running = True

while running: #start runnign the game
    screen.fill((255, 255, 255)) 
    #fills the screen with a solid white color every frame
    #itll help clears the old frame before drawing a new one

    for event in pygame.event.get(): #takes in all the input events that happens
        if event.type == pygame.QUIT:
            running = False #if the user closes the window, the game will end
        next_scene = current_scene.handle_event(event) #passes events to the current screen
        if next_scene:
            current_scene = next_scene

    current_scene.update() #updates the game state
    current_scene.render(screen) #render the current screen 

    pygame.display.flip() #updates the screen
    clock.tick(60) #how many runs of the loop in a second, for now, lets do 60 FPS

pygame.quit()

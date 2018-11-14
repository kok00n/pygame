import pygame

# initialization of pygame module
pygame.init()

# definition of game main display
# we want to have resolution of the game to be 800 x 600
# it returns pygame.Surface object
gameDisplay = pygame.display.set_mode((800, 600))

# we define the title of the window
pygame.display.set_caption('A bit Racey')

# setting the game clock. It's used for tracking time within the game
clock = pygame.time.Clock()

crashed = False

# The game loop which will run until we crash
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

# updates specific area of the screen (display.flip() updates whole screen)
    pygame.display.update()
    clock.tick(60)

# quits pygame instance
pygame.quit()
quit()

import pygame
import time
import random


pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("A bit Racey")
clock = pygame.time.Clock()

car_speed = 0
car_width = 73

# We are loading racecar image to a variable
carImg = pygame.image.load('racecar.png').convert_alpha()


def things(thingx, thingy, thingw, thingh, color):
    # draw rectangle function parameters: where to draw/ what color/ location parameters
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


# car function places the car on the display
def car(x, y):
    # blit draws the image on the screen
    gameDisplay.blit(carImg, (x, y))


def crash():
    message_display('You Crashed')
    game_loop()


def message_display(text):
    # in Font we can specify font type and font size
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)


def text_objects(text, font):
    # True parameter stands for anti-aliasing
    textSurface = font.render(text, True, black)
    # get_rect() we get the position of rectangle
    return textSurface, textSurface.get_rect()


def game_loop():
    # definition of starting points for the car
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    # starting point of a block to be avoided
    thing_startx = random.randrange(0, display_width)
    # we want to start an object off the screen
    thing_starty = -600

    # how fast we want to an object to move
    thing_speed = 7

    # dimensions of an object
    thing_width = 100
    thing_height = 100

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        car(x, y)

        # if car cross the boundaries exit the game
        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()

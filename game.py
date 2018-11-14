import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("A bit Racey")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# We are loading racecar image to a variable
carImg = pygame.image.load('racecar.png')

# car function places the car on the display
def car(x, y):
    # blit draws the image on the screen
    gameDisplay.blit(carImg, (x, y))


# definition of starting points for the car
x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
car_speed = 0
car_width = 73

gameExit = False
clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

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
    car(x, y)

    # if car cross the boundaries exit the game
    if x > display_width - car_width or x < 0:
        gameExit = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

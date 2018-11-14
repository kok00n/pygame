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

crashed = False
clock = pygame.time.Clock()

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

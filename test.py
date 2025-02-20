import sys, pygame
pygame.init()

size = width, height = 1300, 800
speed = [5, 5]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ball = pygame.image.load("vangoon.jpg").convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    clock.tick(60)

    screen.fill(black)
    screen.blit(ball)
    pygame.display.flip()

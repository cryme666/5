import pygame
import sys
pygame.init()
WIDTH,HEIGHT = 800,600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('PING PONG')


while True:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,255,255))
    pygame.draw.circle(screen,(0,0,0),(0,0),100,5)

    pygame.display.flip()



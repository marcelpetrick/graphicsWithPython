import pygame, time
from pygame.locals import *

pygame.init()

RED = (255, 0, 0)
WHITE= (255, 255, 255)
BLACK = (0, 0, 0)

dialFIELD = pygame.display.set_mode((400, 400))
dialFIELD.fill(WHITE)
MX = 200
MY = 200
MP = ((MX, MY))

pygame.draw.circle(dialFIELD, BLACK, MP, 50)
pygame.draw.rect(dialFIELD, RED, (MX, MY,50,50))
pygame.draw.line(dialFIELD, BLACK, (50, 50), (300, 300), 4)

mainloop = True

while mainloop:
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                mainloop = False

pygame.quit()

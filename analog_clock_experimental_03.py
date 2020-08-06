import pygame, time
from pygame.locals import *
from math import sin, cos, radians

pygame.init()

RED = (255, 0, 0)
WHITE= (255, 255, 255)
BLACK = (0, 0, 0)

dialFIELD = pygame.display.set_mode((400, 400))
dialFIELD.fill(WHITE)

MX = 200
MY = 200
MP = ((MX, MY))

def dot(radius, angle):
    # draw a dot @ circumference wit radius and angle
    w1 = radians(angle * 6 - 90)
    x1 = int(MX + radius * cos(w1))
    y1 = int(MY + radius * sin(w1))
    return((x1, y1))

# pygame.draw.circle(dialFIELD, BLACK, dot(190, 2), 2)

for i in range(60):
    pygame.draw.circle(dialFIELD, BLACK, dot(190, i), 2)


for i in range(12):
    pygame.draw.circle(dialFIELD, BLACK, dot(190, i * 5), 4)


mainloop = True

while mainloop:

    currentTime = time.localtime()
    s = currentTime.tm_sec

    pygame.draw.circle(dialFIELD, WHITE, MP, 182)
    pygame.draw.line(dialFIELD, BLACK, MP, dot(120, 1), 6)
    pygame.draw.line(dialFIELD, BLACK, MP, dot(170, 2), 4)
    pygame.draw.line(dialFIELD, RED, MP, dot(180, s), 2)

    pygame.display.update()
    for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                mainloop = False

pygame.quit()

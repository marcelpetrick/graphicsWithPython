import pygame
import math
import time

def create_background(width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        background = pygame.Surface((width, height))
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(
                                background,
                                colors[(row + col) % 2],
                                pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width
        return background

def do_polygon_demo(surface, counter):
        color = (255, 255, 0) # yellow

        num_points = 8
        point_list = []
        center_x = surface.get_width() // 2
        center_y = surface.get_height() // 2
        for i in range(num_points * 2):
                radius = 100
                if i % 2 == 0:
                        radius = radius // 2
                ang = i * 3.14159 / num_points + counter * 3.14159 / 60
                x = center_x + int(math.cos(ang) * radius)
                y = center_y + int(math.sin(ang) * radius)
                point_list.append((x, y))
        pygame.draw.polygon(surface, color, point_list)

width =400
height = 300
fps = 60

pygame.init()
screen = pygame.display.set_mode((width, height))
background = create_background(width, height)
clock = pygame.time.Clock()


for cnt in range(1, 1000):
        screen.blit(background, (0, 0))

        # do_rectangle_demo, do_circle_demo, do_horrible_outlines,
        # do_nice_outlines, do_polygon_demo, do_line_demo

        do_polygon_demo(screen, cnt)
        pygame.display.flip()
        clock.tick(fps)

pygame.quit()


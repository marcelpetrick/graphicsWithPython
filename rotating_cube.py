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

def rotate_3d_points(points, angle_x, angle_y, angle_z):
        new_points = []
        for point in points:
                x = point[0]
                y = point[1]
                z = point[2]
                new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
                new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
                y = new_y
                z = new_z
                new_x = x * math.cos(angle_y) - z * math.sin(angle_y)
                new_z = x * math.sin(angle_y) + z * math.cos(angle_y)
                x = new_x
                z = new_z
                new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
                new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
                x = new_x
                y = new_y
                new_points.append([x, y, z])
        return new_points

def do_line_demo(surface, counter):
        color = (0, 0, 0) # black
        cube_points = [ [-1, -1, 1], [-1, 1, 1], [1, 1, 1],
                        [1, -1, 1], [-1, -1, -1], [-1, 1, -1],
                        [1, 1, -1], [1, -1, -1]]

        connections = [ (0, 1), (1, 2), (2, 3), (3, 0), (4, 5),
                        (5, 6), (6, 7), (7, 4), (0, 4), (1, 5),
                        (2, 6), (3, 7)
                        ]

        t = counter * 2 * 3.14159 / 60 # this angle is 1 rotation per second

        # rotate about x axis every 2 seconds
        # rotate about y axis every 4 seconds
        # rotate about z axis every 6 seconds
        points = rotate_3d_points(cube_points, t / 2, t / 4, t / 6)
        flattened_points = []
        for point in points:
                flattened_points.append(
                        (point[0] * (1 + 1.0 / (point[2] + 3)),
                         point[1] * (1 + 1.0 / (point[2] + 3))))

        for con in connections:
                p1 = flattened_points[con[0]]
                p2 = flattened_points[con[1]]
                x1 = p1[0] * 60 + 200
                y1 = p1[1] * 60 + 150
                x2 = p2[0] * 60 + 200
                y2 = p2[1] * 60 + 150

                pygame.draw.line(surface, color, (x1, y1), (x2, y2), 4)

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

        do_line_demo(screen, cnt)
        pygame.display.flip()
        clock.tick(fps)

pygame.quit()




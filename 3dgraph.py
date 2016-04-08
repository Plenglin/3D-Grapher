import math
import pprint
import sys
import time

import pygame

import matrix
import transform

turnrate = math.pi/16

# change me!
function = lambda x, y: math.cos(x) - math.sin(y)

pitch = 0
roll = 0
yaw = 0
xMin = -10
xMax = 10
yMin = -10
yMax = 10
xStep = .5
yStep = .5

def generate3dPoints(func, xMin, xMax, yMin, yMax, xStep, yStep):
    x = xMin
    values = []
    while x <= xMax:
        a = []
        y = yMin
        while y <= yMax:
            try:
                a.append(matrix.columnvec(x, y, func(x, y), 1))
            except ZeroDivisionError:
                a.append(matrix.columnvec(x, y, 0, 0))
            y += yStep
        values.append(a)
        x += xStep
    return values

def render(display, points):
    display.fill((0, 0, 0))
    transformation = transform.scale3(40, 40, 300) * transform.translate3(15, 15, 0) * transform.rotate3(-roll, -yaw, -pitch)
    p = [[transformation * j for j in i] for i in points]
    for i in range(0, len(p) - 1):
        for j in range(0, len(p[0]) - 1):
            pygame.draw.line(display, (255,255,255), (p[i][j][0,0], p[i][j][0,1]), (p[i+1][j][0,0], p[i+1][j][0,1]))
            pygame.draw.line(display, (255,255,255), (p[i][j][0,0], p[i][j][0,1]), (p[i][j+1][0,0], p[i][j+1][0,1]))

    o = transformation * matrix.columnvec(0, 0, 0, 1)
    x = transformation * matrix.columnvec(20, 0, 0, 1)
    y = transformation * matrix.columnvec(0, 20, 0, 1)
    z = transformation * matrix.columnvec(0, 0, 20, 1)
    pygame.draw.line(display, (255,0,0), (o[0,0], o[0,1]), (x[0,0], x[0,1]))
    pygame.draw.line(display, (0,255,0), (o[0,0], o[0,1]), (y[0,0], y[0,1]))
    pygame.draw.line(display, (0,0,255), (o[0,0], o[0,1]), (z[0,0], z[0,1]))

def main():
    global pitch, roll, yaw
    pygame.init()
    pygame.display.set_caption('3d graph')
    display = pygame.display.set_mode((1280, 1024))
    display.fill((0, 0, 0))
    points = generate3dPoints(function, xMin, xMax, yMin, yMax, xStep, yStep)
    render(display, points)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    yaw -= turnrate
                elif event.key == pygame.K_d:
                    yaw += turnrate
                elif event.key== pygame.K_w:
                    pitch += turnrate
                elif event.key == pygame.K_s:
                    pitch -= turnrate
                elif event.key== pygame.K_q:
                    roll += turnrate
                elif event.key == pygame.K_e:
                    roll -= turnrate
                render(display, points)
        pygame.display.update()

if __name__ == '__main__':
    main()

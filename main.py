import pygame
import numpy as np
import random
import matplotlib.pyplot as plt
from Examples import Point
from Examples import Examples
from MLP import MLP

startX = 318
startY = 230
armLength = 100.0

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([600,500])
examples = Examples(armLength).Generation(10000)

def Translation(center, angle):
    x = Point(center.x + armLength * np.sin(angle), center.y - armLength * np.cos(angle))
    return x

def FindPoints(angles):
    alpha = np.pi - angles[0]
    beta = angles[1] * (-1.0)
    point1 = Translation(Point(startX, startY), alpha)
    point2 = Translation(point1, np.pi - beta + alpha)
    return point1, point2

def Unstandarization(angles):
    return np.array(angles) * np.pi

def DrawLearningPoints():
    for p in examples[0]:
        pygame.draw.circle(screen, (128,0,128), (p[0] + startX, p[1] + startY), 1.1)
    
def main():
    trainX = (np.array(examples[0]) + armLength * 2) / (armLength * 4) * 0.8 + 0.1
    trainY = np.array(examples[1]) / np.pi * 0.8 + 0.1
    mlp = MLP()

    for i in range(10000):
        mlp.Learning(trainX, trainY)
    
    errors = mlp.errors
    plt.plot(range(len(errors)), errors)
    plt.show()
    
    screen.fill((255,255,255))
    image = pygame.image.load('robot.jpg')
    screen.blit(image, (0,0))
    pygame.display.flip()
    run = True

    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            elif e.type == pygame.MOUSEMOTION:
                position = pygame.mouse.get_pos()
                x = position[0] - startX
                y = position[1] - startY

                predict = Unstandarization(mlp.Forward(((x + armLength * 2)/(armLength * 4) * 0.8 + 0.1, (-y + armLength * 2)/(armLength * 4) * 0.8 + 0.1)))
                points = FindPoints(predict)

                screen.fill((255,255,255))
                image = pygame.image.load('robot.jpg')
                screen.blit(image, (0,0))
                pygame.draw.line(screen, (255,0,255), (startX, startY), (points[0].x, points[0].y), width=4)
                pygame.draw.line(screen, (255,0,255), (points[0].x, points[0].y), (points[1].x, points[1].y), width=4)
                DrawLearningPoints()
                pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
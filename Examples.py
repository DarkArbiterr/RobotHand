import numpy as np
import matplotlib.pyplot as plt

class Point(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Examples(object):

    def __init__(self, armLength = 10):
        self.input = []
        self.output = []
        self.armLength = armLength
        self.center = Point(0, 0)

    def Translation(self, center, angle):
        x = Point(center.x + self.armLength * np.sin(angle), center.y - self.armLength * np.cos(angle))
        return x

    def PointGeneration(self):
        alpha = np.random.random() * np.pi
        beta = np.random.random() * np.pi
        self.output.append([alpha, beta])
        tPoint = self.Translation(self.center, alpha)
        fPoint = self.Translation(tPoint, np.pi - beta + alpha)
        return fPoint

    def Generation(self, examplesNumber):
        for i in range(examplesNumber):
            p = self.PointGeneration()
            self.input.append([p.x, p.y])
        return self.input, self.output
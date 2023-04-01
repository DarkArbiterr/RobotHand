from turtle import dot
import numpy as np
import matplotlib.pyplot as plt

class MLP(object):

    def __init__(self, learningEta=0.01):
        self.inputLayer = 2
        self.hiddenLayer1 = 10
        self.hiddenLayer2 = 6
        self.outputLayer = 2
        self.learningEta = learningEta
        self.errors = []
        self.weights1 = np.random.randn(self.inputLayer, self.hiddenLayer1)
        self.weights2 = np.random.randn(self.hiddenLayer1, self.hiddenLayer2)
        self.weights3 = np.random.randn(self.hiddenLayer2, self.outputLayer)

    def Sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))
    
    def DerivativeSigmoid(self, x):
        return x * (1 - x)

    def Forward(self, x):
        self.y0 = np.array(x).copy()
        self.a1 = np.dot(self.y0, self.weights1)
        self.y1 = self.Sigmoid(self.a1)
        self.a2 = np.dot(self.y1, self.weights2)
        self.y2 = self.Sigmoid(self.a2)
        self.a3 = np.dot(self.y2, self.weights3)
        self.y3 = self.Sigmoid(self.a3)
        return self.y3

    def Backward(self, out):
        self.epsilon3 = out - self.y3
        self.delta3 = self.epsilon3 * self.DerivativeSigmoid(self.y3)
        self.epsilon2 = self.delta3.dot(self.weights3.T)
        self.delta2 = self.epsilon2 * self.DerivativeSigmoid(self.y2)
        self.epsilon1 = self.delta2.dot(self.weights2.T)
        self.delta1 = self.epsilon1 * self.DerivativeSigmoid(self.y1)

        self.weights3 += self.learningEta * self.y2.T.dot(self.delta3)
        self.weights2 += self.learningEta * self.y1.T.dot(self.delta2)
        self.weights1 += self.learningEta * self.y0.T.dot(self.delta1)

    def Learning(self, x, y):
        self.Forward(x)
        self.Backward(y)
        self.errors.append(np.mean(np.square(y - self.y3)) * 100)

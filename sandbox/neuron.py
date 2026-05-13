import random
import math

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

        self.learning_rate = 0.1

        self.result = None
    
    def feedforward(self, x, y):
        self.result = (x * self.weights[0]) + (y * self.weights[1]) + self.bias
        self.result = 1/(1 + math.exp(-self.result))
        return self.result
    
    def correction(self, pair, answer):
        error = answer - self.result

        for i in range(len(self.weights)):
            adjustment = error * (self.result * (1 - self.result)) * pair[i] * self.learning_rate
            self.weights[i] += adjustment
        
        self.bias += error * (self.result * (1 - self.result)) * self.learning_rate

brain = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))

data = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 1], 1)
]
for test in range(5000):
    if (test + 1) % 100 == 0:
        print(f'Цикл {test + 1}')
    for pair, target in data:
        brain.feedforward(pair[0], pair[1])
        brain.correction(pair, target)
        brain.feedforward(pair[0], pair[1])
    if (test + 1) % 100 == 0:
        print(f'Сумма ошибки - {target - brain.result}')

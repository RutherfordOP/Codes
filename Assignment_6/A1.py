import math
#A1
#a)
def summation_unit(inputs, weights):
    return sum(i * w for i, w in zip(inputs, weights))
#b1) Step Function
def step_function(x):
    return 1 if x >= 0 else 0
#b2)Biolar Step Function
def bipolar_step_function(x):
    return 1 if x >= 0 else -1
#b3)Sigmoid Function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
#b4)TanH Function
def tanh(x):
    return math.tanh(x)
#b5)ReLU Function
def relu(x):
    return max(0, x)
#b6)Leaky ReLU functions
def leaky_relu(x, alpha=0.01):
    return x if x > 0 else alpha * x
#c)

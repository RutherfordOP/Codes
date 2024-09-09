import numpy as np
import matplotlib.pyplot as plt

W0 = -0.25
W1 = 0.5
W2 = 0.75
alpha = 0.1

def step_function(x):
    return 1 if x >= 0 else 0


def perceptron(x1, x2, W0, W1, W2):
    return step_function(W0 + W1 * x1 + W2 * x2)


training_data = [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1)
]


def train_perceptron(epochs):
    global W0, W1, W2
    errors = []
    for epoch in range(epochs):
        total_error = 0
        for x1, x2, target in training_data:
            output = perceptron(x1, x2, W0, W1, W2)
            error = target - output
            W0 += alpha * error
            W1 += alpha * error * x1
            W2 += alpha * error * x2
            total_error += error ** 2
        errors.append(total_error)
        if total_error <= 0.002:
            break
    return errors, epoch + 1


errors, epochs = train_perceptron(1000)


plt.plot(range(epochs), errors)
plt.xlabel('Epochs')
plt.ylabel('Sum-Square Error')
plt.title('Epochs vs Sum-Square Error')
plt.show()

print(f'Weights converged after {epochs} epochs.')

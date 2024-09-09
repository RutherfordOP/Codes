import numpy as np
import matplotlib.pyplot as plt


initial_W0 = -0.25
initial_W1 = 0.5
initial_W2 = 0.75


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


def train_perceptron(learning_rate, epochs=1000):
    W0, W1, W2 = initial_W0, initial_W1, initial_W2
    for epoch in range(epochs):
        total_error = 0
        for x1, x2, target in training_data:
            output = perceptron(x1, x2, W0, W1, W2)
            error = target - output
            W0 += learning_rate * error
            W1 += learning_rate * error * x1
            W2 += learning_rate * error * x2
            total_error += error ** 2
        if total_error <= 0.002:
            return epoch + 1
    return epochs

learning_rates = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
epochs_to_converge = []


for lr in learning_rates:
    epochs = train_perceptron(lr)
    epochs_to_converge.append(epochs)


plt.plot(learning_rates, epochs_to_converge, marker='o')
plt.xlabel('Learning Rate')
plt.ylabel('Epochs to Converge')
plt.title('Learning Rate vs Epochs to Converge')
plt.grid(True)
plt.show()

print(f'Learning rates: {learning_rates}')
print(f'Epochs to converge: {epochs_to_converge}')

import numpy as np
import matplotlib.pyplot as plt


W0 = -0.25
W1 = 0.5
W2 = 0.75
alpha = 0.1


def bipolar_step_function(x):
    return 1 if x >= 0 else -1


def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))

def relu_function(x):
    return max(0, x)


def perceptron(x1, x2, W0, W1, W2, activation_function):
    return activation_function(W0 + W1 * x1 + W2 * x2)


training_data = [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1)
]


def train_perceptron(epochs, activation_function):
    global W0, W1, W2
    errors = []
    for epoch in range(epochs):
        total_error = 0
        for x1, x2, target in training_data:
            output = perceptron(x1, x2, W0, W1, W2, activation_function)
            error = target - output
            W0 += alpha * error
            W1 += alpha * error * x1
            W2 += alpha * error * x2
            total_error += error ** 2
        errors.append(total_error)
        if total_error <= 0.002:
            break
    return errors, epoch + 1


epochs = 1000
errors_bipolar, epochs_bipolar = train_perceptron(epochs, bipolar_step_function)
errors_sigmoid, epochs_sigmoid = train_perceptron(epochs, sigmoid_function)
errors_relu, epochs_relu = train_perceptron(epochs, relu_function)


plt.plot(range(epochs_bipolar), errors_bipolar, label='Bi-Polar Step')
plt.plot(range(epochs_sigmoid), errors_sigmoid, label='Sigmoid')
plt.plot(range(epochs_relu), errors_relu, label='ReLU')
plt.xlabel('Epochs')
plt.ylabel('Sum-Square Error')
plt.title('Epochs vs Sum-Square Error for Different Activation Functions')
plt.legend()
plt.show()

print(f'Bi-Polar Step function converged after {epochs_bipolar} epochs.')
print(f'Sigmoid function converged after {epochs_sigmoid} epochs.')
print(f'ReLU function converged after {epochs_relu} epochs.')

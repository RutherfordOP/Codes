import numpy as np
import matplotlib.pyplot as plt


initial_W0 = -0.25
initial_W1 = 0.5
initial_W2 = 0.75
alpha = 0.1


training_data = [
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 0)
]


def summation_unit(inputs, weights, bias):
    return np.dot(inputs, weights) + bias


def step_function(x):
    return 1 if x >= 0 else 0

def bipolar_step_function(x):
    return 1 if x >= 0 else -1

def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))

def tanh_function(x):
    return np.tanh(x)

def relu_function(x):
    return max(0, x)

def leaky_relu_function(x, alpha=0.01):
    return x if x >= 0 else alpha * x


def comparator_unit(target, output):
    return target - output


def train_perceptron(epochs, activation_function):
    W0, W1, W2 = initial_W0, initial_W1, initial_W2
    errors = []
    for epoch in range(epochs):
        total_error = 0
        for x1, x2, target in training_data:
            inputs = np.array([x1, x2])
            weights = np.array([W1, W2])
            summation = summation_unit(inputs, weights, W0)
            output = activation_function(summation)
            error = comparator_unit(target, output)
            W0 += alpha * error
            W1 += alpha * error * x1
            W2 += alpha * error * x2
            total_error += error ** 2
        errors.append(total_error)
        if total_error == 0:
            break
    return errors, epoch + 1


epochs = 1000
errors_step, epochs_step = train_perceptron(epochs, step_function)
errors_bipolar, epochs_bipolar = train_perceptron(epochs, bipolar_step_function)
errors_sigmoid, epochs_sigmoid = train_perceptron(epochs, sigmoid_function)
errors_tanh, epochs_tanh = train_perceptron(epochs, tanh_function)
errors_relu, epochs_relu = train_perceptron(epochs, relu_function)
errors_leaky_relu, epochs_leaky_relu = train_perceptron(epochs, leaky_relu_function)


plt.plot(range(epochs_step), errors_step, label='Step')
plt.plot(range(epochs_bipolar), errors_bipolar, label='Bi-Polar Step')
plt.plot(range(epochs_sigmoid), errors_sigmoid, label='Sigmoid')
plt.plot(range(epochs_tanh), errors_tanh, label='TanH')
plt.plot(range(epochs_relu), errors_relu, label='ReLU')
plt.plot(range(epochs_leaky_relu), errors_leaky_relu, label='Leaky ReLU')
plt.xlabel('Epochs')
plt.ylabel('Sum-Square Error')
plt.title('Epochs vs Sum-Square Error for Different Activation Functions (XOR Gate)')
plt.legend()
plt.show()

print(f'Step function converged after {epochs_step} epochs.')
print(f'Bi-Polar Step function converged after {epochs_bipolar} epochs.')
print(f'Sigmoid function converged after {epochs_sigmoid} epochs.')
print(f'TanH function converged after {epochs_tanh} epochs.')
print(f'ReLU function converged after {epochs_relu} epochs.')
print(f'Leaky ReLU function converged after {epochs_leaky_relu} epochs.')

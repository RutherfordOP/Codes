import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

outputs = np.array([[0], [0], [0], [1]])


np.random.seed(1)
weights_input_hidden = 2 * np.random.random((2, 2)) - 1
weights_hidden_output = 2 * np.random.random((2, 1)) - 1

learning_rate = 0.05
max_iterations = 1000
error_threshold = 0.002

for iteration in range(max_iterations):

    hidden_layer_input = np.dot(inputs, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    final_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    final_layer_output = sigmoid(final_layer_input)
    

    error = outputs - final_layer_output
    if np.mean(np.abs(error)) <= error_threshold:
        print(f"Converged after {iteration} iterations")
        break
    

    final_layer_delta = error * sigmoid_derivative(final_layer_output)
    hidden_layer_error = final_layer_delta.dot(weights_hidden_output.T)
    hidden_layer_delta = hidden_layer_error * sigmoid_derivative(hidden_layer_output)
    
    weights_hidden_output += hidden_layer_output.T.dot(final_layer_delta) * learning_rate
    weights_input_hidden += inputs.T.dot(hidden_layer_delta) * learning_rate

print("Trained weights (input to hidden):")
print(weights_input_hidden)
print("Trained weights (hidden to output):")
print(weights_hidden_output)

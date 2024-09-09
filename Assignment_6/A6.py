import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


X = np.array([
    [20, 6, 2, 386],
    [16, 3, 6, 289],
    [27, 6, 2, 393],
    [19, 1, 2, 110],
    [24, 4, 2, 280],
    [22, 1, 5, 167],
    [15, 4, 2, 271],
    [18, 4, 2, 274],
    [21, 1, 4, 148],
    [16, 2, 4, 198]
])


y = np.array([[1], [1], [1], [0], [1], [0], [1], [1], [0], [0]])


weights = np.random.rand(X.shape[1], 1)
learning_rate = 0.1
epochs = 10000


for epoch in range(epochs):
    
    inputs = X
    weighted_sum = np.dot(inputs, weights)
    activated_output = sigmoid(weighted_sum)
    

    error = y - activated_output
    
  
    adjustments = error * sigmoid_derivative(activated_output)
    weights += np.dot(inputs.T, adjustments) * learning_rate


print("Trained weights:\n", weights)


new_data = np.array([25, 5, 3, 350])
result = sigmoid(np.dot(new_data, weights))
print("Transaction value (High=1, Low=0):", result)

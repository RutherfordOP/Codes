import numpy as np

    
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


X_bias = np.hstack((np.ones((X.shape[0], 1)), X))


X_pseudo_inverse = np.linalg.pinv(X_bias)


weights_pseudo_inverse = np.dot(X_pseudo_inverse, y)


print("Weights from pseudo-inverse method:\n", weights_pseudo_inverse)


new_data = np.array([1, 25, 5, 3, 350])  
result = np.dot(new_data, weights_pseudo_inverse)
print("Transaction value (High=1, Low=0):", result)

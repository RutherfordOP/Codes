from sklearn.neural_network import MLPClassifier
import numpy as np

inputs_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs_and = np.array([0, 0, 0, 1])

inputs_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs_xor = np.array([0, 1, 1, 0])

mlp_and = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', learning_rate_init=0.05, max_iter=1000)
mlp_and.fit(inputs_and, outputs_and)

mlp_xor = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', learning_rate_init=0.05, max_iter=1000)
mlp_xor.fit(inputs_xor, outputs_xor)

print("AND Gate Predictions:")
print(mlp_and.predict(inputs_and))

print("XOR Gate Predictions:")
print(mlp_xor.predict(inputs_xor))

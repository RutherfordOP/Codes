import matplotlib.pyplot as plt
import numpy as np


X = np.random.randint(1, 11, size=(20, 2))


classes = ['Class0' if sum(point) <= 10 else 'Class1' for point in X]

for point, classification in zip(X, classes):
    if classification == 'Class0':
        plt.scatter(point[0], point[1], c='blue', label='Class0' if 'Class0' not in plt.gca().get_legend_handles_labels()[1] else "")
    else:
        plt.scatter(point[0], point[1], c='red', label='Class1' if 'Class1' not in plt.gca().get_legend_handles_labels()[1] else "")

plt.xlabel('Feature X')
plt.ylabel('Feature Y')
plt.title('Scatter Plot of Training Data')
plt.legend()
plt.show()

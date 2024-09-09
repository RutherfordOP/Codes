import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

X_train = np.random.randint(1, 11, size=(20, 2))
y_train = np.array([0 if sum(point) <= 10 else 1 for point in X_train])

x_test = np.arange(0, 10.1, 0.1)
y_test = np.arange(0, 10.1, 0.1)
X_test = np.array([[x, y] for x in x_test for y in y_test])

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

for point, prediction in zip(X_test, y_pred):
    if prediction == 0:
        plt.scatter(point[0], point[1], c='blue', s=1)
    else:
        plt.scatter(point[0], point[1], c='red', s=1)

plt.xlabel('Feature X')
plt.ylabel('Feature Y')
plt.title('kNN Classification of Test Data')
plt.show()

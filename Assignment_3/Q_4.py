import matplotlib.pyplot as plt

feature = 'Income'  # Change this to any feature you want to analyze
data = X[feature]

# Plot histogram
plt.hist(data, bins=30, edgecolor='black')
plt.title(f'Histogram of {feature}')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Calculate mean and variance
mean = np.mean(data)
variance = np.var(data)
print(f"Mean of {feature}: {mean}")
print(f"Variance of {feature}: {variance}")


def minkowski_distance(x1, x2, r):
    return np.linalg.norm(x1 - x2, ord=r)

feature_vector_1 = X.iloc[0].values
feature_vector_2 = X.iloc[1].values
r_values = range(1, 11)
distances = [minkowski_distance(feature_vector_1, feature_vector_2, r) for r in r_values]

plt.plot(r_values, distances, marker='o')
plt.title('Minkowski Distance vs. r')
plt.xlabel('r')
plt.ylabel('Distance')
plt.show()

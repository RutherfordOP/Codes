from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

distortions = []
k_values = range(2, 20)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_train)
    distortions.append(kmeans.inertia_)

plt.plot(k_values, distortions, 'bx-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Distortion')
plt.title('Elbow Method For Optimal k')
plt.show()

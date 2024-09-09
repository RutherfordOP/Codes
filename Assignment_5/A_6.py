from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

scores = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data)
    scores.append(kmeans.inertia_)

plt.plot(k_values, scores, 'bx-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Elbow Score')
plt.title('Elbow Method For Optimal k')
plt.show()

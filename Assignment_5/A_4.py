from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X_train)

labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

print("Cluster Labels:", labels)
print("Cluster Centers:\n", cluster_centers)

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

kmeans = KMeans(n_clusters=2, random_state=42).fit(X_train)

silhouette = silhouette_score(X_train, kmeans.labels_)
calinski_harabasz = calinski_harabasz_score(X_train, kmeans.labels_)
davies_bouldin = davies_bouldin_score(X_train, kmeans.labels_)

print(f"Silhouette Score: {silhouette}")
print(f"Calinski-Harabasz Score: {calinski_harabasz}")
print(f"Davies-Bouldin Score: {davies_bouldin}")

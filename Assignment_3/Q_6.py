# Train kNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Test accuracy
accuracy = knn.score(X_test, y_test)
print(f"Accuracy of kNN (k=3): {accuracy:.2f}")

# Predict using the kNN classifier
predictions = knn.predict(X_test)
print("Predictions on test set:", predictions)

# Confusion matrix
cm = confusion_matrix(y_test, predictions)
print("Confusion Matrix:")
print(cm)

# Classification report
report = classification_report(y_test, predictions)
print("Classification Report:")
print(report)

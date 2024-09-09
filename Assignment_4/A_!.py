from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

conf_matrix_train = confusion_matrix(y_true_train, y_pred_train)
precision_train = precision_score(y_true_train, y_pred_train)
recall_train = recall_score(y_true_train, y_pred_train)
f1score_train = f1_score(y_true_train, y_pred_train)

conf_matrix_test = confusion_matrix(y_true_test, y_pred_test)
precision_test = precision_score(y_true_test, y_pred_test)
recall_test = recall_score(y_true_test, y_pred_test)
f1score_test = f1_score(y_true_test, y_pred_test)

print("Training Data Metrics:")
print("Confusion Matrix:\n", conf_matrix_train)
print("Precision:", precision_train)
print("Recall:", recall_train)
print("F1-Score:", f1score_train)

print("\nTest Data Metrics:")
print("Confusion Matrix:\n", conf_matrix_test)
print("Precision:", precision_test)
print("Recall:", recall_test)
print("F1-Score:", f1score_test)

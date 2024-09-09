from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

rmse_train = np.sqrt(mean_squared_error(y_train_true, y_train_pred))
rmsle_train = np.sqrt(mean_squared_error(np.log1p(y_train_true), np.log1p(y_train_pred)))
mae_train = mean_absolute_error(y_train_true, y_train_pred)
r2_train = r2_score(y_train_true, y_train_pred)

rmse_test = np.sqrt(mean_squared_error(y_test_true, y_test_pred))
rmsle_test = np.sqrt(mean_squared_error(np.log1p(y_test_true), np.log1p(y_test_pred)))
mae_test = mean_absolute_error(y_test_true, y_test_pred)
r2_test = r2_score(y_test_true, y_test_pred)

print("Training Data Metrics:")
print(f"RMSE: {rmse_train}")
print(f"RMSLE: {rmsle_train}")
print(f"MAE: {mae_train}")
print(f"R² Score: {r2_train}")

print("\nTest Data Metrics:")
print(f"RMSE: {rmse_test}")
print(f"RMSLE: {rmsle_test}")
print(f"MAE: {mae_test}")
print(f"R² Score: {r2_test}")

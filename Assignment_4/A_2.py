from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np


y_true = [...]  
y_pred = [...]  

mse = mean_squared_error(y_true, y_pred)

rmse = np.sqrt(mse)

mae = mean_absolute_error(y_true, y_pred)

r2 = r2_score(y_true, y_pred)

print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"MAE: {mae}")
print(f"R² Score: {r2}")

if r2 < 0.5:
    print("The model may be underfitting.")
elif r2 > 0.9:
    print("The model may be overfitting.")
else:
    print("The model seems to have a regular fit.")

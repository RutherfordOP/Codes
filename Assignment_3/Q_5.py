import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('Lab Session Data.xlsx', sheet_name='marketing_campaign')

# Extract features and labels
X = df.drop('Response', axis=1).select_dtypes(include=[np.number])  # Use only numerical features
y = df['Response']

# Handle missing values by imputing with the mean
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.3, stratify=y)

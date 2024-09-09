import pandas as pd
import numpy as np

# Load dataset
df = pd.read_excel('Lab Session Data.xlsx', sheet_name='marketing_campaign')

# Extract features and labels
X = df.drop('Response', axis=1).select_dtypes(include=[np.number])  # Use only numerical features
y = df['Response']

def calculate_intraclass_interclass(X, y):
    classes = y.unique()
    class_means = {}
    class_spreads = {}

    for cls in classes:
        class_data = X[y == cls]
        class_means[cls] = class_data.mean(axis=0)
        class_spreads[cls] = class_data.std(axis=0)

    interclass_distances = {}
    for cls1 in classes:
        for cls2 in classes:
            if cls1 != cls2:
                distance = np.linalg.norm(class_means[cls1] - class_means[cls2])
                interclass_distances[(cls1, cls2)] = distance

    return class_means, class_spreads, interclass_distances

class_means, class_spreads, interclass_distances = calculate_intraclass_interclass(X, y)
print("Class Means:", class_means)
print("Class Spreads:", class_spreads)
print("Interclass Distances:", interclass_distances)

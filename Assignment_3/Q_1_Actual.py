import pandas as pd

# Load dataset from the specific sheet
df = pd.read_excel('Lab Session Data.xlsx', sheet_name='marketing_campaign')

# Extract features and labels
X = df.drop('Year_Birth', axis=1)
y = df['Year_Birth']

# Display column names and the first few rows
print(df.columns)

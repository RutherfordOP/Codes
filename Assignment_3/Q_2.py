import pandas as pd

# Load dataset
df = pd.read_excel('Lab Session Data.xlsx', sheet_name='marketing_campaign')

# Display unique classes in the Response column
unique_classes = df['Response'].unique()
print("Unique classes in the 'Response' column:", unique_classes)

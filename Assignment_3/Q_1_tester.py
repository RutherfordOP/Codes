import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the Excel sheet, specifying that the column names are in the 6th row (index 5)
file_path = 'Project-Management-Sample-Data.xlsx'
df = pd.read_excel(file_path, header=5)
#File bpathi

# Select only the "District Name" and "Chloride (mg/L)" columns
selected_columns = df[['Project Name', 'Days Required']]

# Group by district and calculate the mean chloride level for each district
grouped_df = selected_columns.groupby('Project Name').mean().reset_index()

# Define acceptable and unacceptable classes based on chloride level
acceptable_class = grouped_df[grouped_df['Days Required']]


# Calculate the mean (centroid) for each class
acceptable_mean = acceptable_class['Days Required'].mean(axis=0)


# Calculate the spread (standard deviation) for each class
acceptable_std = acceptable_class['Days Required)'].std(axis=0)

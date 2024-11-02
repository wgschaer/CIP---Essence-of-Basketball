import pandas as pd

# Load the MVP data from the CSV file
file_path = "D:/MDS 2024/2nd Semester/CIP02 Data Collection, Integration and Preprocessing/CIP---Essence-of-Basketball/Sabin/nba_mvp_data_1999_2023.csv"
mvp_data = pd.read_csv(file_path)

# Filter data for the relevant columns
metrics_columns = ['PTS', 'TRB', 'AST', 'STL', 'BLK', 'FG%', '3P%', 'FT%', 'WS', 'WS/48']
mvp_stats = mvp_data[metrics_columns]

# Convert columns to numeric, replacing any non-numeric values
mvp_stats = mvp_stats.apply(pd.to_numeric, errors='coerce')

# Calculate the mean and standard deviation for each metric
stats_summary = mvp_stats.describe().loc[['mean', 'std']]

# Display the results to the user
print(stats_summary)

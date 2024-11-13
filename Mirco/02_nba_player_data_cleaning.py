import pandas as pd

# Load the dataset
file_path = 'data/nba_player_stats_combined_2004_2024.csv'
data = pd.read_csv(file_path)

# Step 1: Remove unnecessary columns
data = data.drop(columns=['Unnamed: 0'])

# Step 2: Handle missing values
# Although the data does not have missing values, let's handle it as a precaution
data = data.dropna()  # Drop rows with any missing values

# Step 3: Standardize column names
data.columns = data.columns.str.lower().str.replace(' ', '_')

# Step 4: Ensure numeric columns are properly formatted
numeric_columns = [
    'age', 'gp', 'w', 'l', 'min', 'pts', 'fgm', 'fga', 'fg%', '3pm', '3pa', '3p%',
    'ftm', 'fta', 'ft%', 'oreb', 'dreb', 'reb', 'ast', 'tov', 'stl', 'blk', 'pf',
    'fp', 'dd2', 'td3', '+/-'
]
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Step 5: Remove duplicate rows
data = data.drop_duplicates()

# Step 6: Save the cleaned data
cleaned_file_path = 'data/nba_player_stats_cleaned.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Data cleaning completed. Cleaned data saved to {cleaned_file_path}.")

# Import necessary libraries
import pandas as pd

# Load the NBA dataset
file_path = "data/nba_team_stats_2004_2024.csv"
nba_data = pd.read_csv(file_path)

# 1. Remove unnecessary columns
if "Unnamed: 0" in nba_data.columns:
    nba_data.drop(columns=["Unnamed: 0"], inplace=True)
print("Step 1: Removed unnecessary columns if present.")

# 2. Handle missing data
missing_values_before = nba_data.isnull().sum().sum()
print(f"Step 2: Checked for missing values. Total missing values before cleaning: {missing_values_before}")

# 3. Data Type Correction
print("Step 3: Data types before correction:")
print(nba_data.dtypes)

# Define a dictionary for type conversion and apply it
type_conversion = {
    'POSS': 'int64',
    'GP': 'int64',
    'W': 'int64',
    'L': 'int64',
    'MIN': 'float64',
    'Season': 'str'
}

# Remove commas from 'POSS' and apply type conversion
nba_data['POSS'] = pd.to_numeric(nba_data['POSS'].astype(str).str.replace(",", ""), errors='coerce')
for col, dtype in type_conversion.items():
    if col in nba_data.columns:
        nba_data[col] = nba_data[col].astype(dtype)

# Display data types after correction
print("Data types after correction:")
print(nba_data.dtypes)

# 4. Filter data based on expected ranges using boolean indexing
initial_row_count = nba_data.shape[0]
nba_data = nba_data[(nba_data['GP'] > 0) & (nba_data['W'] >= 0) & (nba_data['L'] >= 0)]
nba_data = nba_data[(nba_data['eFG%'] >= 0) & (nba_data['eFG%'] <= 100)]
nba_data = nba_data[(nba_data['TS%'] >= 0) & (nba_data['TS%'] <= 100)]
filtered_row_count = nba_data.shape[0]
print(f"Step 4: Filtered data based on expected value ranges. Rows reduced from {initial_row_count} to "
      f"{filtered_row_count}.")

# 5. Data Enrichment: Calculate Win Percentage
nba_data['Win%'] = (nba_data['W'] / nba_data['GP'] * 100).round(2)
print("Step 5: Added 'Win%' column for data enrichment (rounded to 2 decimal places).")

# 6. Final Check for Missing Values
missing_values_after = nba_data.isnull().sum().sum()
print(f"Step 6: Final check completed. Total missing values after cleaning: {missing_values_after}")

# 7. Save the cleaned dataset
output_file_path = "data/cleaned_nba_team_stats_2004_2024.csv"
nba_data.to_csv(output_file_path, index=False)
print(f"Step 7: Cleaned dataset has been saved to {output_file_path}")

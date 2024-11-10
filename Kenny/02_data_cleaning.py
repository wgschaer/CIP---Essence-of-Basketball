# Import necessary libraries
import pandas as pd

# Load the NBA dataset from the updated file path
file_path = "data/nba_team_stats_2004_2024.csv"
nba_data = pd.read_csv(file_path)

# 1. Remove unnecessary columns
nba_data.drop(columns=["Unnamed: 0"], inplace=True)
print("Step 1: Removed unnecessary columns.")

# 2. Handle missing data
missing_values_before = nba_data.isnull().sum().sum()
print(f"Step 2: Checked for missing values. Total missing values before cleaning: {missing_values_before}")

# 3. Data Type Correction (Including removal of commas from 'POSS')
print("Step 3: Data types before correction:")
print(nba_data.dtypes)

# Remove commas from 'POSS' and convert it to numeric
nba_data['POSS'] = pd.to_numeric(nba_data['POSS'].astype(str).str.replace(",", ""), errors='coerce')

# Convert other columns to the correct data types
nba_data['GP'] = pd.to_numeric(nba_data['GP'], errors='coerce')
nba_data['W'] = pd.to_numeric(nba_data['W'], errors='coerce')
nba_data['L'] = pd.to_numeric(nba_data['L'], errors='coerce')
nba_data['MIN'] = pd.to_numeric(nba_data['MIN'], errors='coerce')
nba_data['Season'] = nba_data['Season'].astype(str)

# Display data types after correction
print("Data types after correction:")
print(nba_data.dtypes)

# 4. Check if values lie in the expected range
initial_row_count = nba_data.shape[0]
nba_data = nba_data[(nba_data['GP'] > 0) & (nba_data['W'] >= 0) & (nba_data['L'] >= 0)]
nba_data = nba_data[(nba_data['eFG%'] >= 0) & (nba_data['eFG%'] <= 100)]
nba_data = nba_data[(nba_data['TS%'] >= 0) & (nba_data['TS%'] <= 100)]
filtered_row_count = nba_data.shape[0]
print(f"Step 4: Filtered data based on expected value ranges. Rows reduced from {initial_row_count} to {filtered_row_count}.")

# 5. Data Enrichment
nba_data['Win%'] = ((nba_data['W'] / nba_data['GP']) * 100).round(2)
print("Step 5: Added 'Win%' column for data enrichment (rounded to 2 decimal places).")

# 6. Final Check
missing_values_after = nba_data.isnull().sum().sum()
print(f"Step 6: Final check completed. Total missing values after cleaning: {missing_values_after}")

# 7. Save the cleaned dataset to a CSV file with the updated file path
output_file_path = "data/cleaned_nba_team_stats_2004_2024.csv"
nba_data.to_csv(output_file_path, index=False)
print(f"Step 7: Cleaned dataset has been saved to {output_file_path}")

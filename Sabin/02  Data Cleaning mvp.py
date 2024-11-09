
import pandas as pd

# Load the data from CSV files
# Load the MVP data
mvp_df = pd.read_csv('data/nba_mvp_data_1999_2024.csv')
print("MVP Data - First 5 Rows:")
print(mvp_df.head())
print("\nMissing Values in MVP Data:")
print(mvp_df.isnull().sum()) #checking for missing values

# Load the Champions data
champions_df = pd.read_csv('data/nba_champions_1999_2024.csv')
print("\nChampions Data - First 5 Rows:")
print(champions_df.head())
print("\nMissing Values in Champions Data:")
print(champions_df.isnull().sum())

## Merging and dropping the unnecessary columns:
# Step 1: Extract the ending year from the 'Season' column (e.g., "2023-24" becomes "2024")
mvp_df['Season'] = mvp_df['Season'].apply(lambda x: int(x.split('-')[1]) + 2000 if '-' in x else int(x))

# Step 2: Rename 'Season' to 'Year' to match the Champions DataFrame
mvp_df.rename(columns={'Season': 'Year'}, inplace=True)

# Step 3: Convert 'Year' to integer type for consistency
mvp_df['Year'] = mvp_df['Year'].astype(int)

# Display the first few rows to confirm the changes
print("\nUpdated MVP Data:")
print(mvp_df.head())
print(mvp_df.dtypes)


# Step 4: Merge the MVP and Champions DataFrames on the 'Year' column
merged_df = pd.merge(mvp_df, champions_df, on='Year', how='inner')

# Step 5: Display the first few rows of the merged DataFrame to confirm
print("\nMerged DataFrame - First 5 Rows:")
print(merged_df.head())

# Step 3: Display the column names in the merged DataFrame
print("\nColumns in Merged DataFrame:")
print(merged_df.columns)



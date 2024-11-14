import pandas as pd
from unidecode import unidecode

# Step 1: Load the MVP dataset
mvp_df = pd.read_csv('../Sabin/data/cleaned_nba_data_mvp_with_teams.csv')
print("MVP Dataset - First 5 Rows:")
print(mvp_df.head())
print("\nColumns in MVP Dataset:", mvp_df.columns)

# Step 2: Load the player stats dataset
player_stats_df = pd.read_csv('data/nba_player_stats_cleaned.csv')
print("\nPlayer Stats Dataset - First 5 Rows:")
print(player_stats_df.head())
print("\nColumns in Player Stats Dataset:", player_stats_df.columns)

# Step 3: Check the unique player names in both datasets
print("\nUnique MVP names in MVP Dataset:")
print(mvp_df['Season MVP'].unique())

print("\nUnique player names in Player Stats Dataset:")
print(player_stats_df['player'].unique()[:10])  # Display first 10 player names for reference

# Step 4: Create a mapping dictionary to convert abbreviated MVP names to full names
mvp_name_mapping = {
    'N. Jokic': 'Nikola Jokic',
    'J. Embiid': 'Joel Embiid',
    'G. Antetokounmpo': 'Giannis Antetokounmpo',
    'J. Harden': 'James Harden',
    'R. Westbrook': 'Russell Westbrook',
    'S. Curry': 'Stephen Curry',
    'K. Durant': 'Kevin Durant',
    'L. James': 'LeBron James',
    'D. Rose': 'Derrick Rose',
    'K. Bryant': 'Kobe Bryant',
    'D. Nowitzki': 'Dirk Nowitzki',
    'S. Nash': 'Steve Nash'
}

# Step 5: Clean the 'Season MVP' column using the mapping dictionary
mvp_df['Full Name'] = mvp_df['Season MVP'].map(mvp_name_mapping)

# Step 6: Ensure player names are cleaned in the player stats dataset using `unidecode`
player_stats_df['player'] = player_stats_df['player'].apply(lambda x: unidecode(x) if isinstance(x, str) else x)

# Step 7: Extract the ending year from the 'season' column in the player stats dataset
player_stats_df['Year'] = player_stats_df['season'].apply(lambda x: int(x.split('-')[0]) + 1)

# Step 8: Merge the two datasets on 'Full Name' and 'Year'
merged_mvp_positions = pd.merge(
    mvp_df,
    player_stats_df[['player', 'team', 'Year', 'position']],
    left_on=['Full Name', 'Year'],
    right_on=['player', 'Year'],
    how='left'
)

# Step 9: Drop unnecessary columns including 'Champion Team'
merged_mvp_positions.drop(columns=['Champion Team'], inplace=True)

# Step 10: Rename the 'position' column to 'Position' (with a capital P)
merged_mvp_positions.rename(columns={'position': 'Position'}, inplace=True)

# Step 11: Filter the final columns to keep only relevant information
final_df = merged_mvp_positions[['Year', 'Season MVP', 'Full Name', 'MVP Team', 'Position']]

# Display the merged data with positions
print("\nMVP Data with Positions - First 5 Rows:")
print(final_df.head())

# Save the cleaned data to a new CSV file
final_df.to_csv('data/mvp_with_positions_cleaned.csv', index=False)
print("\nFiltered data saved to 'data/mvp_with_positions_cleaned.csv'")

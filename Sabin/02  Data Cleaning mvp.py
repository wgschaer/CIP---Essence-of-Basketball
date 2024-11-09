import pandas as pd
from unidecode import unidecode

# Step 1: Load the MVP and Champions data
mvp_df = pd.read_csv('data/nba_mvp_data_2004_2024.csv')
champions_df = pd.read_csv('data/nba_champions_2004_2024.csv')

# Step 2: Extract the ending year from the 'Season' column (e.g., "2023-24" becomes "2024") and convert to integer
mvp_df['Season'] = mvp_df['Season'].apply(lambda x: int(x.split('-')[1]) + 2000 if '-' in x else int(x))
mvp_df.rename(columns={'Season': 'Year'}, inplace=True)

# Step 3: Merge the MVP and Champions DataFrames on the 'Year' column
merged_df = pd.merge(mvp_df, champions_df, on='Year', how='inner')

# Step 4: Drop unnecessary columns
columns_to_drop = ['Lg', 'Voting', 'League', 'Points Leader', 'Rebounds Leader',
                   'Assists Leader', 'Win Shares Leader']
merged_df.drop(columns=columns_to_drop, inplace=True)

# Step 5: Clean player names and finals MVP names using `unidecode`
merged_df['Player'] = merged_df['Player'].apply(lambda x: unidecode(x) if isinstance(x, str) else x)
merged_df['Finals MVP'] = merged_df['Finals MVP'].apply(lambda x: unidecode(x) if isinstance(x, str) else x)

# Step 6: Rename 'Player' to 'Season MVP' and format names
merged_df.rename(columns={'Player': 'Season MVP'}, inplace=True)

# Function to format names to "F. Last"
def format_name(name):
    if isinstance(name, str):
        parts = name.split()
        if len(parts) == 2:  # Check if there are exactly two parts
            return f"{parts[0][0]}. {parts[1]}"
    return name

# Apply formatting to the 'Season MVP' column
merged_df['Season MVP'] = merged_df['Season MVP'].apply(format_name)

# Step 7: Rename 'Tm' to 'Team' and convert abbreviations to full team names
merged_df.rename(columns={'Tm': 'Team'}, inplace=True)

# Dictionary to map team abbreviations to full names
team_mapping = {
    'ATL': 'Atlanta Hawks',
    'BOS': 'Boston Celtics',
    'BKN': 'Brooklyn Nets',
    'CHA': 'Charlotte Hornets',
    'CHI': 'Chicago Bulls',
    'CLE': 'Cleveland Cavaliers',
    'DAL': 'Dallas Mavericks',
    'DEN': 'Denver Nuggets',
    'DET': 'Detroit Pistons',
    'GSW': 'Golden State Warriors',
    'HOU': 'Houston Rockets',
    'IND': 'Indiana Pacers',
    'LAC': 'Los Angeles Clippers',
    'LAL': 'Los Angeles Lakers',
    'MEM': 'Memphis Grizzlies',
    'MIA': 'Miami Heat',
    'MIL': 'Milwaukee Bucks',
    'MIN': 'Minnesota Timberwolves',
    'NOP': 'New Orleans Pelicans',
    'NYK': 'New York Knicks',
    'OKC': 'Oklahoma City Thunder',
    'ORL': 'Orlando Magic',
    'PHI': 'Philadelphia 76ers',
    'PHO': 'Phoenix Suns',
    'POR': 'Portland Trail Blazers',
    'SAC': 'Sacramento Kings',
    'SAS': 'San Antonio Spurs',
    'TOR': 'Toronto Raptors',
    'UTA': 'Utah Jazz',
    'WAS': 'Washington Wizards'
}

# Apply the team mapping
merged_df['Team'] = merged_df['Team'].map(team_mapping)

# Step 8: Display the final cleaned data
print("\nCleaned Merged Data - First 5 Rows:")
print(merged_df[['Year', 'Season MVP', 'Team', 'Champion', 'Finals MVP', 'PTS', 'TRB', 'AST']].head())

# Step 9: Save the cleaned data to a new CSV file
final_output_path = 'data/cleaned_nba_data_final_with_teams.csv'
merged_df.to_csv(final_output_path, index=False)
print(f"\nCleaned data saved to '{final_output_path}'")
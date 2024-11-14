# Import necessary libraries
import pandas as pd
import os

# Step 1: Load the dataset
file_path = 'data/nba_player_stats_combined_2004_2024.csv'
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

data = pd.read_csv(file_path)

# Step 2: Remove unnecessary columns
data = data.drop(columns=['Unnamed: 0'])

# Step 3: Handle missing values
data = data.dropna()  # Drop rows with any missing values

# Step 4: Standardize column names
data.columns = data.columns.str.lower().str.replace(' ', '_')

# Step 5: Replace position letters with full words
position_mapping = {'F': 'Forward', 'G': 'Guard', 'C': 'Center'}
data['position'] = data['position'].map(position_mapping)

# Step 6: Replace team abbreviations with full names (sorted alphabetically)
team_mapping = {
    'ATL': 'Atlanta Hawks', 'BOS': 'Boston Celtics', 'BKN': 'Brooklyn Nets',
    'CHA': 'Charlotte Hornets', 'CHI': 'Chicago Bulls', 'CLE': 'Cleveland Cavaliers',
    'DAL': 'Dallas Mavericks', 'DEN': 'Denver Nuggets', 'DET': 'Detroit Pistons',
    'GSW': 'Golden State Warriors', 'HOU': 'Houston Rockets', 'IND': 'Indiana Pacers',
    'LAC': 'Los Angeles Clippers', 'LAL': 'Los Angeles Lakers', 'MEM': 'Memphis Grizzlies',
    'MIA': 'Miami Heat', 'MIL': 'Milwaukee Bucks', 'MIN': 'Minnesota Timberwolves',
    'NJN': 'New Jersey Nets', 'NOH': 'New Orleans Hornets', 'NOP': 'New Orleans Pelicans',
    'NYK': 'New York Knicks', 'OKC': 'Oklahoma City Thunder', 'ORL': 'Orlando Magic',
    'PHI': 'Philadelphia 76ers', 'PHX': 'Phoenix Suns', 'POR': 'Portland Trail Blazers',
    'SAC': 'Sacramento Kings', 'SAS': 'San Antonio Spurs', 'SEA': 'Seattle SuperSonics',
    'TOR': 'Toronto Raptors', 'UTA': 'Utah Jazz', 'WAS': 'Washington Wizards'
}
data['team'] = data['team'].map(team_mapping)

# Step 7: Ensure numeric columns are properly formatted
numeric_columns = [
    'age', 'gp', 'w', 'l', 'min', 'pts', 'fgm', 'fga', 'fg%', '3pm', '3pa', '3p%',
    'ftm', 'fta', 'ft%', 'oreb', 'dreb', 'reb', 'ast', 'tov', 'stl', 'blk', 'pf',
    'fp', 'dd2', 'td3', '+/-'
]
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Step 8: Remove duplicate rows
data = data.drop_duplicates()

# Step 9: Save the cleaned data
cleaned_file_path = 'data/cleaned_nba_player_stats_2004_2024.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Data cleaning completed. Cleaned data saved to {cleaned_file_path}.")

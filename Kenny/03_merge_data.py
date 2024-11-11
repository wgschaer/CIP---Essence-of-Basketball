# Import necessary libraries
import pandas as pd
import os

# Create the 'data' folder if it doesn't exist
os.makedirs("../data", exist_ok=True)

# Load the new MVP dataset and the team stats dataset
mvp_stats_file = "../Sabin/data/cleaned_nba_data_mvp_with_teams.csv"
team_stats_file = "data/cleaned_nba_team_stats_2004_2024.csv"

# Read the CSV files
mvp_stats = pd.read_csv(mvp_stats_file)
team_stats = pd.read_csv(team_stats_file)

# Define the Year-to-Season mapping
year_to_season_mapping = {
    2005: "2004-05", 2006: "2005-06", 2007: "2006-07", 2008: "2007-08",
    2009: "2008-09", 2010: "2009-10", 2011: "2010-11", 2012: "2011-12",
    2013: "2012-13", 2014: "2013-14", 2015: "2014-15", 2016: "2015-16",
    2017: "2016-17", 2018: "2017-18", 2019: "2018-19", 2020: "2019-20",
    2021: "2020-21", 2022: "2021-22", 2023: "2022-23", 2024: "2023-24"
}

# Step 1: Map the 'Year' column in mvp_stats to 'Season' using the dictionary
mvp_stats['Season'] = mvp_stats['Year'].map(year_to_season_mapping)

# Step 2: Standardize column names by converting to lowercase and stripping whitespace
mvp_stats.columns = mvp_stats.columns.str.strip().str.lower()
team_stats.columns = team_stats.columns.str.strip().str.lower()

# Step 3: Extract the list of MVP teams from the mvp_stats dataset
mvp_teams = mvp_stats[['season', 'mvp team']].drop_duplicates().set_index('season')['mvp team'].to_dict()

# Step 4: Merge the datasets on 'season' and 'team', excluding the 'mvp team' column in the output
try:
    merged_data = pd.merge(team_stats, mvp_stats[['season', 'mvp team']].drop_duplicates(), left_on=["season", "team"], right_on=["season", "mvp team"], how="left")
    print("Merging successful.")

    # Step 5: Create the 'is_mvp_team' column based on the MVP teams
    merged_data['is_mvp_team'] = merged_data['team'].eq(merged_data['season'].map(mvp_teams))

    # Step 6: Drop the 'mvp team' column from the merged dataset
    merged_data.drop(columns=['mvp team'], inplace=True)

    # Step 7: Save the merged dataset without the 'mvp team' column
    merged_output_path = "data/merged_nba_data_with_mvp_status.csv"
    merged_data.to_csv(merged_output_path, index=False)

    print(f"Merged dataset with MVP status saved to {merged_output_path}")

except Exception as e:
    print(f"Error during merging: {e}")
